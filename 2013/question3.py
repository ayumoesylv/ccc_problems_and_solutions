Y = int(input("Enter start year: "))
D = Y + 1

def check_if_different(Y):
    check_list = []
    for i in range(0, len(str(Y))):
        if str(Y)[i] not in check_list:
            check_list.append(str(Y)[i])

        else:
            return False
    return True

while True:
    if check_if_different(D) == True:
        print(D)
        break

    else:
        D += 1

# finished in 48 minutes

