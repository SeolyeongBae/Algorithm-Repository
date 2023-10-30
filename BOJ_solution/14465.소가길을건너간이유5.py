# 유형 : 누적합
# 슬라이딩 윈도우라는 문제에서 힌트를 얻었다!
# 누적합으로 k번 횡단보도까지의 멀쩡한 신호등의 개수를 센다.
# 그리고 i번부터 i+K 사이의 누적합을 구하고, 목표하는 수치와 얼마나 차이나는지 계산한다
# 최솟값을 저장하면 그게 곧 답이다.

import sys

def sol(N, K, arr):

    nums = [1] * N

    for a in arr:
        nums[a-1] = 0

    s = [nums[0]]


    for i in range(1, N):
        s.append(s[i-1] + nums[i])

    minimum = 100001

    for i in range(N - K + 1):
        start = i
        end = i + K - 1

        val = s[end] - s[start] + nums[start]

        if (K - val) < minimum : minimum = K - val

    print(minimum)
    return 1

[N, K, B] = list(map(int, input().split()))
# 1 <= B, K <= N

arr = []

for _ in range(B):
    n = int( sys.stdin.readline())
    arr.append(n)


sol(N, K, arr)