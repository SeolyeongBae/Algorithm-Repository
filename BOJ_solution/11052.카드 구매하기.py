#문제를 그리디라고 생각해서 풀었는데 틀렸음!
# DP로 풀면 된다.
'''
반례
5
1 9 18 25 1

'카드 1개 대비 가격'이 높은 순으로 따지면 25, 1을 사면 26이 나온다.
근데 사실은 18 + 9를 사면 27이라서 이게 더 목표에 맞다.
헉.

'''

#총 8가지의 카드
#카드 n개가 포함된 카드팩 .. N가지
#돈을 최대한 많이 지불해서 카드를 N장 산다

def sol(arr):

    target = len(arr) #총 n개를 구입해야 한다

    dp = [0 for _ in range(target + 1)]
    #dp[i] 는 i개를 구매하는 최댓값.
    #arr[i-1]은 i-1 개를 샀을때의 가격
    dp[1] = arr[0]

    for i in range(2, target + 1):
        # 시간을 더 줄이려면... 1부터 i+1 대신에 (i//2) + 1까지 해도 된다
        # 이 코드에서는 5를 보는 경우 dp[3] + 2개구매, dp[2] + 3개구매 같은 경우를 따지게 되는데, 이런 경우에는 1~ i+1를 봐야 한다.
        # 하지만 dp[3] + dp[2] 라고 생각하면 어떨까? 최댓ㄷ값끼리 더하는 것이므로 상당히 합리적이다.
        # 그렇게 되면 절반만 해도 된다.
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i-j] + arr[j-1])

        #3개 사는경우 = 3개짜리, 2개짜리 + 1개짜리, 1개짜리 3개. 어떤게 더 클까?
        # -> 하지만 위는 잘못된 사고. 2개짜리 + 1개짜리, 1개짜리 + 2개짜리 경우로 생각해야 한다.
        # 1개짜리 3개를 생각한 건 납득이 되지만, 이렇게 풀면 DP적 사고가 어렵다!

    return dp[-1]

    # 나눌수있는 베낭문제인데?
    # 틀린 풀이 : 그리디
    # ratio = [((arr[i] / (i+1)), i) for i in range(target)]
    # ratio.sort(key=lambda r: -r[0])
    #
    # ans = 0
    # total = target #지금 사야하는 카드 수
    #
    #
    # for i in range(target):
    #     amount = ratio[i][1] + 1
    #     price = ratio[i][0]
    #
    #     if total < amount:
    #         continue
    #
    #     tmp = (total // amount) * amount
    #
    #     total -= tmp
    #     ans += price * tmp

    return int(ans)

n = int(input())
cards = list(map(int, input().split()))

print(sol(cards))
