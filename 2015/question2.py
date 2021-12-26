text = str(input("Type text: "))

smile_count = 0
frown_count = 0

for i in range(0, len(text)):
    if text[i] == ':' and text[i + 1] == '-' and text[i + 2] == ')':
        smile_count += 1

    if text[i] == ':' and text[i + 1] == '-' and text[i + 2] == '(':
        frown_count += 1

if smile_count == 0 and frown_count == 0:
    print("None")

elif smile_count == frown_count:
    print("Unsure")

elif smile_count > frown_count:
    print("Happy")

elif smile_count < frown_count:
    print("Sad")

# finished in 6 minutes 36 seconds
