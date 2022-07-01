name=input("Enter a string that you wanna reverse: ")
reversed_str=""
# for i in range(len(name)):
#     reversed_name.append(name[-i-1])
reversed_name=[j for i in range(len(name)) for j in name[-i-1]]
#reversed_name=[j for i in range(len(name)) for j in name[-i-1] if i==len(name)-1 for i in j: reversed_str+=i]
#reversed_name=[j for i in range(len(name)) for k in name[-i-1] for j in k ]
for i in reversed_name:
    reversed_str+=i   
print(reversed_str)