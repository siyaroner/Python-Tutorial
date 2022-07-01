
#Custom string formatting function
first_name= 'Siyar'
last_name= 'Oner'
output= 'Hello, '+ first_name+" "+ last_name
print(output)
output= "Hello, {} {} ".format(first_name, last_name)
print(output)
output= "Hello, {0} {1} ".format(first_name, last_name)
print(output)
output= "Hello, {1} {0} ".format(first_name, last_name)
print(output)
#onyly avaiblale in python 3
output= f"Hello, {first_name} {last_name} "
print(output)

