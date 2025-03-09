#Vamos limpar os dados e remover uma coluna para melhorar a visualização dos dados
import pandas as pd

df = pd.read_csv('ecommerce_sales.csv') 

df = df.drop(columns=['Total']) 
df = df.drop_duplicates() 

df['Date'] = pd.to_datetime(df['Date']) 
df['Category'] = df['Category'].astype('category') 

df['Total_Sales'] = df['Quantity'] * df['Price_Unitary'] 
df.sort_values(by='Total_Sales', ascending=False, inplace=True) 

df.to_csv('sales_clean.csv', index=False) 