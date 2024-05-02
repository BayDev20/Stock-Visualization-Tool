# Stock Data Visualization Tool

This Python script leverages the `yfinance` library to fetch and display stock data after a user types in a ticker such as AAPL or BTC-USD. It includes price movements and volume along with a buy/sell indicator.* Indicator uses key financial indicators like the RSI (Relative Strength Index) to determine signals. Designed for financial analysts and hobbyists alike, this tool provides insightful visualizations to aid in stock market analysis.

![image](https://github.com/BayDev20/Stock-Visualization-Tool/assets/152105436/4d82c2fc-7eff-4230-923e-8768299e6fae)



## Features

- Fetch and display closing prices.
- Calculate and visualize daily returns.
- Visualize relative Strength index.
- Based on key trading indicators: Moving Averages, MACD, RSI.
- Plot data using Matplotlib for clear, informative visualizations.

![image](https://github.com/BayDev20/Stock-Visualization-Tool/assets/152105436/e8df551e-475d-4814-ba1f-4da20184e90c)


## Prerequisites

Before you begin, ensure you have the following:
- Python 3.x installed on your system.
- `yfinance`, `flask`, and `matplotlib` libraries installed.

## Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/stock-analysis-tool.git
cd stock-analysis-tool
```
## Step 2: Set Up a Virtual Environment (Optional but Recommended)
It's a good practice to use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
## Step 4: Run the Application
Start the Flask server:
```bash
python stocks.py
```
## Step 5: Access the Application
Open a web browser and go to http://127.0.0.1:5000 to start using the application.
## Usage
To use the application, follow these steps:

Enter a Stock Ticker: Input the symbol of the stock you want to analyze (e.g., AAPL, GOOGL, MSFT) in the text field.
Submit: Click the "Show Chart" button to display the stock's price graph and RSI chart.
View Results: The results will display directly on the web page with options to analyze another stock.

### *Disclaimer
This Stock Analysis Tool is provided for informational and educational purposes only. It is designed for fun and to help users learn more about stock market trends through visual analysis. It is not intended for financial investment or trading purposes.

The data and information provided by this tool do not constitute financial advice, and users should not make any investment decision based solely on the output from this tool. All users should conduct their own research and consider seeking advice from independent financial advisors before making any investment decisions.

By using this tool, you acknowledge and agree that any reliance on or use of the information available through this tool is entirely at your own risk. The developer or provider of this tool shall not be liable for any losses or damages arising from the use of this tool.


