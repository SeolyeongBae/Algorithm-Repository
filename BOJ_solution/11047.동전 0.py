#문제 유형: 그리디
#5585번이랑 다른 점이 뭔지 모르겠음... 왜 난이도가 올라간 거지?

def sol(target, coins):

    coins.reverse()
    answer = 0

    for i in range(len(coins)):
        answer += target // coins[i]
        target = target % coins[i]

    return answer


[N, K] = list(map(int, input().split()))
coin_list = []

for _ in range(N):
    coin_list.append(int(input()))

print(sol(K, coin_list))
