#Enter a two digit number and swap their digits and create a new two digit number.
#Be sure to use the .format method to create your output.
#Enter a Number: 17
#Swapped Number: 71

n = int(input("Enter a two-digit number: "))
first_digit = n // 10
second_digit = n % 10
swapped_number = (second_digit * 10) + first_digit
print (swapped_number)