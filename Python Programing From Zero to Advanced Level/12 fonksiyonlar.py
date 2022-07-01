## iç içe fonksiyonlar ####
# fonksiyondan deðer döndürme
def factorial(n):
    if not isinstance(n, int):  #it's cheking for n whether it is integer or not
        raise TypeError('n must be an integer')
    
    def inner(n):
        if n is 1 or n is 0:
            return 1
        if n<0:
            raise ValueError('n must be equalt 0 or greater than 0')
        return n*inner(n-1)

    return inner(n)
try:
    print(factorial(5))
except Exception as ex:
    print(ex)
else:
    print("During calculating has not been encountered any Error")
finally:
    print("process is done")
    
#### iç içe fonksiyonlar ##
# fonksiyon döndürme

def usalma(n):
    
    def ust(u):
        return n**u
    return ust

iki=usalma(2)
print(iki(3))

#////////////////////////////////////////////////////////////////
def yetkiSorgulama(page):
    def inner(role):
        if role is "admin":
            return f"dear {role} welcome to the {page} "
        else:
            return f"sorry you can't {page} without being admin "
    return inner
user1=yetkiSorgulama("secret page")
print(user1("admin"))

#////////////////////////////////////////////////////////////////////////

def islemler(islemAdi):
    def toplama(*deger):
        toplam=0
        for i in deger:
            toplam+=i
        return toplam
    def carpma(*deger):
        carpim=1
        for i in deger:
            carpim*=i
        return carpim
    if islemAdi is "toplama":
        return toplama
    else:
        carpma
toplam=islemler("toplama")

print(toplam(3,4,3,23))
#///////////
def toplama(*sayi):
    toplam=0
    for i in sayi:
        toplam+=i
    return print(toplam)
def cikarma(*sayi):
    cikan=0
    for i in sayi:
        cikan-=i
    return print(cikan)
def carpma(*sayi):
    carpim=1
    for i in sayi:
        carpim*=i
    return print(carpim)
def bolme(*sayi):
    bolme=0
    for i in sayi:
        bolme/=i
    return print(bolme)
def islemler(t,c,cr,b,islem):
    print(islem)
    if islem == "toplama":
        t(78,78,255,36)
    elif islem is "cikarma":
        c(78,78,255,36)
    elif islem is "carpma":
        cr(78,78,255,36)
    elif islem is "bolme":
        b(78,78,255,36)
    else:
        print("gecersiz islem")
    
islemler(toplama,cikarma,carpma,bolme,"carpma")
