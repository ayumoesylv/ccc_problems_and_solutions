h = int(input())
M = int(input())

for i in range(1, M):
    A = (-6 * i * i * i * i) + (h * i * i * i) + (2 * i * i) + i
    if A <= 0:
        print("The balloon first touches ground at hour", i)
        break

else:
    print("The balloon does not touch the ground in the given time.")

# finished in 13 minutes 48 seconds
