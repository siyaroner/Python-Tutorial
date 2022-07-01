from numpy import *

arr=array([1,65,52,41])
print (arr)

# There is six ways to create an array via numpy modele
""" 1-array()
    2-linspace()
    3-logspace()
    4-arrange()
    5-zeros()
    6- ones()
"""

arr=array([1,65,52,41],int)
arr=array([1,65,52,41], float)
arr= linspace(0,40,10) #(start, stop, retstep)
print (arr)
arr=arange(0,40,10)
print (arr)
arr=logspace(0,40,10)
print (arr)
arr=zeros(5)
print (arr)
arr=ones(5)
print (arr)