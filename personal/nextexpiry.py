import pandas as pd
import glob
from pandasql import sqldf
import sqlalchemy
import datetime
from datetime import date
from datetime import timedelta

folder_path1 = '/Users/kumarsaurabh/Downloads/xx/fo23FEB2018bhav.csv'

data1 = pd.read_csv(folder_path1)

df1 = pd.DataFrame(data1)
df1['EXPIRY_DT'] = pd.to_datetime(df1['EXPIRY_DT'])
df2 = df1[df1['EXPIRY_DT'].dt.strftime('%Y-%m-%d') == "2018-04-26"]

d_f3 = sqldf("select sum(OPEN_INT) as CURR_OI , SYMBOL,INSTRUMENT,OPTION_TYP from df2 where INSTRUMENT = 'OPTSTK' group by SYMBOL,OPTION_TYP ")

d_f3 .to_csv('/Users/kumarsaurabh/Downloads/new_csv_new.csv')