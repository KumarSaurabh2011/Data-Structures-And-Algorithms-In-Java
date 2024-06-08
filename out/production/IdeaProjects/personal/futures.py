

import pandas as pd
import glob
from pandasql import sqldf
import sqlalchemy
import datetime
from datetime import date
from datetime import timedelta

folder_path = '/Users/kumarsaurabh/Downloads/fnobavcopydata'
folder_path1 = '/Users/kumarsaurabh/Downloads/xx'
file_list = glob.glob(folder_path + "/*bhav.csv")
#main_dataframe = pd.DataFrame(pd.read_csv(file_list[0], encoding='utf-8'))
#m_d = sqldf("select sum(OPEN_INT) as OI,SYMBOL,INSTRUMENT from main_dataframe where INSTRUMENT = 'FUTSTK' group by SYMBOL ")
new_list = []
new_list1 = []
for i in range(0, len(file_list)):
    data = pd.read_csv(file_list[i])
    df = pd.DataFrame(data)
    d_f = sqldf("select sum(OPEN_INT) as OI , sum(CLOSE) as CLOSE,sum(CONTRACTS) as CONTRACTS,sum(VAL_INLAKH) as VAL_INLAKH ,SYMBOL,INSTRUMENT from df where INSTRUMENT = 'FUTSTK' group by SYMBOL ")
    d_f1 = sqldf("select sum(OPEN_INT) as OI , sum(CLOSE) as CLOSE,sum(CONTRACTS) as CONTRACTS,sum(VAL_INLAKH) as VAL_INLAKH, SYMBOL,INSTRUMENT,OPTION_TYP from df where INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP ")
    new_list.append(d_f)
    new_list1.append(d_f1)

main_dataframe = pd.concat(new_list)
main_dataframe1 = pd.concat(new_list1)
main_dataframe.to_pickle('/Users/kumarsaurabh/Downloads/fut_pikl.pickle')
main_dataframe1.to_pickle('/Users/kumarsaurabh/Downloads/opt_pikl.pickle')
#df_mf = main_dataframe[main_dataframe['INSTRUMENT'] == 'FUTSTK'].groupby('SYMBOL')['OI'].median()
#df_mOP = main_dataframe1[main_dataframe1['INSTRUMENT'] == 'OPTSTK'].groupby(['SYMBOL','OPTION_TYP'])['OI'].median()

df_mf = main_dataframe.groupby('SYMBOL').OI.quantile(0.70)
df_mOP = main_dataframe1.groupby(['SYMBOL', 'OPTION_TYP']).OI.quantile(0.70)
#d1_mf.to_csv('/Users/kumarsaurabh/Downloads/new_csvQUANTF.csv')
#d1_mOP.to_csv('/Users/kumarsaurabh/Downloads/new_csvQUANTOP.csv')
#df_mf=pd.read_csv('/Users/kumarsaurabh/Downloads/new_csvQUANTF.csv')
#df_mOP=pd.read_csv('/Users/kumarsaurabh/Downloads/new_csvQUANTOP.csv')
#df_mf.columns = ['SYMBOL', 'QUANTILE', 'OI']
#df_mOP.columns = ['SYMBOL', 'OPTION_TYP', 'QUANTILE', 'OI']




df_mf.to_csv('/Users/kumarsaurabh/Downloads/new_csv00.csv')
df_mOP.to_csv('/Users/kumarsaurabh/Downloads/new_csv000.csv')
dfx = sqldf("select cast(ROUND(AVG(OI)) as int) as AVG_OI ,max(OI) as MAX_OI,SYMBOL,INSTRUMENT,  AVG(CLOSE) as close, AVG(CONTRACTS) as contracts, AVG(VAL_INLAKH) as val_inlakh from main_dataframe where"
            " INSTRUMENT = 'FUTSTK' group by SYMBOL")
dfx.to_csv('/Users/kumarsaurabh/Downloads/new_csv1.csv')

dfx1 = sqldf("select ROUND(AVG(OI)) as AVG_OI ,max(OI) as MAX_OI,SYMBOL,INSTRUMENT,OPTION_TYP ,  AVG(CLOSE) as close, AVG(CONTRACTS) as contracts, AVG(VAL_INLAKH) as val_inlakh from main_dataframe1 where"
            " INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP")
dfx1 .to_csv('/Users/kumarsaurabh/Downloads/new_csv2.csv')


x = datetime.datetime.now()
y = x.strftime("%d%b%Y")
z = 'fo'+y+'bhav.csv'
data1 = pd.read_csv(folder_path1+"/"+z)
df1 = pd.DataFrame(data1)
d_f2 = sqldf("select sum(OPEN_INT) as OI , SYMBOL ,INSTRUMENT, sum(CLOSE) as cls ,sum(CONTRACTS) as cont,sum(VAL_INLAKH) as val_in_lak from df1 where INSTRUMENT = 'FUTSTK' group by SYMBOL ")
d_f3 = sqldf("select sum(OPEN_INT) as OI , SYMBOL,INSTRUMENT,OPTION_TYP, sum(CLOSE) as cls ,sum(CONTRACTS) as cont,sum(VAL_INLAKH) as val_in_lak from df1 where INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP ")

