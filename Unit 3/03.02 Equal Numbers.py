#Given three integers, determine how many of them are equal to each other.
#The program must print one of these numbers:
#3 (if all are the same),
#2 (if two of them are equal to each other and the third is different) or
#0 (if all numbers are different).
#Enter First Number: 10
#Enter Second Number: 5
#Enter Third Number: 10
#2

firstnum = int(input("Enter a first number: "))
secondnum = int(input("Enter a second number: "))
thirdnum = int(input("Enter a third number: "))
if firstnum == secondnum == thirdnum:
    print("3")
elif firstnum == secondnum:
    print("2")
elif firstnum == thirdnum:
    print("2")
elif secondnum == thirdnum:
    print("2")
else:
    print("0")