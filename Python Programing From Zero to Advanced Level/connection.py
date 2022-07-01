import mysql.connector

connection=mysql.connector.connect(
host="localhost",  #server hizmeti alınırsa bunun yerine server hizmeti alınan yerin verdiği ip adresi girilecek.
user="root", 
password="mysql1234",
database="schooldb" #bununla hangi veritabanına bağlanacağı seçilebilir
)