d_f2.to_csv('/Users/kumarsaurabh/Downloads/new_csv3.csv')
d_f3 .to_csv('/Users/kumarsaurabh/Downloads/new_csv4.csv')

df10= sqldf("select d_f2.cls,d_f2.cont,d_f2.val_in_lak,dfx.avg_oi,dfx.MAX_OI,d_f2.OI,d_f2.symbol,d_f2.Instrument,(d_f2.OI-dfx.avg_oi) as diff , dfx.CLOSE,dfx.CONTRACTS,dfx.VAL_INLAKH "
            "from dfx inner join d_f2  on dfx.SYMBOL=d_f2.SYMBOL")
df10.to_csv('/Users/kumarsaurabh/Downloads/new_csv7.csv')

df11= sqldf("select d_f3.cls,d_f3.cont,d_f3.val_in_lak,dfx1.avg_oi,dfx1.MAX_OI,d_f3.OI,d_f3.symbol,d_f3.Instrument,d_f3.OPTION_TYP,(d_f3.OI-dfx1.avg_oi) as diff, dfx1.CLOSE,dfx1.CONTRACTS,dfx1.VAL_INLAKH "
            "from dfx1 inner join d_f3  on dfx1.SYMBOL=d_f3.SYMBOL and dfx1.OPTION_TYP=d_f3.OPTION_TYP")
df11.to_csv('/Users/kumarsaurabh/Downloads/new_csv8.csv')



today = date.today()
yesterday = today - timedelta(days=1)
A = yesterday.strftime("%d%b%Y")
zz = 'fo'+A+'bhav.csv'

data2 = pd.read_csv(folder_path1+"/"+zz)
df2 = pd.DataFrame(data2)
d_f9 = sqldf("select sum(OPEN_INT) as OI , SYMBOL ,INSTRUMENT from df2 where INSTRUMENT = 'FUTSTK' group by SYMBOL ")
d_f99 = sqldf("select sum(OPEN_INT) as OI , SYMBOL,INSTRUMENT,OPTION_TYP from df2 where INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP ")

d_f9.to_csv('/Users/kumarsaurabh/Downloads/new_csv9.csv')
d_f99 .to_csv('/Users/kumarsaurabh/Downloads/new_csv10.csv')

df12= sqldf("select dfx.avg_oi,d_f9.OI,d_f9.symbol,d_f9.Instrument,(d_f9.OI-dfx.avg_oi) as diff "
            "from dfx inner join d_f9  on dfx.SYMBOL=d_f9.SYMBOL")
df12.to_csv('/Users/kumarsaurabh/Downloads/new_csv11.csv')

df13 = sqldf("select dfx1.avg_oi,d_f99.OI,d_f99.symbol,d_f99.Instrument,d_f99.OPTION_TYP,(d_f99.OI-dfx1.avg_oi) as diff "
            "from dfx1 inner join d_f99  on dfx1.SYMBOL=d_f99.SYMBOL and dfx1.OPTION_TYP=d_f99.OPTION_TYP")
df13.to_csv('/Users/kumarsaurabh/Downloads/new_csv12.csv')

ddf = sqldf("select df10.avg_oi,df10.oi,df10.symbol,df10.instrument,df10.diff from df10 "
            "inner join df12 on df10.symbol = df12.symbol "
            " where df12.diff <=0 and df10.diff >=0"
            )


ddf.to_csv('/Users/kumarsaurabh/Downloads/new_csv13.csv')

ddf1 = sqldf("select df11.avg_oi,df11.oi,df11.symbol,df11.instrument,df11.diff,df11.OPTION_TYP from "
             "df11 inner join df13 on df11.symbol = df13.symbol and df11.OPTION_TYP=df13.OPTION_TYP"
             " where df11.diff >=0 and df13.diff <=0")


ddf1.to_csv('/Users/kumarsaurabh/Downloads/new_csv14.csv')

x = datetime.datetime.now()
y = x.strftime("%d%b%Y")
z = 'fo'+y+'bhav.csv'
data1 = pd.read_csv(folder_path1+"/"+z)
#data1['EXPIRY_DT'] = pd.to_datetime(data1['EXPIRY_DT'], format='mixed')
#filtered = data1.loc[(data1['EXPIRY_DT'] != '28-Jun-2023')]
#df1 = pd.DataFrame(filtered)
df1 = pd.DataFrame(data1)
d_f2 = sqldf("select sum(OPEN_INT) as CURR_OI , SYMBOL ,INSTRUMENT from df1 where INSTRUMENT = 'FUTSTK' group by SYMBOL ")
d_f3 = sqldf("select sum(OPEN_INT) as CURR_OI , SYMBOL,INSTRUMENT,OPTION_TYP from df1 where INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP ")

d_f2.to_csv('/Users/kumarsaurabh/Downloads/new_csvA.csv')
d_f3 .to_csv('/Users/kumarsaurabh/Downloads/new_csvB.csv')

df10= sqldf("select df_mf.OI,d_f2.CURR_OI,d_f2.symbol,d_f2.Instrument,(d_f2.CURR_OI-df_mf.OI) as diff "
            "from df_mf inner join d_f2  on df_mf.SYMBOL=d_f2.SYMBOL")
