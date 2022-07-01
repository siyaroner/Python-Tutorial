class Computer: # we can accept class as an design or a brand(like samsung)
    def config(self): # functions (methods) are behavior and values are attributes
        print("i5","16gb ram","1tb ssd") #Self is the object we're passing. For this example they are comp1 and comp2
        
comp1=Computer() #comp1 is an object now.
comp2=Computer() #comp1 is an object now.
Computer.config(comp1) # it's equal to comp1.config()
Computer.config(comp2)
comp1.config()         
comp2.config()         
#////////////////////////////////////////////////////////////////
# __init__ method
class Computer: # we can accept class as an design or a brand(like samsung)
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        
    def config(self): # functions (methods) are behavior and values are attributes
        print("Config is ",self.cpu,self.ram) #Self is the object we're passing. For this example they are comp1 and comp2.
        #we can name self something else we want
        
comp1=Computer("i5",16) #comp1 is an object now.
comp2=Computer("Intel-7,",8) #comp1 is an object now.

comp1.config()         
comp2.config()   
#////////////////////////////////////////////////////

class human:
    def __init__(self):
        self.name="siyar"
        self.age=27
    def update(ageself):
        ageself.age=28
    def compare(self,anotherone):
        if self.age==anotherone.age:
            print("they are same")
        else:
            print("they are different")
p1=human()
p2=human()
p2.name="mustafa"
p2.age=30
print(p1.name, p1.age)
print(p2.name, p2.age)
p1.update()
print(p1.name,p1.age)
print(p1.compare(p2))
#////////////
#Types of variables
#1- Class/static variables
#2-Object/instance variables

class car:
    wheels=4 # this is class variable
    def __init__(self):
        self.mil=1000
        self.brand="TOGG" #these are object/instance variables

c1=car()
c2=car()
c1.mil=800
#////////////////////////////////
#Types of methods
#1- Class methods
#2-Object/instance methods
#3-static methods

class student:
    
    school="ITU"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)/3
    
    def getM1(self): #accessor method
        return self.m1
    
    def setM1(self,value): #mutator method
        self.m1=value
        return self.m1
    @classmethod         #if you use class method then you have use class decorator
    def getschool (cls): #class method
        return cls.school
    
    @staticmethod #if you use static method then you have use class decorator
    def info (): #static method
        print("This is student class")

s1=student(23,56,46)
s2=student(65,34,98)

print(s1.avg)
print(student.info())
#////////////////////////////////////
# Inner class
class student: #outer class
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop() 
    def show(self):
        print(self.name,self.rollno)
    
    class laptop: # inner class
        def __init__(self):
            self.brand="hp"
            self.cpu="i9"
            self.ram=16 
        def __str__(self)->str:
            return f"{self.brand}, {self.cpu}, {self.ram}"
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=student("siyar",2)
s2=student("siyar2",4)
s1.show()
#lap1=student.laptop()
print(s1.lap.brand)
lap1=s1.lap
lap2=s2.lap
print(lap1.show())
print("s1:",s1)
#//////////////////////////////
# Inheritance
class a:
    def feature1(self):
        print("feature 1 is working")
        
    def feature2(self):
        print("feature 2 is working")    
        
class b(a):  #single level inheritance
    def feature3(self):
        print("feature 3 is working")
        
    def feature4(self):
        print("feature 4 is working") 
        
class c(b):  # multi level inheritance (c can get a and b feature)
    def feature5(self):
        print("feature 5 is working")

class d(c,b): #multiple inheritance (d can get c and b feature)       
    def feature6(self):
        print("feature 6 is working")         
        
a1=a()
a1.feature1()
b1=b()        
b1.feature2()
c1=c()
c1.feature3()
d1=d()
d1.feature5()
#///////////////////////////////////////////////////
# Constructor in Inheritance
class a:
    def __init__(self):  # if b don't have initial function then when you call b class it will initial a's initial function
        print("in a init")
    def feature1(self):
        print("feature 1 is working")
        
    def feature2(self):
        print("feature 2 is working")    
        
class b():  #single level inheritance
    def __init__(self):  # if b have initial function then when you call b class it will initial only b's initial function
        print("in b nit")
        super().__init__()  #but if you add this then when you call b class it will initialize a and b's initial functions
    def feature3(self):
        print("feature 3 is working")        
class c(a,b):  #single level inheritance
    def __init__(self):  # if b have initial function then when you call b class it will initial only b's initial function
        print("in c nit")
        super().__init__()  #Method Resolution Order(MRO) it will call class a
    def feat(self):
        super().feature2() 
b1=b()
c1=c() 
c1.feat()        
        
        
    