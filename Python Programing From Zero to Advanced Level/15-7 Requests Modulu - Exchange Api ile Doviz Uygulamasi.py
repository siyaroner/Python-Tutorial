import json

import requests

# api_url = "https://api.exchangerate.host/latest&base="

# bozulan_doviz = input("bozduracağiniz döviz türü(ör: USD, EUR): ").upper()
# alinan_doviz = input("çevirmek istediğiniz para birimi (ör: TRY): ").upper()
# miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

# result = requests.get(api_url+bozulan_doviz)
# result = json.loads(result.text)
# print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
# print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["rates"][alinan_doviz],alinan_doviz))


### bağlıntı üzerinden hesaplama

bozulan_doviz = input("bozduracağiniz döviz türü(ör: USD, EUR): ").upper()
alinan_doviz = input("çevirmek istediğiniz para birimi (ör: TRY): ").upper()
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))
api_url = f"https://api.exchangerate.host/latest?amount={miktar}&base={bozulan_doviz}" #miktar ile bozulan döviz yer değiştirebilir.

result = requests.get(api_url)
result = json.loads(result.text)
print("{} {} = {:.2f} {}".format(miktar, bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))