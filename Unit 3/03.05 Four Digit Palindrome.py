#A palindrome is a number which reads the same when read forward as it it does when read backward.
#Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
#Hint: put the units, tens, hundreds, and thousands in separate variables.
#Enter a Number: 1221
#YES
#Enter a Number: 1231
#NO

number = int(input("Enter a four-digit integer: "))
onedigit = int(number % 10)
tendigit = int(number % 100 / 10)
hundreddigit = int(number % 1000 / 100)
thousanddigit = int(number % 10000 / 1000)
firstdigits = str(thousanddigit) + str(hundreddigit)
seconddigits = str(onedigit) + str(tendigit)
if firstdigits == seconddigits:
    print("YES")
else:
    print("No")