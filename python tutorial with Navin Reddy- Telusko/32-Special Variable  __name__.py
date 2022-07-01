from Calc import * # this will run __name__ when you import it 

def welcome_bot():
    print("Hello User, you are welcome Calculator")
print(__name__)  
if __name__ == '__main__':  # __name__ is equal to __main__ 
    welcome_bot()
    
s= add(3,5)
print(s)