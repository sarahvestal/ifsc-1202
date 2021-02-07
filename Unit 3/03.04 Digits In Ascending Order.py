#Given a three-digit integer, print "YES" if its digits are in ascending order left to right, print "NO" otherwise.
#Enter a Number: 123
#YES
#Enter a Number: 132
#NO

number = int(input("Enter a three-digit integer: "))
onedigit = int(number % 10)
tendigit = int(number % 100 / 10)
hundreddigit = int(number % 1000 / 100)
if hundreddigit < tendigit < onedigit:
    print("YES")
else:
    print("No")
