import sqlite3

import numpy as np
import pandas as pd
from numpy.random import randn

# from array import *

############### PANDAS SERIES ####################
# pandas_series=pd.Series()
# print(pandas_series) # veri tipi series olarak çıkar
# nums=[39,45,65,67,21]
# letters=["a", "b", "c", "d", "e",]
# dic={"a":1,"b":2,"c":3,"d":4}
# randnum=np.random.randint(10,200,10)
# pandas_series=pd.Series(nums)
# print(pandas_series) 
# print(pd.Series(letters))
# print(pd.Series(4))
# print(pd.Series(4,[0,1,2,3]))
# print(pd.Series(nums,letters))
# print(pd.Series(dic))
# print(pd.Series(dic)[d])
# print(pd.Series(randnum))
# print(pd.Series(randnum)[0])
# print(pd.Series(randnum)[-1])
# print(pd.Series(randnum)[:2])
# print(pd.Series(randnum)[-2:])
# print(pd.Series(randnum)[12]) # olmayan veri için nan (not a number) bilgisi verir hata vermez
# print(pd.Series(randnum).ndim) #dimension 
# print(pd.Series(randnum).dtype)
# print(pd.Series(randnum).shape) 
# print(pd.Series(randnum).sum)
# print(pd.Series(randnum).max())
# print(pd.Series(randnum).min())
# print(pd.Series(randnum)+pd.Series(randnum))
# print(np.sqrt(pd.Series(randnum)))
# print((pd.Series(randnum))>=20)
# print((pd.Series(randnum))%2==0)
# print(pd.Series((pd.Series(randnum))%2==0))
# opel2018=pd.Series([20,60,40,30],["astra","corsa","mokka","insignia"])
# opel2019=pd.Series([70,80,46,40],["astra","corsa","Grandland","insignia"]) #grandland ve mokka eşleşmediği için toplamlarında nan döner
# print(opel2018,"\n",opel2019)
# print(opel2018+opel2019)

########### PANDAS DATAFRAME ##############################
# Dataframe'ler data serilerinin birleşiminden oluşur.
# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])

# data=dict(apples=s1,oranges=s2)
# df=pd.DataFrame(data)
# print(df)
# df=pd.DataFrame([0,1,2,34,]) #sütun ve satır ismi belirtilmediği için satır ve kolon 0'dan başlar
# lst=[["ahmet",50],["ali",60],["çinar",80]]
# dic={"name":["ahmet","ali","çinar"],"grade":[50,40,60]}
# dic_lst=[
#          {"name":"ahmet","grade":50},
#          {"name":"ali","grade":70},
#          {"name":"çinar","grade":40}
#         ]
# # df=pd.DataFrame(lst,columns=["name","grade"],index=[1,2,3],dtype=float) #eğer columns index ismileri belirtilmeyecekse sıralama [seri,index,sütun] şeklinde olmalı.
# # df=pd.DataFrame(dic,index=[1,2,3],dtype=float) 
# df=pd.DataFrame(dic_lst,index=[1,2,3],dtype=float) 

# print(df)

####### FARKLI DOSYA TİPLERİNDEN VERİ OKUMA #######################

# df=pd.read_csv("csv files/saudiarabia_carsprices.csv")
# print(df)
#df=pd.read_json("person.json")
# df=pd.read_excel("csv files/person.xlsx")
# connection=sqlite3.connect("")
# df=pd.read_sql_query("db files/sample.db",connection)
# print(df)


####### DataFrame ile Satır Sütun Seçimi ##########


