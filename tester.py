print("Test")


import yfinance as yf
arg = 'asd'

data = yf.download(tickers=arg, period='1mo', interval='60m')