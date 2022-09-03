##### Imports #####

from calendar import c
from datetime import datetime,timedelta
from logging import raiseExceptions
from tkinter import E
import requests
from sqlalchemy import create_engine
import os



class coin:

    def __init__(self,code:str,name:str):
        self.code = code
        self.name = name
        self.url_api = f"https://www.mercadobitcoin.net/api/{code}/"
    
    def get_currently_info(self,method:str):
        url_consult = self.url_api + method
        return requests.get(url_consult).json()

    def get_info_by_date(self,date:datetime = datetime.now()- timedelta(days = 1)):
        url_consult = self.url_api + f"day-summary/{date.year}/{date.month}/{date.day}"
        return requests.get(url_consult).json()
    
    def get_all_history_info(self):
        try:
            list = []
            date_init = datetime.now()- timedelta(days = 1)
            while True:
                try:
                    list.append(self.get_info_by_date(date_init))
                    print(self.get_info_by_date(date_init))
                    date_init = date_init - timedelta(days=1)
                except:
                    print("Done")
                    return list
        except:
            print("Error! Something went wrong when getting history info.")



class connection_bd:

    def __init__(self,user:str,password:str,host:str,database_name:str):
        self.user = user
        self.password = password
        self.host = host
        self.database_name = database_name

    def create_engine_bd(self):
        try:
            engine =  create_engine(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.database_name}')
            print("Engine created!")
            try:
                engine.connect()
                print("Engine successfully connected!")
                return engine
            except:
                print("Error! Engine could not connect with Data Base.")
        except:
            print("Error! Engine could not be created")




if __name__ == '__main__':
    db_user = os.environ.get('DB_USER')
    db_psw = os.environ.get('DB_PSW')
    conn = connection_bd(db_user,db_psw,'localhost','padrao')
    engine = conn.create_engine_bd()