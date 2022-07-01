import re

# print(dir(re))

txt="Python Kursu: Python Programlama Rehberiniz | 40 saat"
print(re.findall("Python",txt))
print(len(re.findall("Python",txt))) #adet bulunur
print(re.split(" ",txt))
print(re.sub(" ","-",txt)) #sub string deðiþtirme iþlemi yapýyor
print(re.search("Python",txt)) #bulduðu ilk kelimenin baþlangýç ve son karakter sýrasýný verir
print((re.search("Python",txt).span()))
print((re.search("Python",txt).start()))#baþlangýç
print((re.search("Python",txt).end())) #bitiþ karakter sýrasý
print((re.search("Python",txt).group())) #aranan kelime
print((re.search("Python",txt).string)) #arandýðý yer
print(re.findall("[abc]",txt))
print(re.findall("[^abc]",txt)) # ^ hariç tutmak için kullanýlýr
print(re.findall("[a-p]",txt))
print(re.findall("[0-9]",txt))
print(re.findall("...",txt)) #üç karakter þekilinde arar
print(re.findall("Pyt..n",txt)) #üç karakter þekilinde arar
print(re.findall("^P",txt)) # P ile baþlayan karakter var mý
print(re.findall("a$",txt)) # a ile biten karakter var mý
print(re.findall("ma*n",txt)) # a'dan sonra n geliyor mu 0 ve ya 1 adet eþleþtirir
print(re.findall("ma*an",txt)) # a'dan sonra n geliyor mu 0 ve ya 1 adet eþleþtirir
print(re.findall("ma+an",txt)) # a'dan sonra n geliyor mu en az 1





