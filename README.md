# Stock Data Visualization Tool

This Python script leverages the `yfinance` library to fetch and display stock data after a user types in a ticker such as AAPL or BTC-USD. It includes price movements and volume along with a buy/sell indicator.* Inicator uses key financial indicators like moving averages, MACD (Moving Average Convergence Divergence), and RSI (Relative Strength Index) to determine signals. Designed for financial analysts and hobbyists alike, this tool provides insightful visualizations to aid in stock market analysis.

## Features

- Fetch and display closing prices and trading volume.
- Calculate and visualize daily returns.
- Based on key trading indicators: Moving Averages, MACD, RSI.
- Plot data using Matplotlib for clear, informative visualizations.

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
