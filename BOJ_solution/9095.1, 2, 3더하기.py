#실버 3
#딱 봐도 DP
#살짝 동전 느낌??인데 순서바꾼게 허용돼서 쉽다.
#근데 11까지면 그냥 사람 손으로 11까지 구한 어레이 만드는게 더 쉬울듯 -> 근데 틀렸다! -> print문을 엉뚱한데 써놔서 틀렸다.

def sol(nums):

    dp = [1, 2, 4]

    for n in nums:
        if n <= len(dp):
            print(dp[n-1])
        else:
            for _ in range(len(dp), n):
                l = len(dp) - 1
                sums = dp[l] + dp[l-1] + dp[l-2]
                dp.append(sums)

            print(dp[-1])
    return

T = int(input())
nums = []
for _ in range(T):
    i = int(input())
    nums.append(i)

sol(nums)

