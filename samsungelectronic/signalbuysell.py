import pandas as pd
import numpy as np
import csv
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
 
data = ['MACD']#, 'MACD_oscillator']
for x in data:
    df = pd.read_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{x}.csv", encoding='utf-8')
    df = df.truncate(before=4041, axis=0)

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
    
    print(f"전략 : {x} \n투자금 : 1,000,000원 최종잔액 : {int(tot):,}원 \n수익률 : {(tot-1000000) / 10000}% 연평균 수익률 : {(tot-1000000) / 70527.7778}%")

tot = 1000000
kk = tot % df.iloc[0][1] 
k = tot // df.iloc[0][1]
tot = df.iloc[-1][1] * k + kk
print(f"전략 : Buy-and-hold \n투자금 : 1,000,000원 최종잔액 : {int(tot):,}원 \n수익률 : {(tot-1000000) / 10000}% 연평균 수익률 : {(tot-1000000) / 70527.7778}%")
 ######################################### 결과뽑기 #############################################
df1 = df.copy()
df1['anomaly'] = 0
ll = list()
f = open("C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/predict.csv", 'r', encoding='utf-8-sig')
rea = csv.reader(f)
for row in rea:
    ll.extend(row)
f.close

for i in range(len(df1)):
    if i == 0:
        # df1.iloc[i][-1] = 0
        continue
    elif i == len(df1) - 1:
        continue
    else:
        df1.loc[i+4041, 'anomaly'] = float(ll[i-1])
#print(df1)
tot = 1000000
y = 0
xx = 0
for i in range(len(df1)):
    if df1.iloc[i][-2] == '매수':
        if df1.iloc[i][-1] == 0:
            if y == 0:
                y = tot // df1.iloc[i][1]
                xx = tot % df1.iloc[i][1]
    elif df1.iloc[i][-2] == '매도':
        if df1.iloc[i][-1] == 0:
            if y != 0:
                tot = y * df1.iloc[i][1] + xx
                xx = 0
                y = 0

print(f"전략 : Anomaly-Transformer \n투자금 : 1,000,000원 최종잔액 : {int(tot):,}원 \n수익률 : {(tot-1000000) / 10000}% 연평균 수익률 : {(tot-1000000) / 70527.7778}%")