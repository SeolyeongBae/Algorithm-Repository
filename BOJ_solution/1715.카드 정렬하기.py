#시작 시간: 10시 30분
from heapq import heappush, heappop
def sol(c):
    ans = 0

    while(len(c) > 1):
        t = heappop(c)
        s = t + heappop(c)
        ans += s

        heappush(c, s)
    return ans


N = int(input())
cards = []

for _ in range(N):
    heappush(cards, int(input()))


print(sol(cards))



'''
#naive한 풀이

def sol(c):
    ans = 0
    while(len(c) > 1):
        c.sort()
        c.reverse()

        t = c[-1]
        c.pop()
        ans += t + c[-1]
        c[-1] = t + c[-1]

    return ans
'''