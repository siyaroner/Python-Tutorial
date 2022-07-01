# First way
a=5
b=6
temp= a
a=b
b=temp
print("a=",a,"b=",b)
# Second way
a=5
b=6
a,b = b,a
print("a=",a,"b=",b)
