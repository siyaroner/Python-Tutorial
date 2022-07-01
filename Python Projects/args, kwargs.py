         #### *ARGS ####

# in normal function how many parameters you defined in function then 
#have to put that much parameter in function when you call it. Otherwise
# you'll an error.
def normal(one, two):
    print(one,two)

#normal("argument one") #it will give an error because it requires two arguments
normal("argument one", "argument two") 
#normal("argument one", "argument two","argument three")#it will give an error because it requires two arguments but given three arguments
# so to overcome this problem we can use *args

def args(*args): # we can use any name after *. so we don't only use *args also *a,*b etc. whatever you want
    for i in lst:
        print(i)
    print("\n")
lst=["one","two","three"]
args(*lst) #if you use a list for function arguments you must put * sign
#or
args("one","two","three")#it's output will be same. 
#in here like we see only by one item (*args) we can add more parameters we calling function

def args1(one,two,*args):
    print(one, two)
    for i in lst1:
        print(i)
    print("\n")
lst1=["1","2","3"]
args1("one","two",*lst1) #if you don't give three arguments you'll get an error
                    #### **KWARGS ####
#  **kwarg requires key arguments it's basically means it needs a dictionary
def kwarg(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
    print("\n")

d={"k1":"v1","k2":"v2","k3":"v3"}
kwarg(**d)   
#or
kwarg(k1="v1",k2="v2",k3="v3")

##### *arg, **kwargs####

def f(required,*arg,**kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
f("hello")
f("hello",1,2,3)
f("hello",1,2,3,key="v1",k="v2")
#////////////////////////////////////////////////////////////////
class car:
    def __init__(self,*color,**mileage):
        self.color=color
        self.mileage=mileage

class AlwaysBlueCar(car):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.color="blue"

bc=AlwaysBlueCar()
print(bc.color)    



 
