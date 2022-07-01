import re

# print(dir(re))

txt="Python Kursu: Python Programlama Rehberiniz | 40 saat"
print(re.findall("Python",txt))
print(len(re.findall("Python",txt))) #adet bulunur
print(re.split(" ",txt))
print(re.sub(" ","-",txt)) #sub string de�i�tirme i�lemi yap�yor
print(re.search("Python",txt)) #buldu�u ilk kelimenin ba�lang�� ve son karakter s�ras�n� verir
print((re.search("Python",txt).span()))
print((re.search("Python",txt).start()))#ba�lang��
print((re.search("Python",txt).end())) #biti� karakter s�ras�
print((re.search("Python",txt).group())) #aranan kelime
print((re.search("Python",txt).string)) #arand��� yer
print(re.findall("[abc]",txt))
print(re.findall("[^abc]",txt)) # ^ hari� tutmak i�in kullan�l�r
print(re.findall("[a-p]",txt))
print(re.findall("[0-9]",txt))
print(re.findall("...",txt)) #�� karakter �ekilinde arar
print(re.findall("Pyt..n",txt)) #�� karakter �ekilinde arar
print(re.findall("^P",txt)) # P ile ba�layan karakter var m�
print(re.findall("a$",txt)) # a ile biten karakter var m�
print(re.findall("ma*n",txt)) # a'dan sonra n geliyor mu 0 ve ya 1 adet e�le�tirir
print(re.findall("ma*an",txt)) # a'dan sonra n geliyor mu 0 ve ya 1 adet e�le�tirir
print(re.findall("ma+an",txt)) # a'dan sonra n geliyor mu en az 1





