# # 
# liste=[1,2,3,4,5,6,7,8,9]

# for i in liste: print(i)  #liste iterable olduðu için for kullanýlabiliyor

# print(dir(liste)) #liste içerisinde ierator fonksiyonu var

# #//////////////////
# liste=[1,2,3,4,5,6,7,8,9]
# iterator=iter(liste)
# print(next(iterator))
# print(next(iterator))# print ile yazdýkça bir sonraki elemaný yazar eleman sayýsý bittiðinde stopiteration hatasý verir.

# # for fonksiyonun çalýþma mantýðý =>
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
#////////////////////////////////////////////////////////////////

class iterator():
    
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start +=1
            return x
        else:
            raise StopIteration


list= iterator(1,9)
myiter=iter(list)
print(next(myiter))
print(next(myiter))
#... or
for x in list:
    print(x)