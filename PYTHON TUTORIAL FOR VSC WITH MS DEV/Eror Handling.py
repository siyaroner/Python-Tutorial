# #Syntax Errors
# #This code won't run at all cuz we need to add : this after y
 x=34
 y=65
 if x==y
    print ("success")

# #Runtime Errors
# #This code will fail when run
x=3
y=0
 print(x/y)

# #Catching runtime errors

try:
    print (x/y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print ("Sorry, something went wrong")
else:
    print ("Something really went wrong")
finally:
    print ("This always runs on succes or failure")


# Logic Errors
#This code won't run at all
 x=453
 y=45
 if x<y :
     print (str(x)+" greater than "+ str(y))
     

