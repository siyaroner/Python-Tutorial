# iteratoru kullanabilmek için generatora ihtiyaç var. Generator bellek üzerinde sadece bir adreste bulunur. liste gibi her 
#elemaný bellek üzerine kaydederek belleði iþgal etmez

def cube():
    for i in range(50000000): # bu kadar sayýyý liste atarsak çok ciddi yer kaplar ve yavaþ çalýþýr.
        yield i**3  #generator için gerekli olan ifade


generator=cube()
print(generator) #bu bir genarator ve adres ismi çýkar
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator)) # aþaðýdaki ifadeye gerek yok ama anlaþýlýr olmasý için...
iterator=iter(generator)
print(next(iterator)) #bu eleman sadece bu sefer çaðrýlýr ve kaydedilmediði için geri çaðrýlmaz.
print(next(iterator))
print(next(iterator))
print(next(iterator))
#////////////////////////////////////////////////////////////////
liste=(i**3 for i in range (3))
print (next(liste))
print (next(liste))
print (next(liste))
