import sys
sys.setrecursionlimit(1000)
i=1
def greet():
    global i
    print("Hey", i)
    i+=1
    greet()
    
greet()