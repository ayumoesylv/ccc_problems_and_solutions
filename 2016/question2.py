line1 = input("enter numbers: ")
line2 = input("enter numbers: ")
line3 = input("enter numbers: ")
line4 = input("enter numbers: ")

list1 = []
list2 = []
list3 = []
list4 = []


for i in range(0, len(line1)):
    number = ''
    if not ' ':
        number = ''
        number = number+str(i)

    list1.append(int(number))

for i in range(0, len(line2)):
    number = ''
    if not ' ':
        number = ''
        number = number+str(i)

    list2.append(int(number))

for i in range(0, len(line3)):
    number = ''
    if not ' ':
        number = ''
        number = number+str(i)

    list3.append(int(number))

for i in range(0, len(line4)):
    number = ''
    if not ' ':
        number = ''
        number = number+str(i)

    list4.append(int(number))

sum1h = list1[0] + list1[1] + list1[2] + list1[3]
sum2h = list2[0] + list2[1] + list2[2] + list2[3]
sum3h = list3[0] + list3[1] + list3[2] + list3[3]
sum4h = list4[0] + list4[1] + list4[2] + list4[3]

sum1v = list1[0] + list2[0] + list3[0] + list4[0]
sum2v = list1[1] + list2[1] + list3[1] + list4[1]
sum3v = list1[2] + list2[2] + list3[2] + list4[2]
sum4v = list1[3] + list2[3] + list3[3] + list4[3]

if sum1h == sum2h == sum3h == sum4h == sum1v == sum2v == sum3v == sum4v:
    print("magic")

else: print("not magic")

# currently stuck, time spent so far 24 minutes 50 seconds

