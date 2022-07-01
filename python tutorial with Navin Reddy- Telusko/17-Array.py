""" TypeCode    C Tyepe         Python Type         Min. Size in Bytes 
    
        'b'         signed char     int                 1
        'B'         unsigned char   int                 1
        'u'         Py_UNICODE      Unicode Character   2
        'h'         signed short    int                 2
        'H'         unsigned short  int                 2
        'i'         signed int      int                 2
        'I'         unsigned int    int                 2
        'l'         signed long     int                 4
        'L'         unsigned long   int                 4
        'f'         float           float               4
        'd'         double          double              4
    """
from array import *

vals=array ('i',[4,6,7,2,-13,9])
 
print(vals)
print(vals.buffer_info())
print(vals[0])
print(vals.reverse())
print(vals[0])
print(vals.reverse())

for i in range(len(vals)):
    print(vals[i])
# Another method  
for e in vals:
    print(e)
    
chr=array ('u',['s','i','y','a','r'])
for e in chr:
    print(e,end="")
    
newArr=array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)
    
    
    
    
    
# Array value from user
from array import *
arr= array("i",[])
n= int(input("Enter the lenght of the array: \n"))

for i in range(n):
    x=int(input("Enter the value of the array: \n"))
    arr.append(x)
    print(arr)

val= int(input("Enter the value that you wanna know its index:\n"))
for k in range(len(arr)):
    if val==arr[k]:
        print(f"index of the {arr[k]} is {k}")
        break
    k+=1