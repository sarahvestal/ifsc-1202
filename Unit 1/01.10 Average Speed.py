#Write a program that prompts for the lenght of a race in kilometers, the prompts for the number of minutes and number of seconds needed to run the race.
#Display the average speed in Miles per Hour
#Hint: Use the int() function to convert your input to an integer.
#Hint: There are 1.61 kilometers in a mile.
#Enter Length of Race in Kilometers: 10
#Enter Minutes: 61
#Enter Seconds: 33
#6.054765352614396

kilometers = input("Enter number of kilometers in race: ")
minutes = input("Enter number of minutes to complete: ")
seconds = input("Enter number of seconds to complete: ")
seconds_minute = (int(seconds)) / 60
time = (int(minutes)) + (float(seconds_minute))
hours = (float(time)) / 60
miles = (int(kilometers)) / 1.61
mph = (float(miles)) / (float(hours))
print (mph)