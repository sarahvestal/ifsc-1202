#Given the coordinates of the three points A, B, and C on a line, print a distance from the point A to closest point to it.
#Hint: Determine the distance from A to B by subtracting B from A, then determine the distance from A to C by subtracting C from A. Determine the smallest distance.
#Enter Point A: 10
#Enter Point B: 35
#Enter Point C: 30
#20

firstnum = int(input("Enter Point A: "))
secondnum = int(input("Enter Point B: "))
thirdnum = int(input("Enter Point C: "))
distanceAB = secondnum - firstnum
distanceAC = thirdnum - firstnum
if distanceAB < distanceAC:
    print(distanceAB)
if distanceAB >= distanceAC:
    print(distanceAC)