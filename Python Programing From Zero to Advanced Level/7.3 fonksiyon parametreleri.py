def change(n):
    n[0]="istanbul"
    print(sehirler)

sehirler=["ankara","izmir"]
change(sehirler)

def add(*params):   ####  it qwulas to this: sum=0 for n in params sum+=n  return sum
    return sum(params)
print(add(10,30,40))

def displayuser(**parameters): # it means it will be dictionary
    for key,value in parameters.items():
        print(f"{key} is {value}")
        
displayuser(name="siyar", age=27)

def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
myfunc(1,2,3,4,5,k1="v1")


num=[1,4,5]
square=  lambda x: x**2
for i in num:
    print(square(i))
for x in num:
    print((lambda x: x**2)(x))

def sqr(num): return num**2
numbers=[4,6,2,7]
result=list(map(sqr, numbers))
print(result)
result2=list(filter(lambda x: x%2==0, result))
print(result2)
    


