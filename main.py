import pandas as pd

file = r'C:\Users\henri\Desktop\apostas.xlsx'
df_bens = pd.read_excel(file)

print(len(df_bens))
print(df_bens.head(5))