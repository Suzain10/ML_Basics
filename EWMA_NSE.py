# -*- coding: utf-8 -*-
"""EWMA_NSE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14RMqpwcnr2ERtV9vx7kNestU7PTBluGv
"""

pip install yfinance pandas matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download historical data from Yahoo Finance
ticker = "TCS.NS"  # TCS stock ticker on NSE (National Stock Exchange of India)
data = yf.download(ticker, start="2023-01-01", end="2023-06-29") # Adjust date range as needed

# Step 2: Calculate short-term (20 days) and long-term (100 days) EWMA
data['EWMA_short'] = data['Close'].ewm(span=20, adjust=True).mean()
data['EWMA_long'] = data['Close'].ewm(span=100, adjust=True).mean()

# Step 3: Plotting
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', linewidth=2)
plt.plot(data['EWMA_short'], label='EWMA (20 days)', linestyle='--')
plt.plot(data['EWMA_long'], label='EWMA (100 days)', linestyle='--')
plt.title('Exponentially Weighted Moving Averages for TCS')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download historical data from Yahoo Finance
ticker = "MRF.NS"  # TCS stock ticker on NSE (National Stock Exchange of India)
data = yf.download(ticker, start="2023-01-01", end="2023-06-29")   # Adjust date range as needed

# Step 2: Calculate short-term (20 days) and long-term (100 days) EWMA
data['EWMA_short'] = data['Close'].ewm(span=20, adjust=True).mean()
data['EWMA_long'] = data['Close'].ewm(span=100, adjust=True).mean()

# Step 3: Plotting
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', linewidth=2)
plt.plot(data['EWMA_short'], label='EWMA (20 days)', linestyle='--')
plt.plot(data['EWMA_long'], label='EWMA (100 days)', linestyle='--')
plt.title('Exponentially Weighted Moving Averages for TCS')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

