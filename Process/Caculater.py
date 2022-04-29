def SMA(data, period = 30,column = "close"):
  return data[column].rolling(window=period).mean()

def EMA(data, period = 20,column = "close"):
  return data[column].ewm(span=period,adjust=False).mean()

def MACD(data,period_long = 26, period_short = 12, period_signal=9,column='close'):
  ShortEMA = EMA(data, period = period_short,column = column)
  LongEMA = EMA(data, period = period_long,column = column)
  data["MACD"] = ShortEMA-LongEMA
  data["signal_Line"] = EMA(data, period = period_signal,column = "MACD")
  return data

def RSI(data, period=20,column='close'):
  delta = data[column].diff(1)
  delta = delta.dropna()
  up = delta.copy()
  down = delta.copy()
  up[up<0] = 0
  down[down>0] = 0
  data["up"] = up
  data["down"] = down
  AVG_Gain = SMA(data,period,column='up')
  AVG_Loss = abs(SMA(data,period,column='down'))
  RS = AVG_Gain/AVG_Loss
  RSI = 100-(100/(1+RS))
  data["RSI"] = RSI
  return data

