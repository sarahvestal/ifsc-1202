#Prompt for two two-digit numbers.
#Merge them into single number as follows:
#Tens digit from first number
#Tens digit from second number
#Units digit from first number
#Units digit form second number
#Enter First 2 Digit Number: 12
#Enter Second 2 Digit Number: 34
#Merged Number: 1324

numberfirst = int(input("Enter the first 2-digit number: "))
onedigitfirst = int(numberfirst % 10)
tendigitfirst = int(numberfirst % 100 / 10)
numbersecond = int(input("Enter the second 2-digit number: "))
onedigitsecond = int(numbersecond % 10)
tendigitsecond = int(numbersecond % 100 / 10)
print ("Merged number: {}{}{}{}".format(tendigitfirst, tendigitsecond, onedigitfirst, onedigitsecond))