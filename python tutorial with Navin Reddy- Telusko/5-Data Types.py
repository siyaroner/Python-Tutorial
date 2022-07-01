# None (null)
# Numeric (int, float, complex, bool(True, False))

a= 5.6 
type(a) #float
b=int(a)
type(b) #integer
k=float(b)
c=complex(k,b)
i=int(True)# 1
print(a,b,k,c,i)
#Squence:
    # List
    # Tuple
    # Set
    # String
    # Range
lst=[2,3,34,51]
type (lst)# List
st= {80,67,54}
type(st)# Set
tpl=(768,45,83)
type(tpl)# Tuple
strn="String"
range(10) # from 0 to 10
list(range(10))
list (range(2,14,2)) #list(range(start, end, increase))
#Dictionary (mapping) {"key":"value",...} instead of index number we use key
d= {"siyar":"samsung","mustafa":"iphone"}
print(d)
print(d.keys())
print(d.values())
print(d["siyar"])
print(d.get("mustafa"))


