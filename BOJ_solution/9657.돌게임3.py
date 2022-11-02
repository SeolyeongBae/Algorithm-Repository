#문제 유형: DP

# 1, 3, 4개 가져갔을때 필승 전략은 무엇일까?


# 1일때 1 - 상근
# 2일때 1 1 - 창영
# 3일떄 3 - 상근
# 4일때 4 - 상근
# 5일때 3 - 1 - 1  - 상근
# 6일때 4 - 1 - 1 - 상근
# 7일때 1 - 4 - 1 - 1 - 창영
# 8일떄
    # 1을 한다면 6일째 - 3번 -> 필패
    # 3을 한다면 5일때 - 3번 -> 필패
    # 4를 한다면 4일째 - 1번 -> 필패

def sol(g):
    #상근이가 짝수 인덱스. 창영이가 홀수 인덱스
    dp = [0, 1, 0, 1, 1]

    if g < 5:
        if dp[g] == 0:
            return "CY"
        else:
            return "SK"

    #dp값이 홀수면 SK, 짝수면 CY
    for i in range(5, g+1):
        if dp[i-1] == 1 and dp[i-3] == 1 and dp[i-4] == 1:
            dp.append(0)
        else:
            dp.append(1)

    if dp[g] == 0:
        return "CY"
    else:
        return "SK"


goal = int(input())

print(sol(goal))
