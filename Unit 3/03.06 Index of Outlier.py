#Prompt for three integers: two are equal to each other and the third one is different.
#Print the index number of the different one, either 1, 2 or 3.
#Enter First Number: 10
#Enter Second Number: 5
#Enter Third Number: 10
#2

firstnumber = int(input("Enter the first two-digit integer: "))
secondnumber = int(input("Enter the second two-digit integer: "))
thirdnumber = int(input("Enter the third two-digit integer: "))
if firstnumber == secondnumber:
    print(thirdnumber)
elif firstnumber == thirdnumber:
    print(secondnumber)
elif secondnumber == thirdnumber:
    print(firstnumber)