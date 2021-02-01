#Enter Number: 179
#The next number for the number 179 is 180.
#The previous number for the number 179 is 178.

enter_number = input("Enter a number: ")
next_number = int(enter_number) + 1
previous_number = int(enter_number) - 1
print("The next number for the number " + (str(enter_number)) + " is " + (str(next_number)) + ".")
print("The previous number for the number " + (str(enter_number)) + " is " + (str(previous_number)) + ".")