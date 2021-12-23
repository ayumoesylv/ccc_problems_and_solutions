sign = str(input("Please type a word: "))

sign.upper()

list_of_letters = ['I', 'O' ,'S' ,'H' ,'Z' ,'X' ,'N']

for i in sign:
    if i not in list_of_letters:
        print("NO")
        break
else:
    print("YES")

# finished in 5 minutes 40 seconds