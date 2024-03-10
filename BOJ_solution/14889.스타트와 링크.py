import sys
import itertools

#combination을 잘 쓰자... 1884msㅋㅋㅋ 망함

def sol(arr):

    minimum = 1001

    len_group = int(len(arr)//2)
    comb = [i for i in range(len(arr))]
    div = list(itertools.combinations(comb, len_group))
    div = div[:len(div)//2]

    for d in div:
        t = [0, 0]  # team 1, team2의 능력치
        r = list(set(comb) - set(d)) # comb에서 d 빼준애들
        for i in itertools.combinations(r, 2):
            t[0] += arr[i[0]][i[1]]
            t[0] += arr[i[1]][i[0]]

        for j in itertools.combinations(d, 2):
            t[1] += arr[j[0]][j[1]]
            t[1] += arr[j[1]][j[0]]

        comp = max(t[1] - t[0], t[0] - t[1])

        minimum = min(comp, minimum)

    return minimum


n = int(input())
arr = []
for _ in range (n):
    l = list(map(int,sys.stdin.readline().split()))
    arr.append(l)


print(sol(arr))

