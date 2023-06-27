import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import datetime
import yfinance as yfin

yfin.pdr_override()

strategy = ['MACD']
start = datetime.date(2000, 1, 1)
end = datetime.date(2022, 12, 31)
samsungelectronic = pdr.get_data_yahoo("005930.KS", start, end)
df = samsungelectronic
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df['변화량'] = df['Close'] - df['Close'].shift(1)
df['상승폭'] = np.where(df['변화량']>=0, df['변화량'], 0)
df['하락폭'] = np.where(df['변화량'] <0, df['변화량'].abs(), 0)

# MACD & MACD oscillator
macd_short, macd_long, macd_signal=12, 26, 9 #기본값
df["MACD_short"] = df["Close"].ewm(span = macd_short).mean()
df["MACD_long"] = df["Close"].ewm(span = macd_long).mean()
df["MACD"] = df.apply(lambda x: (x["MACD_short"] - x["MACD_long"]), axis = 1)
df["MACD_signal"] = df["MACD"].ewm(span = macd_signal).mean()  
df["MACD_oscillator"] = df.apply(lambda x:(x["MACD"] - x["MACD_signal"]), axis = 1)

# welles moving average
# df['AU'] = df['상승폭'].ewm(alpha = 1/14, min_periods = 14).mean()
# df['AD'] = df['하락폭'].ewm(alpha = 1/14, min_periods = 14).mean()
# df['RSI'] = df['AU'] / (df['AU'] + df['AD']) * 100

# 매수/매도 by MACD(0 돌파 시 매수/매도)
df["MACD_sign"] = df.apply(lambda x: ("매수" if x["MACD"]<x["MACD_signal"] else "매도"), axis=1)

# 매수/매도 by MACD oscillator(0 돌파 시 매수/매도)
#df["MACD_oscillator_sign"] = df.apply(lambda x: ("매수" if x["MACD"]>x["MACD_signal"] else "매도"), axis=1)

# 매수/매도 by RSI 30 70 (30 전환 시 매수, 70 전환 시 매도)
#df["RSI_sign"] = df.apply(lambda x: ("매수" if x["RSI"]<50 else "매도"), axis=1)

df = df.sort_index(axis=1)

for x in strategy:
    if x=='RSI':
        k = df[['Close', 'RSI', 'RSI_sign']]
    elif x=='MACD':
        k = df[['Close', 'MACD', "MACD_sign"]]
    # else :
    #     k = df[['Close', 'MACD_oscillator', "MACD_oscillator_sign"]]

    k = k.dropna()
    k.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{x}.csv")