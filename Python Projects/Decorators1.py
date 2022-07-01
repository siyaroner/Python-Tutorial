
def f1():
    print("Called f1")
    
f1()
print(f1) # we'll see f1 address on memory

def f2(f):
    f() # it will be f1()
f2(f1)
#////////////////////////////////////////////////////////////////////////

def f3 (func):
    def wrapper():
        print("started")
        func()
        print("finished\n")
    wrapper()
def f4():
    print("runned")
    
f3(f4)
#////////7
# if want to use return instead of wrapper()

def f3 (func):
    def wrapper():
        print("started")
        func()
        print("finished\n")
    return wrapper #instead of return we can simply call wrapper()
def f4():
    print("runned")

f3(f4) # it will give us .wrapper address so if we wanna call wrapper 
#we have to put () end of the f3(f4). Because the returning item (wrapper) is a functional function

print(f3(f4))
f3(f4)() #this will work properly
#or we can use this method also
f5=f3(f4)
f5()
# so instead of using f5=f3(f4) we can simply use decorators with @ sign

def f3 (func):
    def wrapper():
        print("started")
        func()
        print("finished\n")
    return wrapper

@f3
def f4(a):
    print("the decorators worked and runned")
    print(a)

# f4("paramater") #if we call like this we'll get an error because func() and wrapper() function don't take
#any prameter. So to fix it we can use *arg, **kwargs.

def f3 (func):
    def wrapper(*args,**kwargs):
        print("started")
        val=func(*args,**kwargs)
        print("finished (last)\n")
        return val
    return wrapper

# @f3
# def f4(a,b=5):
#     print("the decorators worked and runned, b=",b)
#     print(a)
    
# f4("paramater") 

@f3
def add(x,y):
    return x+y

print(add(8,7))



        ###### EXAMPLE ################
# example 1:
def before_after(func):
    def wrapper(*args):
        print("before")
        func(*args)
        print("after")
    return wrapper

class test:
    @before_after
    def decorated_method(self):
        print("run")

t=test()
t.decorated_method()


# example 2:

import time


def timer(func):
    def wrapper():
        before=time.time()
        func()
        print("Function took:",time.time()-before, "seconds")
    return wrapper
@timer
def run():
    time.sleep(2)

run()
        