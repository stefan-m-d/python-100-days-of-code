import pandas as pd

excel_file = 'Fast Track ML with Python course\sales data.xlsx'

df = pd.read_excel(excel_file)

print(df.head())