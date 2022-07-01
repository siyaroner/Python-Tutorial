a=input("Enter a number to check it for prime number: ")
a=int(a)
lst=[]
if a>1:
    for i in range(2,a):
        if a%i==0:
           lst.append(i)    
        else:
            if i==a-1 and len(lst)==0:
                print(f"{a} is a prime number")
    if i==a-1 and len(lst)>0:   
        print(f"{a} is not a prime number. Because it can be diveded by {lst}") 
else:
    print(f"{a} is not a prime number")
