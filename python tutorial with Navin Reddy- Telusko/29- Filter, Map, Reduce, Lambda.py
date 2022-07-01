def is_even(n):  
    return n%2==0

nums= [2,3,4,5,6,7,8,0]
evens=list(filter(is_even,nums))
print(evens)

#instead of this we can use lambda because we use it for just  onces
nums= [2,3,4,5,6,7,8,0]
#Filter
evens=list(filter(lambda x: x%2==0,nums))
print(f"Evens: \n{evens}")
#Map
doubles=list(map(lambda x: x*2,evens))
print(f"Doubles: \n{doubles}")
#Reduce
from functools import reduce
sum=reduce(lambda a,b: a+b, doubles)
print(f"Sum: \n{sum}")