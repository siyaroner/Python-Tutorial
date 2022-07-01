# Lists are collections of items

names = ["Muhammed", "Mustafa"]
scores=[]
scores.append (98) #add new item to the end
scores.append (99) #add new item to the end
print (names)
print(scores)
print (scores [1]) # Collections are zero-indexed

# Arrays are also collections of items

from array import array
scores= array ('d')
scores.append(97)
scores.append(56)
print (scores)
print (scores [1]) 

# Difference between of lists and array
# Array: 1- Numarical data types 2- Must all be the same type
# Lists: 1- Store anything  2- Store anytype

# Common Operations

names = ["Muhammed", "Emin"]
print (len(names)) # Get the number of items in the list
names.insert (0, "Omer") # İnsert before index
print (names[0]) 
names.sort () 
print (names)

# Retrieving Ranges

names= ["Muhammed", "Ebubekir", "Omer", "Ali"]
presenters = names [1:3] # it will only show second and third items

print (names)
print (presenters)

#Dictionaries

person = {"first": "Osman"}  #first is tag of Osman
person ["last"]= "Ebu Hureyre" #last will be tag of Ebu Hureyre
print (person)
print (person["first"])

# Difference between of lists and Dictionaries
# Dictionaries: 1- Key/Value pairs 2- Storage order not guaranteed
# Lists: 1- Zero-based index  2- Storege order guaranteed

siyar = {}
siyar["first"]= "Siyar"
siyar["last"]= "Oner"

Mustafa = {}
Mustafa["first"]= "Mustafa"
Mustafa["last"]= "Oner"

people= []
people.append (siyar)
people.append (Mustafa)
people.append ( {
    "first": "Hasan", "last": "Medya"
})
print (people)