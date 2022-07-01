# String can be stored in variables
first_name= 'Siyar'
print(first_name)

# You can combine strings with +
last_name= 'Oner'
print(first_name + last_name)
print("hello  " + first_name +" "+ last_name)

# You can use functions to modify strings
sentence ="the dog is named Sammy"
print ("to capitalize all letters: ") 
print(sentence.upper())
print ("to lower case all letters: ")  
print(sentence.lower())
print ("to capitalize only first letter: ") 
print(sentence.capitalize())
print ("to count the number of the a letter: ") 
print(sentence.count("a"))

# The functions help us format strings we save to files and databases, or display to users

first_name= input ("What's your first name: ")
last_name= input ("What's your last name: ")
print ("Hello "+first_name.capitalize() +" "+ last_name.capitalize())
print ("Hello "+first_name.upper() +" "+ last_name.upper())

# Custom string formatting function
first_name= 'Siyar'
last_name= 'Oner'
output= 'hello, '+ first_name+" "+ last_name
output= "Hello, {} {} ".format(first_name, last_name)
output= "Hello, {0}{1} ".format(first_name, last_name)
# onyly avaiblale in python 3
output= f"Hello, {first_name} {last_name} "