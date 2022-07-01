## DUCK TYPING
from ast import Div


class vsc:
    
    def execute(self):
        print("compiling...")
        print("Runnning...\n")

class myeditor:
    
    def execute(self):
        print("Preparing...")
        print("compiling...")
        print("Executing...")
        print("Running...")

class program:
    
    def code(self,ide):
        ide.execute() # there is two differrent class and they have same method (execute) so this is duck typing

ide=vsc()   

prog1=program()
prog1.code(ide)
ide=myeditor()    
prog1.code(ide)

## OPERATOR OVERLOADING
a=-4
b=10
print(a+b)
print(int.__add__(a,b))
print(abs(a))
class student:
    
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __mul__(self,other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        s4=student(m1,m2)
        return s4
    
    def __truediv__(self,other):
        m1=self.m1/other.m1
        m2=self.m2/other.m2
        s5=student(m1,m2)
        return s5
    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        s6=student(m1,m2)
        return s6
    def __gt__(self,other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1>r2: return True
        else: return False
    def __str__(self): # by __str__ (MAGIC METHOD) it will return m1,m2 value not their address
        return "{} {}".format(self.m1,self.m2)
    
    
s1=student(58,69)
s2=student(60,65)
s3=s1+s2
print(s1,"\n",end="{}\n".format(s2),)
if s1>s2: 
    print("s1 greater than s2")
else: 
    print("s2 greater than s1")
print(s3.m1,s3.m2)
s4=s1*s2
print(s4.m1,s4.m2)
s5=s1/s2
print("{:.2f} {:.2f}".format(s5.m1,s5.m2))
s6=s1-s2
print(s6.m1,s6.m2)

## METHOD OVERLOADING
# When we calling + operator actually we are calling __add__ method. But + operator takes different type of arguments
#different parameters. So overloading method; you have same method but you take different arguments or types or number of arguments.
# but Python doesn't support this.

## METHOD OVERRIDING
# We can appy this by inheritance class

class student:
    
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def sum(self,a=None,b=None,c=None):
        s=0
        if a is not None and b is not None and c is not None:            
            s=a+b+c
        elif a is not None and b is not None:
            s=a+b
        else:
            s=a
        return s

s1=student(58,69)
print(s1.sum(5,6))

class a:
    
    def show(self):
        print("in a show")
    
class b(a):
    #pass
    def show(self):
        print("in b show")

a1=b()
a1.show()

