## OpenAI function calling and retrieval for a financial advisor

Idea: [FinGPT](https://arxiv.org/abs/2306.06031) assistant - using OpenAI function calling and retrieval

Setup:

Edit `.env` and insert OpenAI API key,
then install the dependencies:
```
pip install -r requirements.txt

python main.py
```

---
## Output example:

*User:* Can you give me a buy or hold suggestion based on Apple's stock prices and report?

*Assistant:* Based on the information from Apple's 2023 Form 10-K report and the current stock price of Apple Inc. (AAPL), here are the key takeaways:

1. **Stock Price**: As of the time of inquiry, the last closing stock price for AAPL was approximately $185.27.

2. **Fiscal Year Highlights**:
   - Total net sales: $383.3 billion
   - Net income: $97.0 billion during 2023
   - A decrease in total net sales by 3% or $11.0 billion in 2023 compared to 2022, mostly due to weaker foreign currencies relative to the U.S. dollar and lower sales of Mac and iPhone, partially offset by higher Service sales.

3. **Product Announcements and Updates**:
   - Throughout 2023, Apple announced new products, services, and updates including new models of iPads, Macs, and iPhones.

4. **Share Repurchase and Dividend**:
   - A new share repurchase program announced in May 2023, authorizing up to $90 billion in stock repurchases.
   - The Company repurchased $76.6 billion of its common stock and paid $15.0 billion in dividends and dividend equivalents in 2023.

5. **Macroeconomic Conditions**:
   - Macroeconomic factors such as inflation, changes in interest rates, and currency fluctuations continue to have a direct and indirect impact on Apple's financial performance.

6. **Geographical Performance**:
   - Decreases in net sales were observed in the Americas, Europe, Greater China, and Japan due to various factors, including unfavorable foreign exchange rates. However, there was a slight increase in net sales in the Rest of Asia Pacific region.

Based on these insights, while it is evident that Apple continues to navigate through macroeconomic challenges and foreign currency impacts, the company's ability to generate substantial net sales and income, its consistent product innovation, and commitment to shareholder returns through repurchase programs and dividends showcase resilience.

As for a buy or hold suggestion, this would depend on your individual investment strategy, risk tolerance, and outlook on future company performance as related to industry trends and overall market conditions. While the 2023 report indicates a slight decrease in revenue compared to the previous year, it's important to balance this with Apple's strong financial position, consistent innovation, and ongoing share repurchase initiatives. If you believe in the long-term growth of the company and that the stock price reflects fair value or undervaluation, you might consider this a buying opportunity. On the other hand, if you currently hold AAPL stock and find these fundamentals reassuring relative to your investment thesis, it could support a decision to hold.

Please consult with a financial advisor to align this information with your personal investment goals and to obtain the most current stock market analysis before making any investment decisions.
