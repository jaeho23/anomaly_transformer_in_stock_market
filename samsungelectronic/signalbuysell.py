import pandas as pd

data = ['RSI', 'MACD']#, 'MACD_oscillator']
for x in data:
    df = pd.read_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{x}.csv", encoding='utf-8')

# 각각의 전략에서 매수/매도 시 전체 수익률 & 연평균 수익률 산출
    tot = 1000000
    y = 0
    xx = 0
    for i in range(len(df)):
        if df.iloc[i][-1] == '매수':
            if y == 0:
                y = tot // df.iloc[i][1]
                xx = tot % df.iloc[i][1]
        elif df.iloc[i][-1] == '매도':
            if y != 0:
                tot = y * df.iloc[i][1] + xx
                xx = 0
                y = 0
    
    print(f"전략 : {x} \n 투자금 : 1,000,000, 최종잔액 : {tot} \n 수익률 : {(tot-1000000) / 10000} 연평균 수익률 : {(tot-1000000) / 230000}")