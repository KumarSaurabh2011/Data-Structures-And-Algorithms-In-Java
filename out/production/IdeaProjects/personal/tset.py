from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
from pandasql import sqldf
import csv
import os
df = pd.read_csv(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/Real-Time Stock Indices Futures.csv')
df1 = sqldf('select * from df where "Index" NOT IN ("S&P 500 VIX","Nifty 50", "Bank NIFTY")')
df2 = sqldf('select * from df where "Index" = "Nifty 50"')

#df3 = df1["Chg."].str.replace(',','')
#df4= sqldf('select avg("Chg.") as chg from df3')
df4= sqldf('select avg("Chg.") as chg from df1')
df5 = sqldf('select "Chg." as chg from df2')
df6 = sqldf('select df4.chg as world,df5.chg as nif from df4 join df5')
df6.to_csv(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/today.csv',mode='a',header=False,index=False)

# Assuming your data is stored in data1 and data2
data1 = []
data2 = []

with open(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/today.csv', newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
# Iterate over each row in the CSV file
    for row in csv_reader:
    # Assuming there are two columns in your CSV file
    # Append the data from each column to the respective lists
        data1.append(float(row[0]))
        data2.append(float(row[1]))

print("Data from column 1:", data1)
print("Data from column 2:", data2)
# Combine the data into a single array or DataFrame
data = np.column_stack((data1, data2))

# Check for stationarity
def check_stationarity(series):
    result = adfuller(series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t{}: {}'.format(key, value))

# Check stationarity for each series
for i in range(data.shape[1]):
    print('Stationarity test for variable', i+1)
    check_stationarity(data[:, i])
    print()

# Fit VAR model
model = VAR(data)

# Select lag order using AIC
best_order = model.select_order(maxlags=3)
lag_order = best_order.selected_orders['aic']
print('Best lag order:', lag_order)

# Fit VAR model with the selected lag order
model_fitted = model.fit(lag_order)

# Forecast
forecast_horizon = 3  # Adjust as needed
# Forecasting based on past values of data1
forecast = model_fitted.forecast(data[-lag_order:], steps=forecast_horizon)

# Print the forecast
print('Forecast for the next', forecast_horizon, 'steps:')
print(forecast)


os.remove(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/Real-Time Stock Indices Futures.csv')