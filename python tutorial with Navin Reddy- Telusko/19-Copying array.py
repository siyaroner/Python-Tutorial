from numpy import *
arr1=array([4,2,3,8])
arr1+=1
arr2=array([5,7,9,6])
arr3= arr1+arr2
print(arr3)
arr3=(arr1,arr2)
print(arr3)
print(cos(arr1))
print(sqrt(arr3))
arr3=concatenate([arr1,arr2])
print(max(arr3))
arr4=arr1
print(id(arr1))
print(id(arr4)) # 1 and 4 arrays will have same address
# But if we use view function it won't be same anymore. View is shallow copy
arr4=arr1.view
print(id(arr1))
print(id(arr4))
arr4=arr1.copy # copy is deep copy function so when you change a valeu from one of them it won't effect another one


