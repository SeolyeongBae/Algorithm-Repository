#문제 유형: DP지만 브루트포스로 해결했다.

import sys


def sol(way, target):
    k = list(way.keys())
    k.sort()
    dp = [i for i in range(target + 1)]
    #dp[i]는 i까지 가는데 걸리는 최소시간

    for i in range((target + 1)):
        dp[i] = min(dp[i-1]+1, dp[i])
        # 전에는 지름길이 없을 경우를 따로 핸들링해다. dp 풀이에서는 위 코드로 처리해주고 있기 때문에 특별히 안 해줘도 된다!

        if i in way:
            for w in way[i]:
                dp[w[0]] = min(dp[i] + w[1], dp[w[0]])
                # w[0]은 i에서 갈 수 있는 지름길의 목적지
                # 기존의 값이랑 dp[i]에서 지름길로 간 거랑 어디가 더 빠른지 비교해서 저장.
    return dp[target]

'''
브루트포스 풀이

전체 지름길 없는 경우 찾았던 반례
3 100
0 50 100
0 60 100
20 30 5
지름길이 전부 유효하지 않은 경우, 20을 넣지 않는다.

def sol(way, target):
    #브루트포스 -> 0.6초 걸림

    k = list(way.keys())
    k.sort()
    stack = [0]

    cost = [i for i in range(target + 1)] #cost[i] 는 i(m) 까지 가는데 드는 거리
    cost[0] = 0

    while stack:
        t = stack.pop() # t는 도로의 인덱스
        # 근데 이 문제에서는 한 간선에서 다른 간선으로 가는 방법이 2가지 이상이다... visited array를 쓰는게 의미가 있을까?
        cost[D] = min(cost[D], cost[t] + D - t)

        if t in way: #만약 t에 지름길이 존재하는 경우 -> 근데 지름길이 전부 일반 길보다 길어지면 어떡할까?
            for w in way[t]:
                # w는 t에서 갈 수 있는 지름길, (dest, cost) 튜플 형태
                # 지름길이 일반 길보다 더 길 수도 있다.
                stack.append(w[0]) #도착지를 다음 출발지로 추가
                cost[w[0]] = min(cost[w[0]], cost[t] + w[1]) #w[0] 까지 갈떄까지의 최소 거리를 계산
                cost[D] = min(cost[D], cost[w[0]] + D - w[0])

        #지름길을 선택하지 않고 전부 방문하는 경우
        for i in range(len(k)):
            if k[i] > t:
                stack.append(k[i])
                cost[k[i]] = min(cost[k[i]], cost[t] + (k[i] - t)) # 여기가 틀린것 같은데? 아니네 맞네...
                cost[D] = min(cost[D], cost[k[i]] + D - k[i])

    return cost[D]
'''


N, D = list(map(int, input().split()))
way = []
adj_list = {}

for _ in range(N):
    r = list(map(int,sys.stdin.readline().split()))
    #시작 위치, 도착 위치, 지름길의 길이
    if r[0] <=D and r[1] <= D:
        if r[0] in adj_list:
            adj_list[r[0]].append((r[1], r[2]))
        else:
            adj_list[r[0]] = [(r[1], r[2])]

    #고속도로는 역행이 불가능하므로 뒤에 거는 저장하지 않는다.


print(sol(adj_list, D))