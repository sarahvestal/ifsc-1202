#Enter a two digit number and print out its digits separately.
#Be sure to use to .format method to create your output.
#Enter a Number: 17
#Ones Digit: 7
#Tens Digit: 1

number = int(input("Enter a two digit number: "))
onedigit = number % 10
print ("Ones Digit: {}".format(onedigit))
tendigit = int(number % 100 / 10)
print ("Tens Digit: {}".format(tendigit))