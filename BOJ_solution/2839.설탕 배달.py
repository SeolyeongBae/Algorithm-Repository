#문제 유형 : DP
#목표 N킬로그램 배달할 경우 더 적은 개수의 봉지로 가져갈 수 있게 해야함
#3kg와 5kg가 있다.


def sol(s):

    dp = [2000, 2000, 1, 2000, 1]
    #dp[i] : i+1 킬로그램일때 들고갈수있는 가장 작은 봉투
    #dp[i] = min(dp[i-3], dp[i-5])
    #2000은 sys.maxsize 대신에 최댓값인 5000일대 3kg로만 하려면 어립잡아도 1800개 이상 해야해서 임의로 설정한 수

    if s < 5 :
        if dp[s-1] == 2000 : return -1
        else: return dp[s -1]

    for i in range(5, s):
        minimum = min(dp[i-3], dp[i-5]) + 1
        dp.append(minimum)

    if dp[s-1] >= 2000:
        return -1
    else:
        return dp[s - 1]

sugar = int(input())
print(sol(sugar))


# same solution 2023.ver -> 예전에 푼게 더 나아 보인다!!
# 근데 더 직관적으로 하면 3의 몫을 빼고 나머지를 5로 나눌수 있는가 보는 거인 듯
'''
N = int(input())

# 봉투는 3키로, 5키로가 있음
# 최적화 해야 하는 부분 -> 봉투의 수

dp = [-1, -1, -1, 1, -1, 1] #1부터 5까지, 1부터 인덱싱

# dp[i] = i키로그램을 담는 경우 필요한 최소 봉투의 수
# N >= 3

if N == 4 or N == 5:
    print(dp[N])

else:
    for i in range(6, N+1):
        if max(dp[i-3], dp[i-5]) == -1:
            dp.append(-1)
        else:
            if(dp[i-3] * dp[i-5] < 0):
                dp.append(max(dp[i-3], dp[i-5]) + 1 )
            else:
                dp.append(min(dp[i-3], dp[i-5]) + 1)
    print(dp)
'''