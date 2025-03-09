import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('c:/Users/User/Documents/DataScienceFInal/Start/sales_clean.csv')
df['Date'] = pd.to_datetime(df['Date'])

x = df[['Quantity', 'Price_Unitary']]
y = df['Total_Sales']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=44)
model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('real values')
plt.ylabel('predictions')
plt.title('Predictions vs. Actual Values')
plt.show()

