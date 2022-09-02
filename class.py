from datetime import datetime,timedelta
import requests

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


                
#Alchemix_coin = coin("ALCX","Alchemix")
#Alchemix_coin.get_info_by_date()

#aragon_list = Alchemix_coin.get_all_history_info()
#df = pd.DataFrame.from_records(aragon_list)

#df.to_csv("Alchemix_coin.csv")