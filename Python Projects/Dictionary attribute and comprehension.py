# Dictionary comprehension
import random
customers = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
discount_dict = {customer:random.randint(1,100) for customer in customers}
print(discount_dict)

# Methods	Description

# copy()	    They copy() method returns a shallow copy of the dictionary.
# clear()	    The clear() method removes all items from the dictionary.
# pop()	            Removes and returns an element from a dictionary having the given key.
# popitem() 	    Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
# get()	            It is a conventional method to access a value for a key.
# values()	    returns a list of all the values available in a given dictionary.
# str() 	    Produces a printable string representation of a dictionary.
# update()	    Adds dictionary dict2’s key-values pairs to dict
# setdefault()      Set dict[key]=default if key is not already in dict
# keys()	    Returns list of dictionary dict’s keys
# items()	    Returns a list of dict’s (key, value) tuple pairs
# has_key() 	    Returns true if key in dictionary dict, false otherwise
# fromkeys()	    Create a new dictionary with keys from seq and values set to value.
# type()	    Returns the type of the passed variable.
# cmp()	            Compares elements of both dict.

### 1- copy()   They copy() method returns a shallow copy of the dictionary.
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
d1={}
d1=d.copy()
print(d1)

### 2- clear()  The clear() method removes all items from the dictionary.
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
# Deleting entire Dictionary
d.clear()
print("\nDeleting Entire Dictionary: ")
print(d)

### 3- pop()    Removes and returns an element from a dictionary having the given key.
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
# Deleting a key
# using pop() method
print(f"\nDictionary before deletion: {str(d)}")
pop_ele = d.pop(1)
print("The arbitrary pair returned is: " + str(pop_ele))
print('\nDictionary after deletion: ' + str(d))

### 4- popitem()        Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
# Deleting an arbitrary key (actually last item)
# using popitem() function
pop_ele = d.popitem()
print("\nDictionary after deletion: " + str(d))
print("The arbitrary pair returned is: " + str(pop_ele))

### 5- get()    It is a conventional method to access a value for a key.
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
# accessing a element using get()
# method
print("Accessing a element using get:")
print(d.get(3))

### 6- values()         returns a list of all the values available in a given dictionary.
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
print(d.values())

### 7- str()          Produces a printable string representation of a dictionary.  
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
print(str(d))

### 8- update()         Adds dictionary dict2’s key-values pairs to dict
# Dictionary with three items
Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'} 
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)
#/////////////////////////////
# update the Dictionary with iterable
Dictionary1.update(D='name1', E='name2')
print("Dictionary after updation:")
print(Dictionary1)
#///////////////////////////////////////
Dictionary1[1]="name3"
print(Dictionary1)
#///////////////////////////////////////

### 9- setdefault()             Set dict[key]=default if key is not already in dict
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
first=d.setdefault(1)
print(first)

### 10- keys()          Returns list of dictionary dict’s keys
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
print(d.keys())

### 11- items()         Returns a list of dict’s (key, value) tuple pairs
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
print(d.items())

### 11- has_key()         (has_key removed from python 3.x so you can use "in" instead of it) Returns a list of dict’s (key, value) tuple pairs
d={1:"Siyar", 2:"Hasan", 3:"Mustafa"}
print(2 in d)

### 12- fromkeys()	    Create a new dictionary with keys from seq and values set to value.
# Python 3 code to demonstrate working of fromkeys()
# initializing sequence
seq = {'a', 'b', 'c', 'd', 'e'} 
# using fromkeys() to convert sequence to dict initializing with None
res_dict = dict.fromkeys(seq) 
print("The newly created dict with None values : " + str(res_dict))
# using fromkeys() to convert sequence to dict initializing with 1
res_dict2 = dict.fromkeys(seq, 1)
print("The newly created dict with 1 as value : " + str(res_dict2))
#////////////////////////////////////////////////////////////////
x = ('key1', 'key2', 'key3')
y = 0 
d = dict.fromkeys(x, y)
print(d)
#////////////////////////////////////////////////////////////////
# Python 3 code to demonstrate behaviour with mutable objects
seq = {'a', 'b', 'c', 'd', 'e'}
lis1 = [2, 3]
# using fromkeys() to convert sequence to dict using conventional method
res_dict = dict.fromkeys(seq, lis1)
print("The newly created dict with list values : "+ str(res_dict))
lis1.append(4)
print("The dict with list values after appending : "+ str(res_dict))
lis1 = [2, 3]
print('\n')
# using fromkeys() to convert sequence to dict using dict. comprehension
res_dict2 = {key: list(lis1) for key in seq}
print("The newly created dict with list values : "+ str(res_dict2))
lis1.append(4)
print("The dict with list values after appending (no change) : " + str(res_dict2))


### 13- type()	    Returns the type of the passed variable.
# Python3 simple code to explain the type() function
print(type([]) is list)  
print(type([]) is not list) 
print(type(()) is tuple)  
print(type({}) is dict)  
print(type({}) is not list)

### 14- cmp()	     Compares elements of both dict.
#cmp(dict1, dict2)
#This method returns 0 if both dictionaries are equal, -1 if dict1 < dict2 and 1 if dict1 > dic2.
# dict1 = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Name': 'Mahnaz', 'Age': 27}
# dict3 = {'Name': 'Abid', 'Age': 27}
# dict4 = {'Name': 'Zara', 'Age': 7}
# print ("Return Value : %d", cmp(dict1, dict2))
# print ("Return Value : %d",cmp (dict2, dict3))
# print ("Return Value : %d",cmp (dict1, dict4))


# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
############################
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
####################################
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
 
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
 
print(Dict)
##################################

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
 
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
 
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
 
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
 
# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
###############################################
# Python program to demonstrate 
# accessing a element from a Dictionary
 
# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
 
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
 
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])
###################################

# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)
 
# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)
 
# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
