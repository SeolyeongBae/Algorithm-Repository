# 문제 유형: 구현?
# 유니온 파인드를 사용해서 해결했다. 이어져 있으면 방문할 수 있다는 뜻이고, 결국 같은 부모를 가진다는 뜻인 듯.
# 급하게 코드를 써서 처음에 틀렸는데 침착하게 다시 푸니까 됐다.

import sys

N = int(input())
M = int(input())

def find(arr, i):
    if arr[i] == i :
        return i
    else:
        arr[i] = find(arr, arr[i])
        return arr[i]

def merge(arr, i, j):
    i = find(arr, i)
    j = find(arr, j)

    if i == j :return i
    if i > j:
        arr[i] = j
    else:
        arr[j] = i

def sol(N, travel, plan):
    par = [i for i in range(N)]

    for i in range(len(par)):
        find(par, i)

    #인접리스트 처리를 해줘야함...
    for i in range(len(travel)):
        t = travel[i]

        for j in range(len(t)):
            if t[j] == 1:
                merge(par, i, j)

    for i in range(len(plan) -1):
        if par[plan[i] -1 ] != par[plan[i+1] -1 ]:
            return 'NO'
    return 'YES'

travel = []

for _ in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    travel.append(t)

plan = list(map(int, sys.stdin.readline().split()))
print(sol(N, travel, plan))