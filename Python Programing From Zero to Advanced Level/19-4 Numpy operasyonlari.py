import numpy as np

num1=np.random.randint(0,100,6)
num2=np.random.randint(0,100,6)
print(num1,"\n",num2,"\n")
# print(num1+num2,"\n")
# print(num2+10)
# print(num2-num1)
# print(num1*num2)
# print(num1/num2)
# print(num1/10)
# print(np.sin(num1))
# print(np.sqrt(num2))
# num3=num1.reshape(3,2)
# print(num3)
# print("\n \n",np.vstack((num1,num2))) #vertical stack
# print("\n \n",np.hstack((num1,num2))) #horizontal stack
# print(num1>50)
# print(num2 %2 ==0)
# print(num1[num2 %2 ==0])
mtrs=np.vstack((num1,num2))
print(mtrs)
rowtotal=mtrs.sum(axis=1)
print("rowtotal= ",rowtotal)
coltotal=mtrs.sum(axis=0)
print("coltotal= ",coltotal)



