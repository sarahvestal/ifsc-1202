#Given a month - an integer from 1 (January) to 12 (December), print the number of days in the month.
#Assume that it is a non-leap year.
#Enter Month: 2
#28

month = int(input("Enter an integer representing the month of the year: "))
if month == 2:
    print("28")
elif month == 4 or 6 or 9 or 11:
    print("30")
else:
    print("31")