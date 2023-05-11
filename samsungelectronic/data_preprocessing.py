import pandas as pd
import numpy as np

data = ['test_label.csv', 'test.csv', 'train.csv']
for x in data:
    df = pd.read_csv("C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/samsungelectronic/train.csv", encoding="utf-8")

    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    df['변화량'] = df['종가'] - df['종가'].shift(1)
    df['상승폭'] = np.where(df['변화량']>=0, df['변화량'], 0)
    df['하락폭'] = np.where(df['변화량'] <0, df['변화량'].abs(), 0)

    # welles moving average
    df['AU'] = df['상승폭'].ewm(alpha=1/14, min_periods=14).mean()
    df['AD'] = df['하락폭'].ewm(alpha=1/14, min_periods=14).mean()
    #df['RS'] = df['AU'] / df['AD']
    #df['RSI'] = 100 - (100 / (1 + df['RS']))
    df['RSI'] = df['AU'] / (df['AU'] + df['AD']) * 100
    df[['RSI']].tail(n=10)
    df = df.dropna()
    
    df.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/samsungelectronic/{x}")