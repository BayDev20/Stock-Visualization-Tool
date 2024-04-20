from flask import Flask, request, render_template, Response
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import io

app = Flask(__name__)

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1mo")

def add_technical_indicators(prices):
    delta = prices['Close'].diff()
    gain = (delta.where(delta > 0, 0)).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.where(delta < 0, 0)).ewm(alpha=1/14, adjust=False).mean()
    rs = gain / loss
    prices['RSI'] = 100 - (100 / (1 + rs))
    return prices

def signal_markers(prices):
    buy_signals = (prices['RSI'] > 30) & (prices['RSI'].shift(1) <= 30)
    sell_signals = (prices['RSI'] < 70) & (prices['RSI'].shift(1) >= 70)
    prices['Buy'] = np.where(buy_signals, prices['Close'], np.nan)
    prices['Sell'] = np.where(sell_signals, prices['Close'], np.nan)
    return prices

def plot_data(prices, ticker):
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
    ax1.plot(prices.index, prices['Close'], label='Close', color='dodgerblue', linewidth=2)
    ax1.scatter(prices.index, prices['Buy'], color='green', label='Buy', marker='^', s=100)
    ax1.scatter(prices.index, prices['Sell'], color='red', label='Sell', marker='v', s=100)
    ax1.set_title(f"Price Chart for {ticker}")
    ax1.set_ylabel('Price')
    ax1.legend(loc='upper left')
    ax2.plot(prices.index, prices['RSI'], label='RSI', color='purple')
    ax2.axhline(70, linestyle='--', color='red', alpha=0.5)
    ax2.axhline(30, linestyle='--', color='green', alpha=0.5)
    ax2.set_ylabel('RSI')
    ax2.set_ylim([0, 100])
    ax2.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        if ticker:
            prices = fetch_stock_data(ticker)
            prices = add_technical_indicators(prices)
            prices = signal_markers(prices)
            img = plot_data(prices, ticker)
            return Response(img.getvalue(), mimetype='image/png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)