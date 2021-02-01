#A timestamp consists of three numbers:
#number of hours
#number of minutes
#number of seconds
#Given two timestamps, calculate how many seconds are between them.
#Assume that the moment of the first timestamp occurred before the moment of the second timestamp.

#First Timestamp
#Enter Hours: 6
#Enter Minutes: 1
#Enter Seconds: 30
#Second Timestamp
#Enter Hours: 6
#Enter Minutes: 2
#Enter Seconds: 10
#40

print ("First Timestamp:")
firsthour = input ("First Hour Number is: ")
firstminute = input ("First Minute Number is: ")
firstsecond = input ("First Second number is: ")
firsttotal = (int(firsthour)) * 3600 + (int(firstminute)) *60 + (int(firstsecond))

print ("Second Timestamp:")
secondhour = input ("Second Hour Number is: ")
secondminute = input ("Second Minute Number is: ")
secondsecond = input ("Second Second number is: ")
secondtotal = (int(secondhour)) * 3600 + (int(secondminute)) *60 + (int(secondsecond))

difference = (int(secondtotal - firsttotal))
#print (difference)