# """
# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
    
# except ZeroDivisionError:
#     print("y için 0 girilemez")
# except ValueError:
#     print("x ve y için sayisal değer girmelisiniz")

# #////////////////////////////////////////////////////////////////////////

# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
    
# except (ZeroDivisionError,ValueError):
#     print("yanliş bilgi girdiniz")
# #////////////////////////////////////////////////////////////////////////

# try:
#     x=int(input("x: "))
#     y=int(input("y: "))
#     print(x/y)
    
# except (ZeroDivisionError,ValueError) as e:
#     print("yanliş bilgi girdiniz")
#     print(e)
# #////////////////////////////////////////////////////////////////////////
# while True:
#     try:
#         x=int(input("x: "))
#         y=int(input("y: "))
#         print(x/y)
        
#     except :
#         print("yanliş bilgi girdiniz")  #doğru bilgi girilene kadar çalişir.
#         #break burada olursa bu sefer yanliş cevap girilmedikçe devam eder
#     else:
#         print("everthing is going well")
#         break
# #////////////////////////////////////////////////////////////////////////
# while True:
#     try:
#         x=int(input("x: "))
#         y=int(input("y: "))
#         print(x/y)
        
#     except Exception as ex: #alabileceğimiz hatalari genelleyip kaydedebiliriz
#         print("yanliş bilgi girdiniz",ex) 
#     else:
#         print("everthing is going well")
#         break
#     finally: # burasi helhalükarda çalişir
#         print("try & exception sonlandi")
# #////////////////////////////////////////////////////////////////////////

# x=10
# if x>5:
#     raise Exception("x 5'ten büyük değer alamaz")
# """
# #////////////////////////////////////////////////////////////////////////
def CheckPassword(psw):
    import re  # regular expression ile kontrol işlemi yapilacak
    if len(psw)<7:
        raise Exception("parola en az  7 karakterli olmalidir.")
    elif not re.search("[a-z]",psw):
        raise Exception("parola kucuk harf icermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola buyuk harf icermelidir.")
    elif not  re.search("[1-9]",psw):
        raise Exception("parola rakam icermelidir.")
    elif  not re.search("[_@$]",psw):
        raise Exception("parola ozel karakter icermelidir.")
    elif re.search("\s",psw):
        raise Exception("parola bosluk icermemelidir.")
    else:
        print("gecerli parola")
        
password="12345Aa_"

try:
    CheckPassword(password)
except Exception as ex:
        print(ex)
else:
    print("geçerli parola: try else")
finally:
       print("yetkilendirme tamamlandi.")
    
#///////////////////////////
class Person:
     
     def __init__(self,name,year):
         if len(name)>10:
             raise Exception("isim 10 karakterden fazla")
         else:
            self.name = name
p=Person("Ahmeeeeeeeeet",1996)