import pandas as pd

df = pd.read_csv("어쩌구저쩌구", encoding='utf-8')

# 매수/매도 by MACD
df["MACD_sign"] = df.apply(lambda x: ("매수" if x["MACD"]>x["MACD_signal"] else "매도"), axis=1)

# 매수/매도 by MACD oscillator
df["MACD_oscillator_sign"] = df.apply(lambda x: ("매수" if x["MACD"]>x["MACD_signal"] else "매도"), axis=1)

# 매수/매도 by RSI 50
df["RSI_sign_50"] = df.apply(lambda x: ("매수" if x["RSI"]>50 else "매도"), axis=1)

# 매수/매도 by RSI 30 70
df["RSI_sign_3070"] = df.apply(lambda x: ("매수" if x["RSI"]<30 else ("매도" if x["RSI"]>70 else '-')), axis=1)