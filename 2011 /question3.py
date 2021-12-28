t1 = float(input("Enter a positive number: "))
t2 = float(input("Enter a positive number: "))

list = [t1, t2]
i = 0
idex = 0

# while i >= 0:
# i = list[idex] - list[idex + 1]
# term = i
# list.append(term)
# idex += 1

while True:
    i = list[idex] - list[idex + 1]
    if i >= 0:
        list.append(i)
        idex +=1

    else:
        break

print(len(list))

# finished in 11 minutes 54 seconds

# corrections
# fixed bug in while loop
