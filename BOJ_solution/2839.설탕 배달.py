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