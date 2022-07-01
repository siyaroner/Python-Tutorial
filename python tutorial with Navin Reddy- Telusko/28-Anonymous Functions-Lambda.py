f= lambda a: a*a
result=f(8)
print(result)
f= lambda a,b: a*b
result=f(8,7)
print(result) 
#////////////////////////////////////////////////////////////////
def myfunc(n):
  return lambda a : a * n+n

mydoubler = myfunc(5) #mydoubler=5*a+5

print(mydoubler(11))    # =5*11+5