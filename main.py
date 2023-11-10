import openai
import time
import yfinance as yf

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

def get_stock_price(symbol: str) -> float:
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return price

tools_list = [{"type": "retrieval"},
    {
    "type": "function",
    "function": {

        "name": "get_stock_price",
        "description": "Retrieve the latest closing price of a stock using its ticker symbol",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "The ticker symbol of the stock"
                }
            },
            "required": ["symbol"]
        }
    }
}]

# Initialize the client
client = openai.OpenAI()

# Upload a file with an "assistants" purpose
file = client.files.create(
    file=open("apple.pdf", "rb"),
    purpose='assistants'
)

# Create an Assistant
assistant = client.beta.assistants.create(
    name="Financial Advisor Assistant",
    instructions="You are a personal Financial Advisor Assistant",
    tools=tools_list,
    model="gpt-4-1106-preview",
    file_ids=[file.id],
)

# Create a Thread
thread = client.beta.threads.create()

# Add a Message to a Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Can you give me a buy or hold suggestion based on Apple's stock prices and report?",
    file_ids=[file.id]
)

# Run the Assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Daniel Romero."
)

print(run.model_dump_json(indent=4))

while True:
    time.sleep(5)

    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print(run_status.model_dump_json(indent=4))

    if run_status.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        for msg in messages.data:
            role = msg.role
            content = msg.content[0].text.value
            print(f"{role.capitalize()}: {content}")

        break
    elif run_status.status == 'requires_action':
        print("Function Calling")
        required_actions = run_status.required_action.submit_tool_outputs.model_dump()
        print(required_actions)
        tool_outputs = []
        import json
        for action in required_actions["tool_calls"]:
            func_name = action['function']['name']
            arguments = json.loads(action['function']['arguments'])
            
            if func_name == "get_stock_price":
                output = get_stock_price(symbol=arguments['symbol'])
                tool_outputs.append({
                    "tool_call_id": action['id'],
                    "output": output
                })
            else:
                raise ValueError(f"Unknown function: {func_name}")
            
        print("Assistant outputs...")
        client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
    else:
        print("Waiting for the Assistant response...")
        time.sleep(5)