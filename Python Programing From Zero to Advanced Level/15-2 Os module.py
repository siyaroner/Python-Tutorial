import datetime
import os

# print(dir(os))

# print(os.name) #i�tetim sisteminin ad�n� verir. nt windows demek
# print(os.getcwd()) # �u anki dosyan�n konumunu verir
#os.chdir("C:/Users/TOSHIBA/Desktop") # change directory
#print(os.getcwd())
# os.mkdir("newdirectory") #yeni klas�r olu�turma �st sat�rda konum de�i�tirildi�i i�in klas�r masa �st�nde olu�turulacak.
#os.rmdir("newdirectory") #dosyay� silmek i�in
#os.removedirs("newdirectory/newfolder") #alt klas�rleri silmek i�in i�i bo� olmak  kayd�yla
#os.rename("newdirectory","newfolder") # klas�r ismini de�i�tirir
#os.chdir("..") # bir �nceki klas�re ge�er
#print(os.getcwd())
#os.chdir("../..") #iki �nceki klas�re ge�er
#print(os.getcwd())
#os.makedirs("newdirectory/newfolder") #klas�r i�inde klas�r olu�turmak i�in. adres vererek de bu i�lem yap�labilir C/.. gibi
#print(os.listdir()) #klas�r i�erisindeki dosyalar�n listesini ��kar�r. ayn� i�lem verilen bir adress i�inde yap�labilir.

# for dosya in os.listdir():
#     print(dosya.endswith(".py"))
print(os.stat("newfile.txt")) #bu dosya i�in durum bilgilerini g�sterir. Olu�turulma, de�i�tirme, boyut vs. bilgilerini g�sterir

result=os.stat("newfile.txt")
print(result.st_size/1024) #byte cinsinden verilen boyut bilgisi mb �evirilir
print(result.st_ctime) #dosyan�n olu�turulma (create) tarihi saniye cinsinden. (milat kabul edilen tarihten bug�ne print(datetime.fromtimestamp(0)))
print(datetime.datetime.fromtimestamp(result.st_ctime)) # saniye cinsinden veri tarihe d�n���r�l�r.
print(datetime.datetime.fromtimestamp(result.st_atime)) # son eri�me tarihi (access)
print(datetime.datetime.fromtimestamp(result.st_mtime)) #de�i�tirme tarihi (modify)
#os.system("notepad.exe") # notepad program�n� �al��t�r�r.
#print(os.path.abspath("newfile.txt")) #dosyan�n tam konumunu verir
print(os.path.dirname("C:/Users/TOSHIBA/Desktop/Python Tutorial/BTK Akademi- Sifirdan Ileri Seviye Python Programlama/newfile.txt")) #klas�r ismi verilir.
print(os.path.dirname(os.path.abspath("newfile.txt"))) #ismi verilen dosyan�n konumu bulunur
print(os.path.exists("newfile.txt")) # b�yle bir dosya var m�? tam adres de verilebilir veya klas�r ismi olarak da arat�labilir.
print(os.path.isdir("address")) #bu bir klas�r m� true or false
print(os.path.isfile("filename")) #bu bir dosya m� true or false
print(os.path.join("C:/deneme1/deneme2")) # b�yle bir dizin olu�turur. ama bu isim de dosya olu�turulmal� yoksa sadece isimi olarak kal�r
print(os.path.split("c:/deneme1/denem2")) # 
print(os.path.splitext("newfile.txt")) #dosya ismi ile uzant�s� ayr�l�r. b�ylece isim de�i�tirme i�lemleri yap�labilir.