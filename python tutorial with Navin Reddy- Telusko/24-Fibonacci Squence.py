lst=[]
def fib(n):
    a=0
    if n<0:
        print("The number must be equal or greater than 0")
        
    else:
    
        for i in range(n):
            if a==0:
                lst.append(a)
                a+=1
            else:
                lst.append(a)
                a=lst[i]+lst[i-1]
        print(lst)
n=input("How many fibonaci do you want: ")
fib(int(n))

# ANOTHER METHOD 

def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range (2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(-3)