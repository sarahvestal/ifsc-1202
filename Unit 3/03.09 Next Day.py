#Prompt for a month (an integer from 1 to 12) and a day in the month (an integer from 1 to 31) in a common year (not a leap year).
#Print the month and the day of the next day after it.
#The first test corresponds to March 30 - next day is March 31
#The second test corresponds to March 31 - next day is April 1
#The third test corresponds to December 31 - next day is January 1
#Enter Month: 3
#Enter Day: 30
#Next Day: 3/31

month = int(input("Enter an integer representing the month of the year: "))
#day = int(input("Enter an integer representing the day of the month: "))
if month == 2:
    monthdays = 28
elif month == 4 or 6 or 9 or 11:
    monthdays = 30
else:
    monthdays = 31
#if day < monthdays:
#    day += 1
print int(monthdays)
#if day == monthdays:
#    day == 1 and month += 1
#print ("Next Day: {}{}".format(month, day))

    