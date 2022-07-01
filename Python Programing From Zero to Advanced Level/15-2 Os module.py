import datetime
import os

# print(dir(os))

# print(os.name) #iþtetim sisteminin adýný verir. nt windows demek
# print(os.getcwd()) # þu anki dosyanýn konumunu verir
#os.chdir("C:/Users/TOSHIBA/Desktop") # change directory
#print(os.getcwd())
# os.mkdir("newdirectory") #yeni klasör oluþturma üst satýrda konum deðiþtirildiði için klasör masa üstünde oluþturulacak.
#os.rmdir("newdirectory") #dosyayý silmek için
#os.removedirs("newdirectory/newfolder") #alt klasörleri silmek için içi boþ olmak  kaydýyla
#os.rename("newdirectory","newfolder") # klasör ismini deðiþtirir
#os.chdir("..") # bir önceki klasöre geçer
#print(os.getcwd())
#os.chdir("../..") #iki önceki klasöre geçer
#print(os.getcwd())
#os.makedirs("newdirectory/newfolder") #klasör içinde klasör oluþturmak için. adres vererek de bu iþlem yapýlabilir C/.. gibi
#print(os.listdir()) #klasör içerisindeki dosyalarýn listesini çýkarýr. ayný iþlem verilen bir adress içinde yapýlabilir.

# for dosya in os.listdir():
#     print(dosya.endswith(".py"))
print(os.stat("newfile.txt")) #bu dosya için durum bilgilerini gösterir. Oluþturulma, deðiþtirme, boyut vs. bilgilerini gösterir

result=os.stat("newfile.txt")
print(result.st_size/1024) #byte cinsinden verilen boyut bilgisi mb çevirilir
print(result.st_ctime) #dosyanýn oluþturulma (create) tarihi saniye cinsinden. (milat kabul edilen tarihten bugüne print(datetime.fromtimestamp(0)))
print(datetime.datetime.fromtimestamp(result.st_ctime)) # saniye cinsinden veri tarihe dönüþürülür.
print(datetime.datetime.fromtimestamp(result.st_atime)) # son eriþme tarihi (access)
print(datetime.datetime.fromtimestamp(result.st_mtime)) #deðiþtirme tarihi (modify)
#os.system("notepad.exe") # notepad programýný çalýþtýrýr.
#print(os.path.abspath("newfile.txt")) #dosyanýn tam konumunu verir
print(os.path.dirname("C:/Users/TOSHIBA/Desktop/Python Tutorial/BTK Akademi- Sifirdan Ileri Seviye Python Programlama/newfile.txt")) #klasör ismi verilir.
print(os.path.dirname(os.path.abspath("newfile.txt"))) #ismi verilen dosyanýn konumu bulunur
print(os.path.exists("newfile.txt")) # böyle bir dosya var mý? tam adres de verilebilir veya klasör ismi olarak da aratýlabilir.
print(os.path.isdir("address")) #bu bir klasör mü true or false
print(os.path.isfile("filename")) #bu bir dosya mý true or false
print(os.path.join("C:/deneme1/deneme2")) # böyle bir dizin oluþturur. ama bu isim de dosya oluþturulmalý yoksa sadece isimi olarak kalýr
print(os.path.split("c:/deneme1/denem2")) # 
print(os.path.splitext("newfile.txt")) #dosya ismi ile uzantýsý ayrýlýr. böylece isim deðiþtirme iþlemleri yapýlabilir.