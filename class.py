from datetime import datetime
import requests

class coin:

    def __init__(self,code:str,name:str):
        self.code = code
        self.name = name
        self.url_api = f"https://www.mercadobitcoin.net/api/{code}/"
    
    def get_currently_info(self,method:str):
        url_consult = self.url_api + method
        return requests.get(url_consult).json()

    def get_info_by_date(self,date:datetime = datetime.now()):
        url_consult = self.url_api + f"day-summary/{date.year}/{date.month}/{date.day}"
        return requests.get(url_consult).json()
    
    def get_all_history_info(self):
        pass
