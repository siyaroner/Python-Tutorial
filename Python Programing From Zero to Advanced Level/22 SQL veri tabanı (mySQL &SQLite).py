import time

import mysql.connector
from mysql.connector import Error

# print(dir(mysql.connector))
# mydb=mysql.connector.connect(
#     host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
#     user="root", 
#     password="mysql1234",
#     database="node-app" #bununla hangi veritabanına bağlanacağı seçilebilir
# )
# print(mydb)

# #workbench ide'si olmadan da mysql veritabanı üzerinde çalışma yapılabilir

# mycursor=mydb.cursor()
# # mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")

# for i in mycursor:
#     print(i)


# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# insert ile veri ekleme

def insertproduct(name,price,imageurl,description):
    connection=mysql.connector.connect(
    host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
    user="root", 
    password="mysql1234",
    database="node-app" #bununla hangi veritabanına bağlanacağı seçilebilir
    )
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,imageurl,description) VALUES (%s,%s,%s,%s)"
    values=(name,price,imageurl,description)

    cursor.execute(sql,values)
    try:
       connection.commit()
       print(f"{cursor.rowcount} tane kayıt eklendi")
       print(f"eklenen kaydın id numarası {cursor.lastrowid}")
    except connection.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print("veritabanı bağlantısı sonlandırıldı.")
def insertproducts(productlist):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    mycursor=connection.cursor()
    sql="INSERT INTO products(name,price,imageurl,description) VALUES(%s,%s,%s,%s)"
    values=productlist
    mycursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"{mycursor.rowcount} tane kayıt eklendi")
        print(f"eklenen son kaydın id numarası: {mycursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata ",err)
    finally:
        connection.close()
        print("sql bağlantısı sonlandırıldı")
def getproducts():
    connection=mysql.connector.connect(
    host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
    user="root", 
    password="mysql1234",
    database="node-app" #bununla hangi veritabanına bağlanacağı seçilebilir
    )
    mycursor=connection.cursor()
    # mycursor.execute("SELECT * FROM products Order By price Asc")
    #mycursor.execute("SELECT * FROM products Order By price Desc")
    #mycursor.execute("SELECT name,price FROM products ") #name price yerine * yapılırsa hepsini seçer
    # mycursor.execute("SELECT name,price FROM products WHERE id=1") 
    # mycursor.execute("Select name,price From products Where neme='samsung'") 
    # mycursor.execute("Select name,price From products Where neme='samsung' and price<=4000") 
    # mycursor.execute("Select name,price From products Where neme LIKE '%samsung%'") # içerisinde samsung ifadesi geçen sonuçlar gelir
    # mycursor.execute("Select name,price From products Where neme LIKE 'samsung%'") # başı samsung olan sonuçlar gelir
    # mycursor.execute("Select name,price From products Where neme LIKE '%s5'") #sonu s5 olan sonuçlar gelir
    # mycursor.execute("Select name,price From products Where neme LIKE 'samsung%' and price<=4000") # başı samsung olan sonuçlar gelir

    #result=mycursor.fetchone() #sadece bir tane kayıt getirir
    # sql="SELECT * from category"
    # sql="select * from products inner join category on category.id=products.categoryid"
    # sql="select products.name,products.price,category.name from products inner join category on category.id=products.categoryid"
    # sql="select products.name,products.price,category.name from products inner join category on category.id=products.categoryid where category.name='telefon'"
    # sql="select products.name,products.price,category.name from products inner join category on category.id=products.categoryid where products.name='samsung s6'"
    sql="select p.name,p.price,c.name from products as p inner join category as c on c.id=p.categoryid where c.name='telefon'"

    mycursor.execute(sql)
    try:
        result=mycursor.fetchall()
        for product in result:
            print(product)
            print(f"{product[0]}")
    except mysql.connector.Error as err:
        print("hata: ",err)
def getproductbyid(id):
    connection=mysql.connector.connect(
    host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
    user="root", 
    password="mysql1234",
    database="node-app" #bununla hangi veritabanına bağlanacağı seçilebilir
    )
    mycursor=connection.cursor()
    sql="SELECT * FROM products WHERE id=%s" #name price yerine * yapılırsa hepsini seçer
    params=(id,)
    mycursor.execute(sql,params)
    result=mycursor.fetchone()
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")    
def getproductinfo():
    connection=mysql.connector.connect(host="localhost",user="root", password="mysql1234",database="node-app")
    mycursor=connection.cursor()
    # sql="Select COUNT(*) from products" #toplam ürün sayısını verir
    # sql="Select COUNT(id) from products where price>2000" # fiyatı 2000'den büyük ürün sayısını verir
    # sql="select avg(price) from products" #ürün fiyatlarının ortalamasını verir
    # sql="select sum(price) from products" #ürün fiyatlarının toplamını verir
    # sql="select max(price) from products" #ürün fiyatlarının en büyüğünü verir
    # sql="select min(price) from products" #ürün fiyatlarının en küçüğünü verir
    # sqlmax="select max(price) from products" #ürün fiyatlarının en büyüğünü verir
    # mycursor.execute(sqlmax)
    # result=mycursor.fetchone()
    # for i in result:
    #     result=i
    # result=int(result)
    sql="select name,price from products where price=(select max(price) from products)"

    mycursor.execute(sql)
    result=mycursor.fetchone()
    print(result)
def updateproduct(name,price):
    connection=mysql.connector.connect(
    host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
    user="root", 
    password="mysql1234",
    database="node-app" #bununla hangi veritabanına bağlanacağı seçilebilir
    )
    mycursor=connection.cursor()
    # sql="update products Set name='Samsung S10' where id=5 or id=4"
    # sql="update products Set price=5500 where name='Samsung S10'"
    sql="update products Set price=%s where name=%s"
    values=(price,name)
    mycursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{mycursor.rowcount} tane kayıt eklendi")
        print(f"eklenen son kaydın id numarası: {mycursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata ",err)
    finally:
        connection.close()
        print("sql bağlantısı sonlandırıldı")  
def deleteproduct():
    connection=mysql.connector.connect(
    host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
    user="root", 
    password="mysql1234",
    database="node-app" #bununla hangi veritabanına bağlanacağı seçilebilir
    )
    mycursor=connection.cursor()
    # sql="update products Set name='Samsung S10' where id=5 or id=4"
    # sql="update products Set price=5500 where name='Samsung S10'"
    # sql="delete from products where id=11"
    # sql="delete from products where name like '%s%"
    sql="delete from products where id=%s"
    values=(id,)
    mycursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{mycursor.rowcount} tane kayıt silindi")
        print(f"eklenen son kaydın id numarası: {mycursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata ",err)
    finally:
        connection.close()
        print("sql bağlantısı sonlandırıldı") 
# productlist=[]
# productlist.clear()
# # while True:
    
#     name=input("ürün adı giriniz: ")
#     price=float(input("ürün fiyatı giriniz: "))
#     imageurl=input("ürün fotoğraf adını giriniz: ")
#     description=input("ürün açıklaması: ")
#     productlist.append((name,price,imageurl,description))
    
#     yanit=(input("devam etmek ister misiniz? (E/H) \n")).upper()
#     if yanit =="H":
#         insertproducts(productlist)
#         print("ürünler ekleniyor...")
#         print("%25")
#         time.sleep(2)
#         print("%50")
#         time.sleep(2)
#         print("%75")
#         time.sleep(2)
#         print("%100")
#         print("ürünler eklendi")
#         break

getproducts()        
        
           
    


