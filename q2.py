import sys
import pandas as pd

df = pd.read_csv(r"C:\\Users\\Chris\\Documents\\Python Scripts\\sample-input-2.txt", sep = ",", header = 0)

columns = []
for col in df.columns:
    columns.append(col)

for col in columns:
    for idx, row in df.iterrows():
        if col == row['ID']:
            df = df.drop([idx])

df = df.drop_duplicates(subset=['ID'], keep='last')
df = df.sort_values(['ID'], ascending=True)
print(df.to_csv(index=False))