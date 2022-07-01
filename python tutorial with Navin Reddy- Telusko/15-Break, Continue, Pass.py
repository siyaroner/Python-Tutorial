# Break
stock=5
ordr= int(input("Hello, how many candy do you want to buy?: \n"))
i=1
while i<=ordr:
    
    if i>stock:
        print("Sorry, we don't have that much candy, we just have "+ str(stock) + " candies")
        break  # it will break the loop
    else:
        print("candy")
    i+=1
print ("Goodbye")

# Continue
for i in range (1,101):
    if i%3==0 and i%5==0:
        continue          # it won't break the loop and won't execute command it will just continue for the next step
    print(i)
print("Goodbye")

# Pass

for i in range(1,101):
    if i%2!=0:
        pass    # pass means there's no code to execute so we add pass because we don't wanna get an error
    else:
        print(i)
print("Goodbye")