import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

df = pd.read_csv('c:/Users/User/Documents/DataScienceFInal/Start/sales_clean.csv')

print(df.describe())

for column in df.columns:
    if np.issubdtype(df[column].dtype, np.number):
        media = np.mean(df[column])
        mediana = np.median(df[column])
        variancia = np.var(df[column], ddof=1)
        desvio_padrao = np.std(df[column], ddof=1)
        minimo = np.min(df[column])
        maximo = np.max(df[column])
        
        print(f"Coluna: {column}")
        print(f"Média: {media}")
        print(f"Mediana: {mediana}")
        print(f"Variância: {variancia}")
        print(f"Desvio Padrão: {desvio_padrao}")
        print(f"Mínimo: {minimo}")
        print(f"Máximo: {maximo}")
        print()

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Total_Sales', data=df, estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Total_Sales'], bins=30, kde=True)
plt.title('Distribution of Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Frequency')
plt.show()

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
sales_trend = df['Total_Sales'].resample('M').sum()

plt.figure(figsize=(10, 6))
sales_trend.plot()
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

#estatistica

categories = df['Category'].unique()
total_sales = [df[df['Category'] == category]['Total_Sales'] for category in categories]
anova_result = f_oneway(*total_sales)
print(f"ANOVA result: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")

if anova_result.pvalue < 0.05:
    print("There is a statistical difference between different product categories.")
else:
    print("There are no significant differences in sales between different product categories.")
