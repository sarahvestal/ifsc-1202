#Enter a number and print its tens digit.
#Be sure to use the .format method to create your output
#Enter a Number: 72
#Tens Digit: 7

number = int(input("Enter a number: "))
tendigit = int(number % 100 / 10)
print ("Tens Digit: {}".format(tendigit))