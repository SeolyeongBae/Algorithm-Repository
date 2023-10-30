# 문제 유형: 누적합 근데 2차원인
# 1트 성공 -> 중요한 점 : 맨 처음 엘리먼트를 0으로 해서 1번째를 버퍼할 수 있는 게 필요했음.
import sys

def sol(arr, target):
    length = len(arr)

    s = [[0] * length for _ in range(length)]
    s[0][0] = arr[0][0]

    for i in range(1,length):
        s[i][0] = s[i-1][0] + arr[i][0]

    for i in range(1, length):
        s[0][i] = s[0][i-1] + arr[0][i]

    for i in range(1,length):
        for j in range(1, length):
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + arr[i][j]
    #2차원 누적합을 구하는 방법 - 0,0부터 i,j까지의 모든 요소의 합 이라는 뜻

    for t in target:
        [x1, y1, x2, y2] = t

        p1 = s[x2-1][y2-1]
        p2 = s[x2 - 1][y1 - 2]
        p3 = s[x1 - 2][y2 - 1]
        p4 = s[x1 - 2][y1 - 2]

        if x1 == 1:
            p3 = 0
            p4 = 0
        if y1 == 1:
            p2 = 0
            p4 = 0

        print(p1 - p2 - p3 + p4)
    return 0;

[n, m] = list(map(int, input().split()))

arr = []

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    arr.append(nums)

targets = []

for _ in range(m):
    coordinate = list(map(int, sys.stdin.readline().split()))
    targets.append(coordinate)

sol(arr, targets)