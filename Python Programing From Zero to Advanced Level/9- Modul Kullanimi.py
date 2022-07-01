import math as m

for i in dir(m): print( i.strip("__"),end=", ")


print(help(m))
print(help(m.log))


from math import factorial as fac

fac(5)

### random ####
import random

print(random.random) #0-1
print(random.random*100)
print(random.uniform(10,100))
print(random.randint(1-600))

names=["a","b","c","d","e","f","g","h","i","j","k"]

print(names[random.randint(0,len(names)-1)]) #or
print(random.choice(names))
print(random.shuffle(names)) # to mix item in list
print(random.sample(names,3)) #it will choice ramdom 3 items in names