# df=pd.DataFrame(randn(4,4),index=["a","b","c","d"],columns=["1","2","3","4"])
# df2 = pd.DataFrame({'1': [21, 25, 26,7],
#                     '2': [7, 7, 13,4],
#                     '3': [11, 3, 3,6],
#                     '4': [14, 83, 36,7]
#                     })
# rslt=df
# print(df.describe)
# rslt=df["1"]
# print(type(df["1"]))
# print(rslt)
# print(df[["1","2"]])
# print(df.loc["a"])  # a satırına denk gelen kolonları yazdırır.
# print(df.loc["a","1"]) # a satırı 1 sütunu
# print(df.loc[:,"1"]) # 1 sütunu ve tüm satırlar
# print(df.loc[:,["1","2"]]) # 1 ve 2 sütunu ve tüm satırlar
# print(df.loc[:,"1":"3"]) # 1 ve 3 dahil 1-3 arasındaki sütunlar
# print(df.loc[:,:"3"]) # 1 ve 3 dahil 1-3 arasındaki sütunlar
# # print(df.loc["a":"c",:"3"])
# print(df.iloc[2]) # 2. indeksteki satıra karşılık gelen tüm kolonlar
# print(df.iloc[2,1:3]) # 2. indeksteki satıra ve 1-3 arasındaki tüm kolonlar
# print(df.loc["a","1"]) # satır kolon isimleri ile hücre bazında seçin 1. satır 1. sütun
# print(df.iloc[0,0]) #indeks numarası ile seçin
# print(df.loc[["a","b"],["1","2"]])
# df["5"]=pd.Series(randn(4),["a","b","c","d"]) # yeni bir sütun ekleme
# df["5"]=df["1"]+df["3"]
# df.loc[len(df.index)]=randn(4).tolist() #yeni bir satır ekleme
# df = df.append(df2, ignore_index = True) # çoklu satır/yeni dataframe ekleme
# print(df)
# print(df.drop("5",axis=1)) # axis=0 satır(x) axis= sütun(y)
# print(df.drop("5",axis=1),inplace= True) # inplace=True olursa var olan df üzerinde değişiklik olur
# print(df)

########### PANDAS DATAFRAME İLE FİLTRELEME ##############################

# data=np.random.randint(10,100,75).reshape(15,5)
# df=pd.DataFrame(data,columns=["column1","column2","column3","column4","column5"])
# rslt=df
# print(rslt.columns) #sütun isimlerini almak için
# print(df.head()) #ilk 5 kaydı getirir
# # print(df)
# print(df.head(10)) #ilk 10 kaydı getirir
# print(df.tail(10)) #son 10 kaydı getirir
# print(df["column1"].head()) # column1'in ilk 5 kaydı getirir
# print(df.column1.head()) # column1'in ilk 5 kaydı getirir
# print(df[["column1","column2"]].head()) # column1 ve 2'in ilk 5 kaydı getirir
# print(df.loc[:,"column1":"column3"].head()) # column1 ve 3 arasındaki ilk 5 kaydı getirir
# print(df[5:15][["column1","column2"]].head()) # 5-15'in column1 ve 2'in ilk 5 kaydı getirir
# print(df>50) #büyükse True değilse False verir
# print(df[df>50]) # 50 büyüklerin değerlerini verir
# print(df[df[df>50]%2==0]) # 50 büyük ve çift sayıların değerlerini verir
# print(df["column1"][df["column1"]>50]%2==0) # column1 için 50 büyük ve çift sayıların değerlerini verir
# print(df[["column1","column2"]][(df["column1"]>50) & (df["column1"]<90)]) # 
#   qeury methodu #
# print(df.query("column1>50 | column1 %2==0")["column3"])


################### IMDB VERİ ANALAZİ #####################

# data=pd.read_csv("csv files/imdb_top250.csv")
# print(data.columns)
# data.drop(["certificate","ranking of movie","DETAIL ABOUT MOVIE","DIRECTOR ","ACTOR 1","ACTOR 2","ACTOR 3","ACTOR 4"],axis=1,inplace=True)
# print(pd.DataFrame(data).describe)
# # print(data.head())
# # print(data[["movie name ","RATING"]][5:20].head())
# #print(data[["movie name ","RATING"]][data["RATING"]>8].head(50))
# # print(data["movie name "][data[(["Year"]>2014) & (["Year"]<2015)]])
# data["Year"]=data["Year"].str.strip("-( I)")
# year=[]
# year=list(data["Year"])
# for i in range(len(year)):
#         year[i]=int(year[i])
# data["Year"]=year
# # print(type(year[0]))
# # for i in range(len(data["Year"])):
# # data["Year"]=int(year)
# # print(year)        
# # print(data["movie name "][(data["Year"]>2014)&(data["Year"]<2017)])
# print(data[(data["RATING"]>8.5)&(data["RATING"]<9)|(data["votes"]>500000)])

