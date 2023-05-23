import pandas as pd

df = pd.read_csv("어쩌구저쩌구", encoding='utf-8')

# 매수/매도 by MACD(0 돌파 시 매수/매도)
df["MACD_sign"] = df.apply(lambda x: ("매수" if x["MACD"]>x["MACD_signal"] else "매도"), axis=1)

# 매수/매도 by MACD oscillator(0 돌파 시 매수/매도)
df["MACD_oscillator_sign"] = df.apply(lambda x: ("매수" if x["MACD"]>x["MACD_signal"] else "매도"), axis=1)

# 매수/매도 by RSI 50(50 돌파 시 매수/매도)
df["RSI_sign_50"] = df.apply(lambda x: ("매수" if x["RSI"]>50 else "매도"), axis=1)

# 매수/매도 by RSI 30 70 (30 전환 시 매수, 70 전환 시 매도)
df["RSI_sign_3070"] = df.apply(lambda x: ("매수" if x["RSI"]<30 else ("매도" if x["RSI"]>70 else '-')), axis=1)

# 각각의 전략에서 매수/매도 시 전체 수익률 & 연평균 수익률 산출
x = 1000000
