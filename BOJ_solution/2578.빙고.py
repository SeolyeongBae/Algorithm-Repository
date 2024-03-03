#문제 유형: 구현, 시뮬레이션.
#전체 런타임을 따져 보니까 훨씬 많이 길다! 어떤 부분에서 더 줄일 수 있을까?


#좀 더 빠르게 하는 법
# 1. 파이썬의 all 함수 사용
# 2. 최소 3빙고 조건 : 12개 이상부터 3빙고 할 수 있음. 특정 횟수 이하는 아예 비교하지 않을 수도 있다. -> 이게 시간 줄이는 핵심 요소!

import sys

def check_bingo(bingo, call):


    r = [0 for _ in range(5)]
    c = [0 for _ in range(5)]
    d = [0, 0]
    for i in range(len(call)):
        f = 0

        for j in range(5):
            for k in range(5):
                if bingo[j][k] == call[i]:
                    r[j] += 1
                    c[k] += 1
                    if (j == k):
                        d[0] += 1
                    if (j + k == 4):
                        d[1] += 1
                    f = 1
                    break
            if f == 1:
                break

        if i < 11:
            continue

        if (r.count(5) + c.count(5) + d.count(5)) >= 3:
            print(i + 1)
            return


bingo = []
for _ in range(5):
    r = list(map(int, sys.stdin.readline().split()))
    bingo.append(r)

call = []
for i in range(5):
    r = list(map(int, sys.stdin.readline().split()))
    call = call + r

check_bingo(bingo, call)

