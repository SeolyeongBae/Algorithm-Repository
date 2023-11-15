# 유형 : 이분탐색 - 이분탐색을 1부터 최대 길이의 range에서 했을 때 그래프의 교점을 찾는 문제
# 에러: zerodivision err - 시작을 1이 아니라 0으로 해서 발생한 오류 같다.

import sys

def sol (arr, N):
    arr.sort()
    s = 1
    e = arr[-1] #제일 큰 값

    answer = 0

    while s <= e:
        total = 0
        mid = (s + e) // 2

        for a in arr:
            total += (a // mid)

        if total >= N:
            s = mid + 1
            answer = mid
        else:
            e = mid - 1

    print(answer)
    return 0

[K, N] = list(map(int, input().split()))
lines = []

for _ in range(K):
    n = int(sys.stdin.readline())
    lines.append(n)

sol(lines, N)