################### DATAFRAME GROUPBY #####################

# personeller={
#                 "çalişan":["ahmet yilmaz","can ertürk","hasan korkmaz","cenk saymaz","ali bilge","riza ertürk","mustafa can"],
#                 "departman":["ik","it","mh","ik","it","mh","ik"],
#                 "yaş":[30,25,45,50,23,34,42],
#                 "semt":["kadiköy","tuzla","maltepe","tuzla","maltpe","tuzla","kadiköy"],
#                 "maaş":[5000,3000,4000,3500,2500,2750,4500]
#             }

# df=pd.DataFrame(personeller)
# rslt=df["maaş"].sum()
# rslt=df.groupby("departman").groups
# rslt=df.groupby(["departman","semt"]).groups
# semtler=df.groupby("semt")
# for name,group in df.groupby("semt"):
#         print(name)
#         print(group)
# # for name,group in df.groupby("departman"):
# #         print(name)
# #         print(group)
# # rslt=df.groupby("semt").get_group("kadiköy")
# # rslt=df.groupby("departman").get_group("it")
# rslt=df.groupby("departman").get_group("it")["maaş"].sum()
# rslt=df.groupby("departman").get_group("ik")["maaş"].mean()
# rslt=df.groupby("departman").get_group("mh")["yaş"].max()
# rslt=df[["çalişan","departman","maaş"]].max()
# rslt=df.groupby("departman")["maaş"].mean()
# rslt=df.groupby("departman")["yaş"].mean()
# rslt=df.groupby("departman").get_group("it")["yaş"].max()
# rslt=df.groupby("departman")["çalişan","departman","maaş"].max().max()
# rslt=df.groupby("departman")["maaş"].max()["it"]
# rslt=df.groupby("departman").agg(np.mean) #aggregation fonksiyonu ile sayı olan değerler üzerinden hesap yapılabilir.
# rslt=df.groupby("departman").get_group("it")["maaş"].agg([np.max,np.min,np.mean,np.sum])
# rslt=df.groupby("departman")["maaş"].agg([np.max,np.min,np.mean,np.sum]).loc["mh"]


# print(rslt)

################### PANDAS İLE KAYIP VE BOZUK VERİ ANALİZİ #####################

# data=np.random.randint(10,100,15).reshape(5,3)
# df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["c1","c2","c3"])
# df=df.reindex(["a","b","c","d","e","f","g","h"])
# rslt=df
# rslt=df.drop("c1",axis=1)
# rslt=df.drop(["c1","c2"],axis=1)
# rslt=df.drop("b",axis=0) #axis=0 yazılmayabilir çünkü varsayılan axis 0
# rslt=df.drop(["b","d"])
# rslt=df.isnull()
# rslt=df.notnull()
# rslt=df["c1"].isnull().sum()
# rslt=df[df["c1"].isnull()]["c1"]
# rslt=df[df["c1"].notnull()]["c1"]
# rslt=df.dropna() #en az bir elemanı nan olan satırları siler
# rslt=df.dropna(axis=1) #en az bir elemanı nan olan sütunları siler
# rslt=df.dropna(how="any") #en az bir elemanı nan olan satırları siler
# rslt=df.dropna(how="all") #tamamı nan olan satırları siler
# rslt=df.dropna(subset=["c1","c2"],how="all") #c1 ve c2 kolonlarında tamamı nan olan satırları siler
# rslt=df.dropna(thresh=6,axis=1,how="any") # 2 tane istenilen değer varsa kayıtları silme
# rslt=df.fillna(value=1) #nan olan yerler istenlen herhangi bir değer veya string ile doldurulabilir.
# rslt=(df.sum()).sum() 
# rslt=df.size
# rslt=sum((df.isnull().sum()))
# toplam_verili_hucreler=df.size-(df.isnull().sum()).sum()
# print(rslt)
# print(toplam_verili_hucreler)

