# Program to multiply two matrices using nested loops
from numpy import *
# 3x3 matrix
x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
y= [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
rslt=[]
a=[]
m=0
# row=len(y)
# cloumn len(y[0]
for j in range(len(x)):
    for i in range(len(y[0])):
        
        for k in range(len(x[0])):
            a.append(x[j][k]*y[k][i])
            if k==2:
                
                ttl=a[m]+a[m+1]+a[m+2]
                rslt.append(ttl)
                m+=3               
l1=rslt[:4]
l2=rslt[4:8]
l3=rslt[8:12]
mtrs=[l1,l2,l3]
print(rslt)
print(mtrs)            

#Version 2
# Program to multiply two matrices using list comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

# for r in result:
print("\n")
print(result[0][0:4])
print(result[1][0:4])
print(result[2][0:4])
print("\n")
