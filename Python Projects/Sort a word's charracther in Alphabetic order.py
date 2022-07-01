# ord() converts a char into an ascii number
# chr() converts a number into a char

name="siyar oner"
name_lst=list(name.lower())
c=[]
for j in range(len(name_lst)):
    j=0
    Min=ord(name_lst[j])
    for i in range(len(name_lst)-1):
        temp=ord(name_lst[i+1])
        if temp<Min:
            Min=temp
    c.append(chr(Min))
    name_lst.remove(chr(Min))
def cnvrt():
    n="" 
    for i in c:
        n+=i
    return(n)  
print(cnvrt())
