# Sometimes we copy and paste our code
import datetime
#print timestamps to see how long sections of code take to run
first_name = "Siyar"
print ("task completed")
start_time= datetime.datetime.now()
print (start_time)
print()

for x in range (0,10):
    print(x)
print("task completed")
finish_time= datetime.datetime.now()
print (finish_time)
print()
execution_time= finish_time - start_time
print(f'Execution time is:  {execution_time}') 

# Use functions instead of repeating code to

from datetime import datetime
#Print the current time and
start_time=datetime.now()
def print_time(function_variable, starttime):
        global start_time
        if function_variable is "start":
                start_time= datetime.now()
                print (f"start time is: {start_time}")
                    
        elif function_variable is "finish":
            finish_time= datetime.now()
            print (f"finish time is: {finish_time}")
            execution_time = finish_time - start_time
            print(f'Execution time is:  {execution_time}') 
            print ("Task compledted")
        
firstname= "Siyar"
print_time("start",start_time)
for x in range (0,10):
    print(x)
print_time("finish",start_time)

# returning value by function
def get_initial (name):
    initial = name[0:1].upper()
    return initial
first_name= input ("Please enter your first name: ")
first_name_initial = get_initial (first_name)
last_name= input ("Please enter your last name: ")
last_name_initial = get_initial (last_name)
print (f"Your initials are: {first_name_initial}{last_name_initial}")

# Functions can accept multiple parameters

def get_initial (name, force_uppercase):
    if force_uppercase:
        initial= name[0:1].upper()
    else:
        initial= name[0:1]
    return initial
first_name= input ("Enter your first name: ")
first_name_initial=get_initial (first_name, True) # if it is False it will pass so it will be whatever user input
print (f"your initial is: {first_name_initial}")

# You can also assign the values to parameters by name when you call the function

def get_initial (name, force_uppercase):
    if force_uppercase:
        initial= name[0:1].upper()
    else:
        initial= name[0:1]
    return initial
first_name= input ("Enter your first name: ")
first_name_initial=get_initial (force_uppercase= True, \
                                 name=first_name) # if it is False it will pass so it will be whatever user input
print (f"your initial is: {first_name_initial}")

# using the named natation when calling functions makes your code more readable

def error_logger (error_code, error_severity, log_to_db,\
                    error_message, source_modele):
    print (f"Error occurred {error_message}")
    # imagene code here that logs our error to a database or file

first_number= 10
second_number=5
print (" Second number is grater than first number. ") if first_number<second_number else error_logger(45,1, True,
                                                                                                       "First number is greater than second number","my_math_method")
