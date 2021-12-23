vote_count = int(input("Enter total number of votes: "))
votes = str(input("Enter vote results: "))

votes.upper()

A_count = 0
B_count = 0

for i in votes:
    if i == 'A':
        A_count += 1

    if i == 'B':
        B_count += 1

while A_count + B_count == vote_count:
    if A_count > B_count:
        print("A")
        break

    elif B_count > A_count:
        print("B")
        break

    elif A_count == B_count:
        print("Tie")
        break

# finished in 6 minutes 13 seconds
