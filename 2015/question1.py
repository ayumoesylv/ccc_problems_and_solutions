month = int(input())
day = int(input())

if month == 2 and day == 18:
    print("Special")

elif month < 2 or month == 2 and day < 18:
    print("Before")

else:
    print("After")

# finished in 5 minutes