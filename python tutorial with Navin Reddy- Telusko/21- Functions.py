def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b
rslt1,rslt2=add_sub(6,4)
print(f"add= {rslt1} \nsub= {rslt2}")


#Types of arguments
def person (age,name="Mustafa"):
    print(name)
    print(age)
    
person("Şiyar", 27)  # Position: we have to track the sequence, if we don't wanna any error
person(age=27, name="Şiyar") # Keyword: Or we can use keywords
person (27)

def sum (*a):             # if you add * sign you enter multiple items by just one variable
    c=0
    for i in a:
        c+=i
        
    print(c)

sum(3,4,5)

def person (name, *data):  # when you add * infront of variable it will return tuple for multiple item
    print(name)
    print(data)
    
person("Şiyar",27, "İstanbul", 1453)  

def person (name, **data):  # when you add ** infront of variable it will return dictionary for multiple item
    print(name)
    print(data)
    for i,j in data.items():
        print(i,":",j)
    
person("Şiyar", age=27, city="İstanbul", nmbr=1453)  

#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)





