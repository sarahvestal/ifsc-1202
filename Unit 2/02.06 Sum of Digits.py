#Enter a three digit number and print the sum of the digits.
#Be sure to use the .format method to create your output.
#Enter a 3 Digit Number: 179
#Sum of Digits: 17

number = int(input("Enter a three digit number: "))
onedigit = int(number % 10)
tendigit = int(number % 100 / 10)
hundreddigit = int(number % 1000 / 100)
print ("Sum of digits: {}".format(hundreddigit + tendigit + onedigit))