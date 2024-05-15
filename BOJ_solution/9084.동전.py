# 문제 유형 : DP, 시간을 줄여야 하는데 어디서 줄일 수 있을까?
# 2차원 DP로 풀었는데 다른 풀이를 보니 1차원으로도 충분할 것 같다.

# values[0] ~ values[j]를 써서 i를 만들 수 있는 경우의 수는?
# 저거의 경우 이제 1, 2, 3원이 있으면 3원을 포함해서 만들 수 있는 경우의 수는 3원부터~를 하는 거구나
# 그러면 이 경우에 1, 2, 3,.... target을 만들 수 있는 수가 0, 1, 2일때 따지는 것인데
# 그럼 5를 만들 수 있는 경우는 5원이 있는경우부터는 안 세면 되겠구나!

def sol(values, target):
    dp = [[0 for _ in range(len(values))] for _ in range(target + 1)]

    # dp[i][j] 는 0번 ~ j번 동전까지 썼을 때 i를 만들 수 있는 경우의 수


    for i in range(target + 1):
        for j in range(len(values)):
            if i - values[j] >= 0:
                dp[i][j] = dp[i - values[j]][j] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j - 1]

            if i == values[j]:
                dp[i][j] = dp[i][j] + 1

    #2차원 디피를 해도 어느 일정 시점 전에 하면 더 일찍 끝낼 수 있는 듯?
    return dp[target][len(values) - 1]

t = int(input())
q = []

for _ in range(t):
    coin_types = int(input())
    coin_values = list(map(int, input().split()))
    target_value = int(input())
    q.append((coin_values, target_value))

for i in q:
    print(sol(i[0], i[1]))