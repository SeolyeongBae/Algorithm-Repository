# 문제 유형은 DP, 생각한 풀이 방법도 맞았지만 구현 과정에서 좀 어려움을 겪었음...
# 또 문제 조건을 잘 생각해서 어렵지 않은 엣지케이스 정도는 생각해보자. 이번의 경우 vip가 없는 경우, 긔고 모든 좌석이 vip인 경우를 따졌어야 했다.
# 아이디어는 맞았지만 구현이 어려웠다. 급하게 풀지 말자.

# 훨씬 더 쉬운 방법: vip 사이의 간격을 그냥 vip[i+1] - vip[i] - 1로 구할 수 있다 ㅎㅎㅎ ... 이걸 몰라서 fixed로 하느라 큰 고난을 겪었다.
# array에서 pop하는 apporach를 한다면 꼭 empty인지 확인해주자
# 테크닉: person_cnt = [j - i - 1 for i, j in zip(vips[:-1], vips[1:])]
# 처럼 [0, 4, 6, 8] 를 [0, 4, 6] 와 [4, 6, 8]로 나눠서 빼주는 식..!! 대박 :)

import sys


def sol (N, fixed):
    fixed.sort()
    fixed.reverse()
    k = -1
    arr = [(i+1) for i in range(N)]
    counts = []
    count = 0


    if len(fixed) != 0:
        k = fixed.pop()
        for i in range(N):
            count += 1
            # 투포인터?
            if arr[i] == k:
                if count >= 2:
                    counts.append(count - 1)
                count = 0

                if len(fixed) == 0:
                    counts.append(len(arr) - i - 1)
                    break
                k = fixed.pop()

    else:
        counts.append(len(arr))

    m = max(counts)

    dp = [0 for _ in range(m)]

    if m > 1:
        dp[0] = 1
        dp[1] = 2

    if m > 2:
        for i in range(2, m):
            dp[i] = dp[i - 1] + dp[i - 2]  # 자리를 안 바꿀 경우 + 자리를 바꿀 경우

    answer = 1
    for c in counts:
        # 나눠진 개수만 구할 수 있다면 그게 무슨 수인지는 상관없다...
        # 이 문제에서 연속으로 뒤바뀌는 것은 불가능하므로 2명이 서로 짝을 짓는다고 할 때 그 경우의 수를 묻는 것이다.
        # 그럼 짝이 1개 있는 경우, 2개 있는 경우, 3개 있는 경우... c//2개 있는 경우가 가능하다.
        # dp로 풀면 동전쌓기랑 똑같다.
        if c <= 1:
            continue

        answer = answer * dp[c-1]
    return answer

N = int(input())
M = int(input())
fixed = []

for _ in range(M):
    f = int(sys.stdin.readline())
    fixed.append(f)

print(sol(N, fixed))