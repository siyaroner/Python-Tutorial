# import datetime
from datetime import datetime, timedelta

# from datetime import date
# from datetime import time

# result=dir(datetime)
# print(result)
#////////////////////////////////////////////////////////////////
# https://www.w3schools.com/python/python_datetime.asp
simdi=datetime.now()
print(simdi)
result=simdi.year
print(result)
result=simdi.month
print(result)
result=simdi.day
print(result)
result=simdi.hour
print(result)
result=simdi.minute
print(result)
result=simdi.second
print(result)
result=datetime.ctime(simdi) #ay ve g�n ismini de verir
print(result)
result=datetime.strftime(simdi,"%Y-%m-%d %H:%M:%S")
print(result)
result=datetime.strftime(simdi,"%X")
print(result)
result=datetime.strftime(simdi,"%A")
print(result)
result=datetime.strftime(simdi,"%B")
print(result)

t="15 Mayis 2022"
gun,ay,yil=t.split()
print(gun,ay,yil)
t="15 May 2022 10:20:49"
dt=datetime.strptime(t,"%d %B %Y %H:%M:%S")
print(dt)
print(dt.year)

birthday=datetime(1995,9,21)
print(birthday)
print(datetime.fromtimestamp(0)) #ba�lang�� ald��� tarih. (bilgisayarlar i�in milat ald��� tarih)
print(datetime.timestamp(birthday)) #ba�lang�� al�nan tarihten verilen tarihe kadar ge�en s�re saniye cinsinden
print(datetime.fromtimestamp(datetime.timestamp(birthday))) #saniye cinsinden veriyi tarih formatina �evirme

now=datetime.now()
birthday=datetime(1995,9,22)
result=now-birthday #timedelta
print(result)
print("{:.2f}".format(int(str(result).split()[0])/365))
print(now+timedelta(50))


