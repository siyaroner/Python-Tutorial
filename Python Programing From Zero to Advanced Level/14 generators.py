# iteratoru kullanabilmek i�in generatora ihtiya� var. Generator bellek �zerinde sadece bir adreste bulunur. liste gibi her 
#eleman� bellek �zerine kaydederek belle�i i�gal etmez

def cube():
    for i in range(50000000): # bu kadar say�y� liste atarsak �ok ciddi yer kaplar ve yava� �al���r.
        yield i**3  #generator i�in gerekli olan ifade


generator=cube()
print(generator) #bu bir genarator ve adres ismi ��kar
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator)) # a�a��daki ifadeye gerek yok ama anla��l�r olmas� i�in...
iterator=iter(generator)
print(next(iterator)) #bu eleman sadece bu sefer �a�r�l�r ve kaydedilmedi�i i�in geri �a�r�lmaz.
print(next(iterator))
print(next(iterator))
print(next(iterator))
#////////////////////////////////////////////////////////////////
liste=(i**3 for i in range (3))
print (next(liste))
print (next(liste))
print (next(liste))
