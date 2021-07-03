import yfinance as yf

def toUpper(symbol):
    return symbol.upper()

def roundTwo(number):
    number = round(number,2)
    return number

def higherLower(open, current):
    diff = current - open
    if diff > 0:
        return 0x00FF00
    if diff < 0:
        return 0xFF0000
    else:
        return 0xFFFFFF

def percentCalc(open,current):
    percent = roundTwo(100*(current-open)/open)
    if percent < 0:
        percent = str(percent) + "%"
    else:
        percent = "+" + str(percent) + "%"
    return percent

def exist(symbol):
    try:
        data = yf.download(tickers= symbol, period='1d', interval='1h')
        x = data["Close"][-1]
        return True
    except:
        return False

def interval(arg_two):
    valid = ['1m','2m','5m','15m','30m','1h','90m']
    if arg_two in valid:
        return True
    else:
        return False
