def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return (even,odd)
        
    
    

lst=[12,43,56,82,94,33,57,44]

even,odd=count(lst)
print("even number",even,"\nodd number:", odd)
print("Even: {} and odd: ".format(even,odd))