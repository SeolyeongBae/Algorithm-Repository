coins = [500, 100, 50, 10, 5, 1]

price = int(input())
ans = 0
target = 1000 - price

for i in range(len(coins)):
    ans += target // coins[i]
    target = target % coins[i]


print(ans)