import json

import requests

#https://jsonplaceholder.typicode.com/

result=requests.get('https://jsonplaceholder.typicode.com/todos')
print(result) #<Response [200]> cevab� ba�ar�l� bir sonu� ald�m�z� s�yl�yor yani her�ey yolunda
result=json.loads(result.text)
for i in result:
    if i["userId"] == 1:
        print(i["title"])
