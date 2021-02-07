#Prompt for a positive real number
#Print the first digit to the right of the decimal point.
#Enter Number: 1.79
#Tenths Value: 7

number = float(input("Enter a positive real number: "))
onedigitright = int(number % 1 * 10)
print ("First digit to right of decimal: {}".format (onedigitright,1))