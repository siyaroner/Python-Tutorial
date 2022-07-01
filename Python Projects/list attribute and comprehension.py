people=[("siyar",7500),
           ("Veysel",16000),
           ("Furkan",0)]
#First method
rich1=[]
for name,income in people:
    if income>10000:
        rich1.append(name)        
print(rich1)
#Second method
rich2=[name for name,income in people if income>14000]
print(rich2)
################################
# Methods	Descriptions

# append()	adds an element to the end of the list
# extend()	adds all elements of a list to another list
# insert()	inserts an item at the defined index
# remove()	removes an item from the list
# pop()	    returns and removes an element at the given index
# clear()	removes all items from the list
# index()	returns the index of the first matched item
# count()	returns the count of the number of items passed as an argument
# sort()	sort items in a list in ascending order
# reverse()	reverse the order of items in the list
# copy() 	returns a shallow copy of the list
a=[]
b=[1,3,4,5]
a.append(6)
print(a)
b.extend(a)
print(b)
b.insert(1,2)
print(b)
b.remove(6)
print(b)
b.pop(4)
print(b)
a.clear()
print(a)
print(b.index(3))
print(b.count(1))
b.insert(0,5)
b.sort()
print(b)
b.reverse()
print(b)
c=b.copy()
print(c)
del c
print(c)



