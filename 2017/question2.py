N = int(input("Enter number: "))
k = int(input("Enter non-neg integer: "))

sum = N

for i in range(0, k):
    N = N*10
    sum += N

print(sum)

# finished in 7 minutes 26 seconds

