from datetime import date
today=str(date.today())
year=int(today[:4])
month=int(today[5:7])
day=int(today[8:])
print("To calculate your age please enter your:")
birth_year=int(input("Enter your birth year: "))
birth_month=int(input("Enter your birth month: "))
birth_day=int(input("Enter your birth day: "))

if month<birth_month:
    print("your age is ",year-birth_year-1)
elif month>=birth_month:
        print("your age is ",year-birth_year)

