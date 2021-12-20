ageY = float(input())
while True:
    if ageY < 0 or ageY > 50:
        ageY = float(input())
    else:
        break


ageM = float(input())
while True:
    if ageM < 0 or ageM > 50:
        ageM = float(input())
    else:
        break

arithmetic_difference = ageM - ageY

ageO = ageM + arithmetic_difference

print(ageO)

# completed code in 2 minutes 42 seconds