# var olan bir fonksiyona o fonksiyonu degitirmeden yeni ozellik ekleme için kullanilir.


def myDecorator (func):
    def wrapper():
        print("fonsiyondan onceki islem")
        func()
        print("fonksiyondan sonraki islemler")
    return wrapper

def sayHello(name):
    print("hello",name)
    
def sayGreeting(name):
    print("greting",name)

SayHello=myDecorator(sayHello)
SayHello()

greeting=myDecorator(sayGreeting)
greeting()
# # #////////////////////////////////////////////////////////////////
# # decorator with @
# print("\nrun decorator with @ ")
# def myDecorator (func):
#     def wrapper():
#         print("fonsiyondan onceki islem")
#         func()
#         print("fonksiyondan sonraki islemler")
#     return wrapper

# @myDecorator
# def sayHello():
#     print("hello")

# # sayHello()
# # # #////////////////////////////////////////////////////////////////
# # # decorator with a paramater

# print("\nrun decorator with parameter ")
# def myDecorator (func):
#     def wrapper(name):
#         print("fonsiyondan onceki islem")
#         func(name) #�a�r�lan foksiyonda parametere var ise o parametre hem buraya hem wrapper fonksiyonun i�ine de yaz�lmal�
#         print("fonksiyondan sonraki islemler")
#     return wrapper

# @myDecorator
# def sayHello(name):
#     print(f"hello {name}")

# sayHello("siyar")
# # ########################################################################

# import math
# import time


# def usalma(a,b):
#     start=time.time()
#     time.sleep(1)
#     print(math.pow(a,b))
#     finish=time.time()
#     print(f"fonksiyon {finish-start} saniye surdu")

# def faktoriyel(n):
#     start=time.time()
#     time.sleep(1)
#     print(math.factorial(n))
#     finish=time.time()
#     print(f"fonksiyon {finish-start} saniye surdu")

# usalma(2,4)
# faktoriyel(4)
# #////////////////////////////
# #i�erideki zaman hesab�n� her iki fonksiyonda da tekrar etti�imiz i�in zaman hesaplamay� ayr� bir fonksiyon olarak tan�mlay�op
# #decorator olarak her iki fonksiyon i�in �a��rabiliriz.


# print("decorator ile islem suresi hesaplama")
# def islemSuresiHesaplama(func):
#     def wrapper(*args, **kwargs):
#         start=time.time()
#         time.sleep(1)
#         func(*args, **kwargs)
#         finish=time.time()
#         print(f"{func.__name__} fonksiyonu {finish-start} saniye surdu")
#     return wrapper
# @islemSuresiHesaplama
# def usalma(a,b):
#     print(math.pow(a,b))  
# @islemSuresiHesaplama
# def faktoriyel(n):
#     print(math.factorial(n))

# usalma(2,4)
# faktoriyel(4)