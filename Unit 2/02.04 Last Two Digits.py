#Enter a number greater than zero and print the value its last two digits.
#Be sure to use to .format method to create your output. You will have to use leading zeros.
#Enter a Number: 178
#Last Two Digits: 78

number = int(input("Enter a number greater than zero: "))
onedigit = number % 10
tendigit = int(number % 100 / 10)
print ("Last two digits: {}{}".format(tendigit, onedigit))


# Here is my revised entry for 02.03 as I am apparently not allowed to change a submission before grading?????

#n = int(input("Enter a two-digit number: "))
#first_digit = n // 10
#second_digit = n % 10
#swapped_number = (second_digit * 10) + first_digit
#print ("Swapped Number: {}".format(swapped_number))