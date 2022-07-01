import json
import os

import requests

#from dotenv import load_dotenv

#load_dotenv()
api_key=os.getenv("API_KEY")
print("lutfen para birimlerini giriniz ornek: TRY, USD, EUR")
nereden=input("cevrilen para birmini giriniz: ").upper()
nereye=input("hedef para birmini giriniz: ").upper()
miktar=input("lutfen cevirmek istediginiz miktari giriniz: ")
url = f"https://api.apilayer.com/exchangerates_data/convert?to={nereye}&from={nereden}&amount={miktar}" #&date=2017-06-17 geçmiþi görmek istersen baðlantýnýn sonuna ekle
payload = {}
headers= {
  "apikey": api_key
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
