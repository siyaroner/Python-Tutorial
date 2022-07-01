
# 1- F/f String
name="siyar"
x=F"Hello {name} {[1, 3]}"
print(x)

# 2- Unpacking
tup= (1,2,3,4,5)
lst=[1,2,3,4,5]
string= "hello"
dic={"a":1, "b":2}
coords=[5,6]

a,b,c,d,e=tup
print(a,b,c,d,e)
a,b,c,d,e=lst
print(a,b,c,d,e)
a,b,c,d,e=string
print(a,b,c,d,e)
a,b=dic  # it will give keys
print(a,b)
a,b=dic.values()  # it will give values
print(a,b)
a,b=dic.items()  # it will give all items with tupple
print(a,b)
x,y=coords
print(x,y)

# 3- Multiple Assignment

width, height=400,500
# if you wanna swap them just do this:
width,height=height,width

# 4- Comprehensions

x=[0 for i in range (10)]
x=[i for i in range (10)]
x=[i for i in range (10) if i%2==0]
x=[i*j for i in range (10) for j in range(20)]
x=[[0 for _ in range (3)] for _ in range(5)]  # if you're not gonna use variable you can use simply _
x=(i for i in 8)  # this is generator object
print(list(x))  # if you use "list" you can convert generator objects into list, or you can convert into tupple by using "tuple" as well
sentence= "hello my name is siyar"
x={char: sentence.count(char) for char in set(sentence)} # this will give the frequence usage of each character in a dictionary
print(x)

# 5- Inline/Ternary Condition

x=1 if 2>3 else 0 # if you don't use else it'll give an error

# 6- Zip

names=["siyar","furkan","leyla","biyo"]
ages=[27,26,25,24]
eye_colors=["blue","green","black","brown","gray"]
# print(list(zip(names,ages,eye_color)))
for name,age,eye_color in zip (names, ages,eye_colors):
    if age>25:
        print(name)
        
# 7-*args and **kwargs
def func1 (arg1,arg2,arg3):
    print(arg1,arg2,arg3)
    
def func2 (arg1=None,arg2=None,arg3=None):
    print(arg1,arg2,arg3)

def func3 (*args, **kwargs):
    print(kwargs,args)
    
args=[1,2,3]
kwargs={"arg2":2,"arg1":1,"arg3":3}
func1(args[0],args[1],args[2])  # This a way to call it
func1(*args)   # * this will unpack the items pass them the function
print("packed: ",args,"\nunpacked(*):",*args)
func2(*kwargs) #this will send key items to the function
func2(**kwargs) #*kwargs) #this will send value items to the function and it will in function order
func3(*args,**kwargs)

# 8 For else & While else
source=[3,5,6,7,8,9]
target=int(input("type the number you wanna search in the source"))
for element in source:
    if element is target:
        print("The target had been found in the source")
        break
else:
    print("Sorry boss, we didn't find the target'")

# 9 Sort By Key
lst=[[1,2],[3,4],[4,2],[-1,3],[4,5],[2,3]]
lst.sort()
print("Normal sorting: ",lst)
lst.reverse()
      #or
lst.sort(reverse=True)
print("Reverse sorting: ",lst)
lst.sort(key=lambda x:x[1]) # it will sort by second elment. lambda is like def func(x): return x[1]
print("Sorting by second elment: ",lst)
lst.sort(key=lambda x:x[1]+x[0]) # it will sort by second+first .
print("Sorting by elments sum: ",lst)
    
# 10 Itertools
import itertools

lst=[1,2,3,4,5,6,7,8]
sum_lst=itertools.accumulate(lst)
print(list(sum_lst))

lst2=["a", "b", "c", "d", "e"]
chain_lst=itertools.chain(lst,lst2)
print(list(chain_lst))

names=["Siyar","Furkan","Veysel","Biyobro"]
show=[1,0,0,1]
compressed_lst=itertools.compress(names,show)
print(list(compressed_lst))