import pandas as pd

data = ['MACD']
data1 = ['train', 'train_label', 'test', 'test_label']

for x in data:
    tot_data = []
    n = []
    df = pd.read_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{x}.csv", encoding='utf-8')
    for i in range(len(df)-1):
        if df.iloc[i,-1] == '매수':
            if df.iloc[i+1,1] < df.iloc[i,1]:
                tot_data.append(df.iloc[i,:])
                n.append(1)
            else: n.append(0)
        elif df.iloc[i,-1] == '매도':
            if df.iloc[i+1,1] > df.iloc[i,1]:
                tot_data.append(df.iloc[i,:])
                n.append(1)
            else: n.append(0)

    tot_data = pd.DataFrame(tot_data)
    df['anomaly'] = pd.DataFrame(n)
    df.dropna()
    
    for y in data1:
        if y == 'train':
            k = df.truncate(after=4041, axis=0)
            k = k.iloc[:,:3]
            k.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{y}.csv", index=False)
        elif y == 'test':
            k = df.truncate(before=4041, axis=0)
            k = k.iloc[:,:3]
            k.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{y}.csv", index=False)
        elif y == 'train_label':
            k = df.truncate(after=4041, axis=0)
            k = k.iloc[:,-1]
            k.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{y}.csv", index=False)
        else:
            k = df.truncate(before=4041, axis=0)
            k = k.iloc[:,-1]
            k.to_csv(f"C:/Users/SLOWLAB/.conda/anomaly_transformer_in_stock_market/data/{y}.csv", index=False)