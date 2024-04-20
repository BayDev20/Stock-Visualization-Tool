import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker):
    """ Fetch historical stock data """
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist  # Return the whole DataFrame

def calculate_returns(prices):
    """ Calculate percentage change returns """
    returns = prices['Close'].pct_change()[1:]
    return returns

def add_rsi(prices, periods=14):
    """ Add Relative Strength Index (RSI) to the DataFrame """
    close_delta = prices['Close'].diff()
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    prices['RSI'] = rsi
    return prices

def add_macd(prices):
    """ Add Moving Average Convergence Divergence (MACD) to the DataFrame """
    exp1 = prices['Close'].ewm(span=12, adjust=False).mean()
    exp2 = prices['Close'].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    prices['MACD'] = macd
    prices['Signal'] = signal
    return prices

def add_moving_averages(prices):
    """ Add moving averages to the DataFrame """
    prices['MA50'] = prices['Close'].rolling(window=50).mean()
    prices['MA200'] = prices['Close'].rolling(window=200).mean()
    return prices

def plot_with_volume(prices, returns, ticker):
    """ Plot closing prices and volume as a subplot """
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(prices['Close'], 'g-')
    ax2.bar(prices.index, prices['Volume'], color='gray', alpha=0.3)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Close Price', color='g')
    ax2.set_ylabel('Volume', color='gray')
    plt.title(f"Price and Volume for {ticker}")
    plt.show()

def plot_data(returns, ticker):
    """ Plot daily returns """
    plt.figure(figsize=(10, 5))
    plt.plot(returns, color='magenta', linestyle='-', linewidth=2, label=f'Daily Returns of {ticker}')
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
    plt.title(f'Daily Returns Over Time for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Returns (%)')
    plt.legend()
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.show()

top_stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'BRK-B', 'V', 'JNJ', 'WMT']

for ticker in top_stocks:
    prices = fetch_stock_data(ticker)
    prices = add_moving_averages(prices)
    prices = add_macd(prices)
    prices = add_rsi(prices)
    returns = calculate_returns(prices)
    plot_with_volume(prices, returns, ticker)  # Pass ticker for the title