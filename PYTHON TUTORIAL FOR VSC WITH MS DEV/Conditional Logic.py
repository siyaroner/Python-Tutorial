# i=1
# for i in range (i+2):
#     price= int(input("Please enter price of the product: "))
#     if price >=1.00:
#         tax= .07
#         print (tax)
#     else:
#         tax= 0
#         print (tax)
    
    
price= float(input("Please enter price of the product: "))
if price >=1.00:
     tax= .07
     tax_price= price*tax
     total_price= price+ tax_price
     print(" product price: "+str(price), "\n tax price: "+str(tax_price), "\n total price: "+str(total_price))
else:
    tax= 0
print (tax)

# Comparison of strings are case insensitive so you should be careful

country= "CANADA"
if country == "canada":
    print ("oh look a Canadian")
else:
    print ("You are not from Canada")

#To avoid this problem you should use string function such as lower or upper functions

if country.lower()== "canada":
    print("oh look a Canadian")
else:
    print ("You are not from Canada")
 
#Multiple conditions
province= input ("What province do you live in? ")
tax=0
if province.upper() == "Alberta":
    tax= 0.05
elif province.lower()== "Nunavut":
    tax=0.05
elif province.upper == "Ontario":
    tax=0.13
print (tax)

# Same but different expressions
province= input ("What province do you live in? ")
tax=0
if province.upper() == "Alberta" or province.lower()== "Nunavut":
    tax= 0.05
elif province.upper == "Ontario":
    tax=0.13
else :
    tax= 0.15
print (tax)

# Same but different expressions
country= input ("What country do you live in? ")

if country.upper() == "Canada":
    province= input ("What province do you live in? ")
    tax=0
    if province.upper() in ("alberta", "nunavut","yukon"):
        tax= 0.05
    elif province.upper == "Ontario":
        tax=0.13
    else :
        tax= 0.15
else :
    tax=0
print (tax)

