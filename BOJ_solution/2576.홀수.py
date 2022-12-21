sums = 0
minimum = 101

for _ in range(7):
    temp = int(input())
    if temp % 2 == 1:
        sums += temp

        if minimum > temp:
            minimum = temp

if sums == 0 : print(-1)
else :
    print(sums)
    print(minimum)