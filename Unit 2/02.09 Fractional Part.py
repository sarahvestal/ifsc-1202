#Enter a positive real number and print its fractional part.
#Hint: Round the result to 10 digits using the round function.
#Enter a Number: 17.9
#Fractional Part: 0.9

number = float(input("Enter a positive real number: "))
onedigitright = float(number % 1)
print ("Fractional Part: {}".format (round(onedigitright, 10)))
