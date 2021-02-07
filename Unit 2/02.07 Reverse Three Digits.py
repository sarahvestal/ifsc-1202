#Enter a three digit number and reverse the digits.
#Be sure to use to .format method to create your output.
#Enter a 3 Digit Number: 291
#Reverse of Digits: 192

number = int(input("Enter a three digit number: "))
onedigit = int(number % 10)
tendigit = int(number % 100 / 10)
hundreddigit = int(number % 1000 / 100)
print ("Reverse of digits: {}{}{}".format(onedigit, tendigit, hundreddigit))