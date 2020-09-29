import pandas as pd
import recorte as rc

file = r'C:\Users\henri\Desktop\apostas.xlsx'
df_bens = pd.read_excel(file)

print(len(df_bens))

new_df = rc.corte(df_bens,10,20)

print(len(new_df))