import os

import pymongo
from bson.objectid import ObjectId

password=os.getenv("mongodb")
# myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient=pymongo.MongoClient(f"mongodb+srv://newuser:{password}@node-app.xhjvk.mongodb.net/test")

mydb=myclient["node-app"] 
mycollection=mydb["products"]
# print(myclient.list_database_names())
# print(mydb.list_collection_names())
# product={"name":"samsung s5","price":3000}
# rslt=mycollection.insert_one(product)
# print(type(rslt))
# print(rslt)
# print(rslt.insert_id)
# productlist=[
#     {"_id":1,"name":"samsung s6","price":3200,"description":"güzel telefon"},
#     {"_id":2,"name":"samsung s7","price":3699,"category":["telefon","elektronik"]},
#     {"_id":3,"name":"samsung s8","price":3888},
#     {"_id":4,"name":"samsung s9","price":4000},
#     {"_id":5,"name":"samsung s10","price":4550},
#     {"_id":6,"name":"samsung s20","price":5999}

# ] # id verilmese de mongodb otomatik bir id veriyor

# rslt=mycollection.insert_many(productlist)
# print(rslt.inserted_ids)

## Select Sorgusu###

# rslt=mycollection.find_one()
# print(rslt)
# for i in mycollection.find():
#     print(i)
# for i in mycollection.find({},{"_id":0,"name":1,"price":1}): #0 göstermez 1 gösterir
#     print(i)

# Filter Sorgusu###

# filter={"name":"samsung s5"}
# rslt=mycollection.find(filter)
# rslt=mycollection.find_one(filter)
# for i in rslt:
#     print(i)

# rslt= mycollection.find_one({"_id":ObjectId('629a40964a64101d9a907343')}) #id string olarak gönderilirse object id dönüştürmesi yapılamıyor bunun için bson.objectid import edilmeli
# rslt= mycollection.find({
#     "name":{
#         "$in":["samsung s5","samsung s6"]
#     }
# })
# rslt= mycollection.find({
#     "price":{
#         "$gt":3500 #gt= greater than gte=grater than or equal , eq= equal, lst=less than
        
#     }
# })
# rslt= mycollection.find({
#     "name":{
#         "$regex":"^s" #regex=regular expression, ^s= s ile başlayan isimler
        
#     }
# })
# for i in rslt:
#     print(i)

# kayıtları sıralama  ##

# rslt=mycollection.find().sort("name",-1)# -1 yapılırsa azalan şekilde sıralanır. Varsayalına ise 1 (Artan)
# rslt=mycollection.find().sort("price",1)# 0 yapılırsa azalan şekilde sıralanır. Varsayalına ise 1 (Artan)
# rslt=mycollection.find().sort([("name",1),("price",-1)])# önce name göre artan şekilde sıralar ve buna uygun olarak sonra fiyat olarak sıralar
# for i in rslt:
#     print(i)

## update sorgusu ##

# mycollection.update_one(
#     {"name":"samsung s6"},
#     {"$set":{
#         "name":"iphone 7",
#         "price":7000
#         }}
# )
# mycollection.update_many(
#     {"name":"samsung s9"},
#     {"$set":{
#         "name":"iphone 8",
#         "price":8000
#         }}
# )
# query={"name":"samsung s10"}
# newvalues={"$set":{
#         "name":"iphone X",
#         "price":10000
#         }}
# rslt=mycollection.update_many(query,newvalues)
    
# print(f"{rslt.modified_count} adet kayıt güncellendi")   
# for i in mycollection.find():
#     print(i)


############### kayıt sileme #####################
 
 
 
 
 
for i in mycollection.find():
     print (i)
     
print("*"*50)

# rslt=mycollection.delete_one({"name":"iphone 6"})
rslt=mycollection.delete_many({"name":"iphone 8"})


for i in mycollection.find():
    print(i)
    
print(f"{rslt.deleted_count} adet kayıt silindi")





