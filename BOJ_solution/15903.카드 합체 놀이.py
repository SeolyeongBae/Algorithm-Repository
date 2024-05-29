# 문제 유형: 그리디, 자료구조?
# list에서 heap을 쓰니까 188ms -> 52ms로 시간이 크게 줄었다. 자료구조에 대한 이해가 필요했다.

import heapq

def sol(n, m , cards):

    #card의 두 수를 더하고, 더한 값을 덮어씌운다 -> 즉 그 값이 복사가 돼서 2개가 된다!!!
    # 3, 5가 있으면 8이 되고 8, 8이 된다
    # 최소가 되기 위해서는 가장 작은 값을 많이 쓰게 해야한다.

    # 그리디? DP? -> 이 경우에는 그리디하게 푸는게 좋아 보임.
    # m: 카드를 합체하는 횟수



    #가장 naive하게 하는 법: 그리디하게, 매번 뽑고 다시 넣음.
    #sort 에서 많이 시간이 걸리는것 같다!

    # cards.sort()
    # for i in range(m):
    #     card1 = cards.pop(0)
    #     card2 = cards.pop(0)
    #
    #     cards = cards + [card1+card2] * 2
    #     cards.sort()

    #조금 더 빠르게 하는 법: heap을 쓴다.
    heapq.heapify(cards)

    for i in range(m):
        c1 = heapq.heappop(cards)
        c2 = heapq.heappop(cards)

        heapq.heappush(cards, c1 + c2)
        heapq.heappush(cards, c1 + c2)


    return sum(cards)
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(sol(n, m, arr))