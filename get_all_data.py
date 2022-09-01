from sqlite3 import Timestamp
import pandas as pd
import requests
from datetime import datetime,timedelta,date
import numpy as np
from dict_coins import dict_coins

"""
Populate a BD with all dates between two dates

"""
def get_coin_history(year:int,month:int,day:int,coin:str):
   url_api = f"https://www.mercadobitcoin.net/api/{coin}/day-summary/{year}/{month}/{day}/"
   return requests.get(url_api).json()

lista = []


lista.append(get_coin_history(2017,11,23,'BTC'))

pd.DataFrame.from_records(lista).columns

get_coin_history(2015,11,23,'BTC')


requests.get("https://www.mercadobitcoin.net/api/AAVE/ticker/").json()

requests.get("https://www.mercadobitcoin.net/api/BTC/day-summary/2019/11/22/").json()

sdate = date(2019,3,22)   # start date
edate = date(2020,4,9)   # end date

for date in pd.date_range(sdate,edate-timedelta(days=1),freq='d').to_list():
    string_date_url = f"{date.year}/{date.month}/{date.day}/"
    print(string_date_url)

