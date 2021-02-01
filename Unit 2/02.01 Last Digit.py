#Prompt for a number and print its last digit.
#Be sure to use to .format method to create your output.
#Enter a number: 23
#Last Digit: 3

number = (int(input("Enter a number: ")))
ldigit= number % 10
print("Last Digit: {}".format(ldigit))

