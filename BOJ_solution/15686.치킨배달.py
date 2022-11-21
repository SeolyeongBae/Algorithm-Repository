#카테고리: 구현
#시작 시간: 밤 11시
#두려운 점: 시간초과!?
#1차 시도: 틀림, 아마도 틀린 이유는 나름의 오류처리인데 이럴 경우에는 빨리하겠다고 오류처리할게 아니고 걍 일반화하는게 좋은것 같음.
#푼 시간: 1시간

import sys
from itertools import combinations

def sol(cmap, cpos, hops, survival) :
    cnum = len(cpos)
    h_arr = [[0 for _ in range(cnum)] for _ in range(len(hops))]
    #h[i][j] : i번 집이 j번째 치킨집에 대한 치킨거리


    for i in range(cnum):
        col_val = cpos[i][0]
        row_val = cpos[i][1]
        for j in range(len(hops)):
            dir = abs(col_val - hops[j][0]) + abs(row_val-hops[j][1])
            h_arr[j][i] = dir

    clist = list(range(cnum))
    try_list = list(combinations(clist, survival))

    minimum = sys.maxsize

    for i in try_list:
        #한 가지가 뽑히는 조합 구현
        total = 0
        for h in h_arr:          #한 집에서 최소 치킨 거리를 계산하기
            local_minimum = 5000
            for j in i:
                if h[j] < local_minimum:
                    local_minimum = h[j]
            total = total + local_minimum

        if minimum > total :
            minimum = total
    return minimum



N, M = map(int, input().split())
chicken_map = []
house_pos = []
chicken_pos = []

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(N):
        if row[j] == 2:
            chicken_pos.append((i, j))
        if row[j] == 1:
            house_pos.append((i, j))
    chicken_map.append(row)

print(sol(chicken_map, chicken_pos, house_pos, M))