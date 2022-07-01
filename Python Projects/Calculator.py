a=None
b=None
rslt=0

def add(a,b):
    if a!=None:
       global rslt
       rslt=a+b
       print(rslt)
       continue_calc()
       
def sub(a,b):
    if a!=None:
       global rslt
       rslt=a-b
       print(rslt)
       continue_calc()
       
def mul(a,b):
    if a!=None:
       global rslt
       rslt=a*b
       print(rslt)
       continue_calc()
       
def div(a,b):
    if a!=None:
       global rslt
       rslt=a/b
       print(rslt)
       continue_calc()
      
def finisher():
    while True:
        print(f"Result: {rslt}")
        break 
def continue_calc():
    global rslt
    a=rslt
    operator=input("Enter operator: ") 
    if operator=="=":
        finisher()      
    
    if operator=="+":
        b=input("Enter other number: ")
        add(int(a),int(b))
    if operator=="-":
        b=input("Enter other number: ")
        sub(int(a),int(b))
    if operator=="*":
        b=input("Enter other number: ")
        mul(int(a),int(b))
    if operator=="/":
        b=input("Enter other number: ")
        div(int(a),int(b))
        
if __name__=="__main__":    
    def enter():
        
            a=None
            b=None
            if a==None and b==None:
                
                a=input("Enter first number: ")
                operator=input("Enter operator: ")        
                b=input("Enter second number: ")
                if operator=="=":
                    finisher()
                if operator=="+":
                    add(int(a),int(b))
                if operator=="-":
                    sub(int(a),int(b))
                if operator=="*":
                    mul(int(a),int(b))
                if operator=="/":
                    add(int(a),int(b))
              
    enter()
  

