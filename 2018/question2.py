N = int(input("Enter parking spaces: "))
yesterday = str(input("Enter parking yesterday: "))
today = str(input("Enter parking today: "))

same_count = 0

for i in range(0, N):
    if yesterday[i] == 'C' and today[i] == 'C':
        same_count += 1


print(same_count)

# finished in 6 minutes 16 seconds
