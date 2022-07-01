gpa = float (input("What was your Grade Point Average?: "))    
lowest_grade= input ("What was your lowest grade?: ")
lowest_grade= float (lowest_grade)
if gpa>= .85 and lowest_grade >= .70:
    print("Well done")

# if you need to remember the results of a condition check later in your code, use Boolean variables as flags

if gpa>= .85 and lowest_grade >= .70 :
    honour_roll = True
else:
    honour_roll= False
#somewhere later in your code 
if honour_roll:  # This means if it's true so we don't need to specify it again
    print ("Well done")

# A student makes honour roll if their average is >= 85 and their lowest grade is not below 70

gpa = float (input("What was your Grade Point Average?: "))    
lowest_grade= input ("What was your lowest grade?: ")
lowest_grade= float (lowest_grade)

if gpa>=.85 and lowest_grade>= .70:
    print ("You made the honour roll")
    