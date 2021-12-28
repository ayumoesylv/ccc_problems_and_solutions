k = int(input("Enter integer: "))


def expand(chr):
    new_chr = ''
    for i in range(0, k):
        new_chr = new_chr + chr
    return new_chr


for i in range(0, k):
    print(expand('*') + expand('x') + expand('*'))

for i in range(0, k):
    print(expand(' ') + expand('x') + expand('x'))

for i in range(0, k):
    print(expand('*') + expand(' ') + expand('*'))

# finished in 18 minutes