################### PANDAS İLE STRING FONKSİYONLARININ KULLANIMI #####################

# data=pd.read_csv("csv files/generationstatemon.csv")
# data.drop(data.iloc[:,7:],axis=1,inplace=True)
# data["GENERATION (MWh)"]=data["GENERATION (Megawatthours)"]
# data.drop(["TYPE OF PRODUCER","index","GENERATION (Megawatthours)"],axis=1,inplace=True)
# data.dropna(how="any",inplace=True)
# data["ENERGY SOURCE"]=data["ENERGY SOURCE"].str.upper()
# data["ENERGY SOURCE"]=data["ENERGY SOURCE"].str.lower()
# data=data[(data["YEAR"]<=2001)&(data["MONTH"]==1)]
# data["index"]=data["ENERGY SOURCE"].str.find("a")
# data["index"]=data["ENERGY SOURCE"].str.contains("coal")
# rslt=data["ENERGY SOURCE"].str.replace(" ","-")
# rslt=data["ENERGY SOURCE"].loc[data["ENERGY SOURCE"].str.split().str.len()]
# rslt=data["ENERGY SOURCE"].loc[data["ENERGY SOURCE"].str.split().str.len()].str.split

# print(rslt.head(50))
# # print(data[data[]])

################### PANDAS İLE JOIN VE MERGE #####################


# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName': ["Yilmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)
# result = pd.merge(df_customers,df_orders,how="inner") #kesişim
# result = pd.merge(df_customers,df_orders,how="left") # müşteri ama siparişi yok
# # result = pd.merge(df_customers,df_orders,how="right") # sipariş var ama müşteri kaydı yok/silinmiş.
# result = pd.merge(df_customers,df_orders,how="outer") # tüm kayıtlar getirilir.
# print(result)
# # # dataframe birleştirme (concat) ###
# customersA = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName': ["Yilmaz","Korkmaz","Çelik","Toprak"]
# }

# customersB = {
#     'CustomerId': [4,5,6,7],
#     'FirstName': ["Yağmur","Çinar","Cengiz","Can"],
#     'LastName': ["Bilge","Turan","Yilmaz","Turan"]
# }

# df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
# df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

# result = pd.concat([df_customersA,df_customersB]) # satır bazında dataframe birleştirme
# result = pd.concat([df_customersA,df_customersB],axis=1) # sütun bazında sütunları birleştirme.


# print(result)


################# PANDAS İLE DATAFRAME METOTLARI ########################

# data = {
#     "c1": [1,2,3,4,5],
#     "c2": [10,20,13,20,25],
#     "c3": ["abc","bcaa","ade","cb","dea"]
# }

# df=pd.DataFrame(data)

# def karele(x):
#     return x**2
# rslt=df
# # rslt=df["c2"].unique() # tekrar eden elemanları bir defa gösterir.
# # rslt=df["c2"].nunique() # toplam eleman sayısı (tekrar edenleri bir sayar)
# # rslt=df["c2"].value_counts() #bir elemandan kaç tane olduğunun sayısını listeler
# # rslt=df["c2"].apply(karele) # fonksiyonlar obje olarak çağrılır
# # rslt=df["c2"].apply(lambda x: x**2)
# rslt["len(c3)"]=df["c3"].apply(len)
# rslt=df.columns
# rslt=len(df.columns)
# rslt=df.index
# rslt=len(df.index)
# rslt=df.info
# rslt=df.sort_values("c2")
# rslt=df.sort_values("c2",ascending=False) # sıralama varsayılan True ayni artandan azalana. false olursa azalandan artana olur. 

# print(rslt)

# data = {
#     "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
#     "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
#     "Gelir": [20,30,15,14,32,42,12,36,52]
# }

# df=pd.DataFrame(data)
# df=df.pivot_table(index="Ay", columns="Kategori",values="Gelir")


# print(df)