df10.to_csv('/Users/kumarsaurabh/Downloads/new_csvC.csv')

df11= sqldf("select df_mOP.OI,d_f3.CURR_OI,d_f3.symbol,d_f3.Instrument,d_f3.OPTION_TYP,(d_f3.CURR_OI-df_mOP.OI) as diff "
            "from df_mOP inner join d_f3  on df_mOP.SYMBOL=d_f3.SYMBOL and df_mOP.OPTION_TYP=d_f3.OPTION_TYP")
df11.to_csv('/Users/kumarsaurabh/Downloads/new_csvD.csv')



today = date.today()
yesterday = today - timedelta(days=1)
A = yesterday.strftime("%d%b%Y")
zz = 'fo'+A+'bhav.csv'

data2 = pd.read_csv(folder_path1+"/"+zz)
df2 = pd.DataFrame(data2)
d_f9 = sqldf("select sum(OPEN_INT) as CURR_OI , SYMBOL ,INSTRUMENT from df2 where INSTRUMENT = 'FUTSTK' group by SYMBOL ")
d_f99 = sqldf("select sum(OPEN_INT) as CURR_OI , SYMBOL,INSTRUMENT,OPTION_TYP from df2 where INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP ")

d_f9.to_csv('/Users/kumarsaurabh/Downloads/new_csvE.csv')
d_f99 .to_csv('/Users/kumarsaurabh/Downloads/new_csvF.csv')

df12= sqldf("select df_mf.OI,d_f9.CURR_OI,d_f9.symbol,d_f9.Instrument,(d_f9.CURR_OI-df_mf.OI) as diff "
            "from df_mf inner join d_f9  on df_mf.SYMBOL=d_f9.SYMBOL")
df12.to_csv('/Users/kumarsaurabh/Downloads/new_csvG.csv')

df13 = sqldf("select df_mOP.OI,d_f99.CURR_OI,d_f99.symbol,d_f99.Instrument,d_f99.OPTION_TYP,(d_f99.CURR_OI-df_mOP.OI) as diff "
             "from df_mOP inner join d_f99  on df_mOP.SYMBOL=d_f99.SYMBOL and df_mOP.OPTION_TYP=d_f99.OPTION_TYP")
df13.to_csv('/Users/kumarsaurabh/Downloads/new_csvH.csv')

ddf = sqldf("select df10.CURR_OI,df10.oi,df10.symbol,df10.instrument,df10.diff from df10 "
            "inner join df12 on df10.symbol = df12.symbol  "
            " where df12.diff <=0 and df10.diff >=0"
            )


ddf.to_csv('/Users/kumarsaurabh/Downloads/new_csvI.csv')

ddf1 = sqldf("select df11.CURR_OI,df11.oi,df11.symbol,df11.instrument,df11.diff,df11.OPTION_TYP from "
             "df11 inner join df13 on df11.symbol = df13.symbol and df11.OPTION_TYP=df13.OPTION_TYP "
             " where df11.diff >=0 and df13.diff <=0")


ddf1.to_csv('/Users/kumarsaurabh/Downloads/new_csvJ.csv')


countries=['united states'], n_results=1)

from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
from pandasql import sqldf
import csv
df = pd.read_csv(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/Real-Time Stock Indices Futures.csv')
#df1 = sqldf('select * from df where "Index" NOT IN ("S&P 500 VIX","Nifty 50", "Bank NIFTY")')
#df2 = sqldf('select * from df where "Index" = "Nifty 50"')
df1 = sqldf('select * from df where "Index" NOT IN ("S&P 500 VIX","DAX")')
df2 = sqldf('select * from df where "Index" = "DAX"')
#df3 = df1["Chg."].str.replace(',','')
#df4= sqldf('select avg("Chg.") as chg from df3')
df4= sqldf('select avg("Chg.") as chg from df1')
df5 = sqldf('select "Chg." as chg from df2')
df6 = sqldf('select df4.chg as world,df5.chg as nif from df4 join df5')
df6.to_csv(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/today.csv',mode='a',header=False,index=False)

# Assuming your data is stored in data1 and data2
data1 = []
data2 = []
data1 = ['-21.263214285714287', '-21.423928571428572', '-22.75392857142857', '-23.086071428571426', '-23.60964285714286', '-23.41142857142857', '-23.713214285714287', '-20.788214285714286', '-21.920357142857142', '-17.570357142857144']
data2 = ['-26.5', '-29.5', '-31.5', '-31.5', '-33.0', '-32.5', '-33.0', '-30.5', '-32.5', '-27.5']
with open(r'/Users/kumarsaurabh/Downloads/fnobavcopydata/today.csv', newline='') as csvfile:
# Create a CSV reader object
    csv_reader = csv.reader(csvfile)
next(csv_reader)
# Iterate over each row in the CSV file
for row in csv_reader:
# Assuming there are two columns in your CSV file
# Append the data from each column to the respective lists
    data1.append(row[0])
data2.append(row[1])

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
best_order = model.select_order(maxlags=1)
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



