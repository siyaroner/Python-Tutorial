
class OgranciNotKayit:
    
    def NotOkuma(self):
        with open("Ogrenci_Not_Kayit.txt","r+",encoding="utf-8") as f:
            print(f.read())
            
    def NotGirme(self):
        ad=input("öğrenci adi: ")
        soyadi=input("öğrenci sodadi ")
        not1=input("not1: ")
        not2=input("not2: ")
        not3=input("not3: ")
        with open("Ogrenci_Not_Kayit.txt","a",encoding="utf-8") as f:
            f.write(f"{ad} {soyadi}: {not1},{not2},{not3}\n")
            
    def OrtalamalariOku(self):
        with open("Ogrenci_Not_Kayit.txt","r+",encoding="utf-8") as f:
            for satir in f:
                print(self.NotHesapla(self,satir))
    
    def NotHesapla(self,*satir):
        satir=str(satir)
        satir= satir[:-1]
        liste=satir.split(":")
        ogrenciAdi=liste[0]
        notlar=liste[1].split(",")
        not1=notlar[0]
        not2=notlar[1]
        not3=notlar[2]
        ortalama=(not1+not2+not3)/3
        return ogrenciAdi+":"+ ortalama+"\n"
    
    def notlariKaydet(self):
       with open("Ogrenci_Not_Kayit.txt","r",encoding="utf-8") as f: 
           liste=[]
           for i in f:
               liste.append(self.NotHesapla(self,i))
        
       with open("Ogrenci_Not_Kayit.txt","r",encoding="utf-8") as f2: 
           for i in liste:
               f2.writ(i)

while True:
    print("Yapmak istediğini işlemin numarasini giriniz: \n")
    islem=int(input("1- Notlari Oku\n2- Not Gir\n3- Notlari Kaydet\n4- Cikis\nİslem numarasi: "))
    onk=OgranciNotKayit()
    if islem is 1:
        onk.NotOkuma()
    elif islem is 2:
        onk.NotGirme()
    elif islem is 3:
        # onk.notlariKaydet()
        pass
    elif islem is 4:
        break