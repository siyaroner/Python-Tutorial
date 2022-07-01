# example 1

## without walrus
x=5
not_walrus=x<7
print(not_walrus)
## with walrus
x=5
print(walrus:=x<7)

# example 2
## without walrus
nums=[]
num=input("type a number: ")
while num.isdigit():
    nums.append(int(num))
    num=input("type a number: ")
print(nums)
## with walrus
nums=[]
while(num:=input("type a number: ")).isdigit():
    nums.append(int(num))
    input("type a number: ")
# example 2
## without walrus
nums=[]
num=input("type a number: ")
while num.isdigit():
    nums.append(int(num))
    num=input("type a number: ")
print(nums)
## with walrus
nums=[]
while(num:=input ("type a number: ")).isdigit():
    nums.append(int(num))
