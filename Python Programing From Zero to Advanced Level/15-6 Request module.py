import json

import requests

#https://jsonplaceholder.typicode.com/

result=requests.get('https://jsonplaceholder.typicode.com/todos')
print(result) #<Response [200]> cevabý baþarýlý bir sonuç aldýmýzý söylüyor yani herþey yolunda
result=json.loads(result.text)
for i in result:
    if i["userId"] == 1:
        print(i["title"])
