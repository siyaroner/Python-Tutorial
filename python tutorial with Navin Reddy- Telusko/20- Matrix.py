from numpy import *
arr1= array ([
                [1,4,5,7,67,98],
                [9,3,2,43,21,80]
                    
])

print(arr1.dtype)
print(arr1.shape) # this will give (row,coloumn) 
print(arr1.size)

arr2=arr1.flatten() #this will turn multi dimensional matrix/array into single dimensional array
print(arr2,"\n")
arr3=arr2.reshape(6,2)
print(arr3,"\n")
arr3=arr2.reshape(2,2,3)  #2 dimensional 2 row 3 coloumn
print(arr3,"\n")
m=matrix(arr1)
print(m,"\n")
m=matrix("1 2 12 ; 3 4 34 ;5 6 56")
print(m,"\n")
print(diagonal(m))
print(m.max(), m.min())
m1=matrix("1 2 12 ; 3 4 34 ;5 6 56")
m2=matrix("1 3 12 ; 0 4 34 ;7 6 56")
m3=m1*m2
print("m3=",m3)


    
