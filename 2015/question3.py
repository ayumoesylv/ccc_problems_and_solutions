word = str(input("Enter word: "))
word = word.lower()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

def find_next_vowel(letter):
    num = alphabet.index(letter)
    distance_up = 0
    distance_down = 0
    check_up = num
    check_down = num

    while (0 <= check_up <= 25) and (0 <= check_down <= 25):
        if alphabet[check_up - 1] in vowels:
            check_up -= 1
            distance_up += 1
            break

        if alphabet[check_up - 1] not in vowels:
            check_up -= 1
            distance_up += 1

        if alphabet[check_down + 1] in vowels:
            check_down += 1
            distance_down += 1
            break

        if alphabet[check_down + 1] not in vowels:
            check_down += 1
            distance_down += 1

    if distance_up > distance_down:
        return alphabet[check_up]

    if distance_up < distance_down:
        return alphabet[check_down]

    if distance_up == distance_down:
        return alphabet[check_up]


def find_next_consonant(letter):
    pass

for i in word:
    if i not in vowels:
        first = i
        second = find_next_vowel(i)
        #third = find_next_consonant(i)
        i = first+second

print(word)

# current time 52 minutes
# cannot finish this problem