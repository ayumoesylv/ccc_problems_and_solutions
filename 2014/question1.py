angle1 = float(input("Please give a positive number: "))
angle2 = float(input("Please give a positive number: "))
angle3 = float(input("Please give a positive number: "))

if angle1 + angle2 + angle3 != 180:
    print("Error")

elif angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("Equilateral")

elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
    print("Isosceles")

else:
    print("Scalene")

# finished in 8 minutes 34 seconds
