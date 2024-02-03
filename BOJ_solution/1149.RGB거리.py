# 시간 줄이기: dp = [[0,0,0]] 이렇게 여러 개 만들어놔서 0에 assign하는 것보다 새로운 array를 만들어 append하는게 더 빠름
# 시간 줄이기2 : 그래도 sys.stdin.readline을 넣는게 가장 빠르다.

import sys
input = sys.stdin.readline

def sol(arr):
    house_count = len(arr)

    dp = [arr[0]]

    for i in range(1, house_count):
        prev = dp[i-1]
        arr_next = [min(prev[1], prev[2]) + arr[i][0],  min(prev[0], prev[2]) + arr[i][1],  min(prev[0], prev[1]) + arr[i][2]]
        dp.append(arr_next)

    return min(dp[-1])


N = int(input())
h = []
for _ in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    h.append(t)

print(sol(h))
