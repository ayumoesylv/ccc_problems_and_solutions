n = int(input("number of rounds: "))
Antonia = 100
David = 100

a = 0
d = 0

for i in range(0, n):
    rolls = str(input("Enter results: "))

    a = int(rolls[0])
    d = int(rolls[2])

    # let d represent david and a represent antonia

    if d > a:
        Antonia -= d

    if a > d:
        David -= a

print(Antonia)
print(David)

# finished in 21 minutes 9 seconds
