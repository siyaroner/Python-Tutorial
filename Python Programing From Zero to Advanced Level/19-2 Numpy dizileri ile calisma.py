# import numpy as np

# lst=[1,2,3,4,5,6,7,8,9]
# # print(np.array(lst))
# # print(np.arange(1,10)) #1-10 arasında bir dizi oluşturur
# # print(np.arange(1,50,4)) #1-50 arasında 4'er artarak dizi oluşturur
# # print(np.zeros(10)) #10 tane sıfıf #floaat
# # print(np.ones(20)) #flaot
# # print(np.linspace(0,100,5)) #0-100 arasını 5 eşit parçaya bölme #floaat
# #print(np.random.randint(0-10)) #0-10 (10 hariç) arasında rastgele bir sayı oluşturur.
# #print(np.random.randint(20))# 0 başlangıç kabul edilir 20'ye kadar
# #print(np.random.randint(1,20,3)) #üçerli olarak rasgele sayı üretir belirtilen aralıkta
# #print(np.random.rand(5)) #0-1 arasında 5 adet sayı üretilir.
# #print(np.random.randn(5)) #0-1 arasında 5 adet sayı üretilir. randn olduğu için negatifler de dahil edilir.add()
# #print((np.arange(50)).reshape(5,10)) #0-50 arası bir dizi oluşturup 5x10'luk matrise çevirir.
# #print(((np.arange(50)).reshape(5,10)).sum(axis=1)) #satırların kendi için toplamını veririr
# #print(((np.arange(50)).reshape(5,10)).sum(axis=0)) #ssütunların kendi için toplamını veririr
# #print((np.random.randint(0,100,10)).max())#0-100 arası 10 tane sayı oluşturup en büyüğünü bulur
# #print((np.random.randint(0,100,10)).min())#0-100 arası 10 tane sayı oluşturup en küçüğünü bulur
# #print((np.random.randint(0,100,10)).mean())#0-100 arası 10 tane sayı oluşturup ortalamalarını bulur
# #print((np.random.randint(0,100,10)).argmax()) #en büyük sayının index numarasını çevirir.
# #print((np.random.randint(0,100,10)).argmin()) #en küçük sayının index numarasını çevirir.

# ### dizilerin indekslenmesi### 

# # lst=[]
# # arr=np.array(lst)

# # for i in range(10):
# #     arr=np.append(arr,np.random.randint(0,100))
   
# # # arr=np.array(lst)
# # # print(arr)
# # arr=np.append(arr,12)



# lst=[]
# # arr1=np.array(lst1)

# while True:
#     lst1=[]
#     while True:
#         lst1.append(np.random.randint(0,100))
#         if len(lst1)>5:
#             break
#     lst.append(lst1)
#     del lst1
#     if len(lst)>2:
#         break
# arr=np.array(lst)
# # print(arr)
# #or
# #arr=np.random.randint(0-100,15).reshape(5,2)

# # print(arr[2])
# # print(arr[-1])
# # print(arr[:4])
# # print(arr[:3])
# # print(arr[1:])
# # print(arr[::])
# # print(arr[:,0]) #0 indeksindeki tüm elemanlar
# # print(arr[:,0:2]) #0-2 indeksindeki tüm elemanlar (2 hariç)
# # print(arr[::-1]) #ters yönden 1'er 1'er
# # print(arr[-1,:]) #sol satırdaki tüm elemenalar
# # print(arr[:2,:1]) #2'ye kadar tüm satırlar 1'e kadar tüm kolonlar

# arr2=arr #shallow copy yani ikiside aynı adresi gösterir ikisinden birinde olacak değişiklik diğerini de etkiler
# arr2=arr.copy() #deep copy ikisi farklı adresleri gösterir. Değişiklikler birbirini etkilemez
x=5
x**=3
print(x)


