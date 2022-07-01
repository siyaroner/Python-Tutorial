# enumarating items
#example 1
my_lsit=["apples", "pears","oranges","fruits"]

# way
count=1
for i in my_lsit:
    print(i)
   
    if count>=1:
        print(f"count is {count}")
    count+=1
#way 2
for i, items in enumerate(my_lsit,start=1):
    print(i,":",items)

# example 2
days=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY","FRIDAY", "SATURDAY", "SUNDAY"]
#way 1
enumerated_days=enumerate(days,start=1)
print(list(enumerated_days))

#way 2
for i, day in enumerate(days,start=1):
    print(i,":",day)