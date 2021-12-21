game1 = str(input())
game2 = str(input())
game3 = str(input())
game4 = str(input())
game5 = str(input())
game6 = str(input())

games_results = [game1, game2, game3, game4, game5, game6]

win_count = 0

for i in games_results:
    if i == 'W':
        win_count += 1

if win_count <= 0:
    print("-1")

elif win_count <= 2:
    print("3")

elif win_count <= 4:
    print("2")

else:
    print("1")

# finished in 8 minutes 25 seconds
