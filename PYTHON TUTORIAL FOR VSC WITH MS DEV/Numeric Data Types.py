#Number can be stored in variables
from symtable import Symbol


pi= 3.14
print(pi)

# You can do math with numbers
# Symbol    Operation
# +         Addition
# -         Subtraction
# *         Multiplication
# /         Division
# **        Exponent

first_num= 5
second_num= 4
print(first_num+second_num)
print(first_num**second_num)

# if you combine strings with numbers, Python gets confused
days_in_feb= 28
# print(days_in_feb +" days in February") #this will give an error
# So to avoid upper error we have to convert the number into the strings. Therefore we will will use str 
print(str(days_in_feb)+ " days in February")

# Numbers can be stored as strings. Numbers stored as strings are treadted as strings
first_num= "5"
second_num= "4"
print(first_num+second_num)

# The input function always returns strings.
first_num=input("Enters first number: ")
second_num= input("Enters second number: ")
print(first_num+second_num)

# if you want to do math with input number you shoult convert the strings into the number with int or float functions

first_num=input("Enters first number: ")
second_num= input("Enters second number: ")
print(int(first_num)+int(second_num))
print(float(first_num)+float(second_num))
