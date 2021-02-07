#Prompt for three numbers and print the smallest value.
#Try to use the cascade if-elif-else.
#Enter First Number: 3
#Enter Second Number: 1
#Enter Third Number: 2
#1

firstnum = int(input("Enter a first number: "))
secondnum = int(input("Enter a second number: "))
thirdnum = int(input("Enter a third number: "))
if firstnum < secondnum < thirdnum:
    print(firstnum)
elif secondnum < firstnum < thirdnum:
    print(secondnum)
else:
    print(thirdnum)