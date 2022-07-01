# We often need current date and time when logging errors and saving data

# To get current date and time we need to use the datetime library 
from datetime import datetime, timedelta
from email.utils import format_datetime
# -To get Day name
# import datetime
# day_name = datetime.datetime.now()
# print("Today is ",day_name.strftime("%A"))
current_date = datetime.now()
# the now function returns a datetime object
print ("today is: " + str(current_date))

# timedate is used to define a period of time
today = datetime.now()
# the now function returns a datetime object
print ("today is: " + str(today))
one_day= timedelta(days=1)
yesterday= today-one_day
print ("yesterday was: " + str(yesterday))

# Use date functions to control date fomatting
print ("day: " + str(current_date.day))
print ("month: " + str(current_date.month))
print ("year: " + str(current_date.year))

print("hour: " +str(today.hour))
print ("minute: " +str(today.minute))
print ("second: "+ str(today.second))
# Sometimes you receive the date as a string and need to convert it to a datetime object
birthday= input ("When is your birthday (dd/mm/yyyy)?: ")
birthday_date= datetime.strptime(birthday,"%d/%m/%Y")
print("Birthday: " +str(birthday_date))

print ("today is: " + str(today))
one_day= timedelta(weeks=1)
lastweek= today-one_day
print ("lastweek was: " + str(lastweek))
