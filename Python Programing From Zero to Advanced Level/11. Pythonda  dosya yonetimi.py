# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open ("dosya_adi","erisme_modu")
#dosyaya erişme modu dosyayı hangi amaçla açtığımızı belirtir.

# "w" : (write) yazma modu. Dosya mevcut değilse oluşturur. Mevcutsa içeriği herşeyi siler istenileni yazar.

""" python klsörünün bulunduğu yerde açmak için"""
file=open("newfile.txt","w",encoding="utf-8")
file.write("heyyy\n")
file.close()
    # print(file)
""" istenilen konumda dosya açmak için"""
    # file=open("C:/Users/TOSHIBA/Desktop/newfile.txt","w",encoding="utf-8")
    # file.close()
    # print(file)
# "a" : (append) ekleme. Dosya mevcut değilse oluşturur Mevcutsa içeriği silmez istenileni son kalan yerden yazar.
file=open("newfile.txt","a",encoding="utf-8")
file.write("how are you\n")
file.close()
# "x" : (create) olusturma. Yeni dosya oluştururur zaten varsa hata verir
    #file2=open("newfile2.txt","x",encoding="utf-8")
# "r" : (read) okuma. Varsıyan dosya konumda yoksa hata verir
    #file=open("newfile.txt","r",encoding="utf-8")
# 1. okuma yöntemi -for ile
    # for i in file:
    #     print(i)
# 2. yöntemi -read()
    # content=file.read()
    # print("içerik 1")
    # print(content)
    # content2=file.read()
    # print("içerik 2")
    # print(content2) #burada bir içerik çıkmaz çünkü imleç son noktada olduğu için sonrasında okunacak birşey kalmaz. bunu önlemek için okumadan sonra file.close() yapılmalı.add()
    # content=file.read(5) #5 byte yani 5 karakter okur
    # print(content)
    # content=file.read(4) #4 byte yani 4 karakter okur
    # print(content)
    # file.close()
# 3. yöntem readline()
    # content=file.readline() #her çalıştırıldığında 1 satır okur
    # print(content,end="")
    # content=file.readline()
    # print(content)
    # file.close()
# 4. yöntem readlines()
    # lst=file.readlines() #içeriği bir listeye atar
    # print(lst)
    # print(lst[0])
    # print(lst[1])
    # file.close()

#### with fonksiyonu ########

# with open("newfile.txt","r",encoding="utf-8") as f:
#     content=file.read()
#     print(content)
#     f.seek(10) #imleci girelen konuma gönderir.
#     print(f.tell()) #imlecin son bulunduğu noktayı verir yani kaçıncı byte/karakterde olduğunu

#### with fonksiyonu ve r+ metodu ########

with open("newfile.txt","r+",encoding="utf-8") as f:  #r+ hem dosyayı okuma hem yazma modunda açar. yazarken son kaldığı yerden yazar içeriği silmez
    #f.seek()
    f.write("r+ metoduyla yazma")
    f.close()
with open("newfile.txt","r+",encoding="utf-8") as f:  #r+ hem dosyayı okuma hem yazma modunda açar. yazarken son kaldığı yerden yazar içeriği silmez
    
    print(f.read())
    f.close()
    




