a=10 #it is global variable
b=3
print(id(a))
def something1():
    a=25  #local variable because it's in a function
    print("inside1",a)
    
something1()
print("outside1 a",a)


def something2():
    global a #this will change the global variable a
    a=45  #local variable because it's in a function
    print("inside2 a",a)

something2()
print("outside2",a)


def something3():
    a=6
    x= globals() ["a"] #this can take all global variables
    print(id(x))

something3()
print("outside2",a)