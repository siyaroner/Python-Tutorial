
def fac(n):
    if n<0:
        print("The number cannot be negative")
    else:
        if n==0:
            print(1)
        else:
            b=n
            for i in range(1,n+1):
                b=b*(n-i)             
                i+=1
                if i==n-1:
                    print(b)
                    break
                     
                  
n=input("Which number's factorial do you want: ")
fac(int(n))
