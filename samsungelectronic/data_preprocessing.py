import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import datetime
import yfinance as yfin

yfin.pdr_override()

data = ['train', 'train_label', 'test', 'test_label']
start = datetime.date(2000, 1, 1)
end = datetime.date(2022, 12, 31)
samsungelectronic = pdr.get_data_yahoo("005930.KS", start, end)
df = samsungelectronic
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df['변화량'] = df['Close'] - df['Close'].shift(1)
df['상승폭'] = np.where(df['변화량']>=0, df['변화량'], 0)
df['하락폭'] = np.where(df['변화량'] <0, df['변화량'].abs(), 0)

# welles moving average
df['AU'] = df['상승폭'].ewm(alpha=1/14, min_periods=14).mean()
df['AD'] = df['하락폭'].ewm(alpha=1/14, min_periods=14).mean()
#df['RS'] = df['AU'] / df['AD']
#df['RSI'] = 100 - (100 / (1 + df['RS']))
df['RSI'] = df['AU'] / (df['AU'] + df['AD']) * 100
df[['RSI']].tail(n=10)

df = df.sort_index(axis=1)

for x in data:
    if x=='train':
        k = df.truncate(after='2020-01-01', axis=0)
        print(k)
        k = k.truncate(after='Volume',axis=1)
    elif x=='train_label':
        k = df.truncate(after='2020-01-01', axis=0)
        k = k.truncate(before='RSI',axis=1)
    elif x=='test':
        k = df.truncate(before='2020-01-01', axis=0)
        k = k.truncate(after='Volume',axis=1)
    else:
        k = df.truncate(before='2020-01-01', axis=0)
        k = k.truncate(before='RSI',axis=1)
    
    k = k.dropna()
    
    k.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/samsungelectronic/RSI_{x}.csv")