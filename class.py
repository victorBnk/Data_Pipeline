##### Imports #####

from calendar import c
from datetime import datetime,timedelta
from logging import raiseExceptions
from tkinter import E
import requests
from sqlalchemy import create_engine
import os
import pandas as pd


class coin:
    """
        Class for create crypto coins object

        Default use:
        * Create object coin
        * Get historical values from coins
        * Get currently info from coins

        API:
            Used mercadobitcoin API.
            Mercado Bitcoin is the biggest platform of cryptocurrency
            from LATAM.
            The API documentation can be accessed by the following link:
            https://www.mercadobitcoin.com.br/api-doc/


        Attributes
        ----------
        code : str
            Code crypto coin from API.
            The list of codes and the respectives names can be accessed in API documentation.

        name : str
            Crypto coin name.
        
        Methods
        -------
        get_currently_info(method:str)
            Get all coin information from API in current day

        get_info_by_date(date:datetime = datetime.now()- timedelta(days = 1))
            Get all coin information on a defined date

        get_all_history_info()
            Get all coin information from scratch date until d-1 

    """

    def __init__(self,code:str,name:str):
        self.code = code
        self.name = name
        self.__url_api = f"https://www.mercadobitcoin.net/api/{code}/"
    
    def get_currently_info(self,method:str):
        """
        Class Method that get current info from API.

        Parameters
        ----------
        method : str
            Consult method from API.Values accepted:
                - ticker : Summary of executed transactions
                - orderbook : Trade book, open buy and sell orders
                - trades : History of operations performed
        return: json
            return json with crypto informations from current day

        """

        url_consult = self.__url_api + method
        return requests.get(url_consult).json()

    def get_info_by_date(self,date:datetime = datetime.now()- timedelta(days = 1)):
        """
        Class Method that get coin info from API in passed date.

        Parameters
        ----------
        date : datetime
            Date to consult coin information
        return: json
            return json with crypto informations from passed day
        """
        url_consult = self.__url_api + f"day-summary/{date.year}/{date.month}/{date.day}"
        return requests.get(url_consult).json()
    
    def get_all_history_info(self):
        """
        Class Method that get coin info from API in passed date.

        Parameters
        ----------
        None

        return: list
            return a list of json with all dates crypto information
        """
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