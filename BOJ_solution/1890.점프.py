#문제 유형: DP

import sys

#목표: 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프해서 감
#각 칸의 수는 현재 칸에서 갈 수 있는 거리를 의미, 반드시 오른쪽이나 아래쪽으로만 이동해야 함.
#무조건 적혀 있는 수 만큼 오른쪽이나 아래로 가야 한다.
#알맞게 이동 가능한 경로의 개수를 구하는 프로그램을 작성하시오.

# 일단 (i, j)에 도착하면 가로줄, 세로줄 검증을 거쳤다.
# 그러나 더 발리 푸는 법으로는... 방문할 떄 그냥 더해버리는 것이다. 그냥 i, j 탐색 방향을 맞춰 놓으며는 최적해의 합이 최적해가 된다...
'''
        if j+board[i][j] < N:
            visited[i][j+board[i][j]] += visited[i][j]
        if i+board[i][j] < N:
            visited[i+board[i][j]][j] += visited[i][j]
            이런 식으로 해볼 수 있다.!!
'''

def sol(game):
    n = len(game)
    total = [[0 for _ in range(n)] for _ in range(n)]
    total[0][0] = 1

    #세로 (위 -> 아래 방향을 따지고)
    #이게 dp인가?? dp라기에는 너무 별론데

    #row_dir
    for i in range(n):
        for j in range(n):
            if (i < game[0][0] and j < game[0][0]) and (i !=0 or j!=0):
                total[i][j] = -1
                continue

            for k in range(0, i):
                #세로 줄 검증
                if game[k][j] == i - k and total[k][j] > 0:
                    total[i][j] += total[k][j]
            for k in range(0, j):
                #가로 줄 검증
                if game[i][k] == j - k and total[i][k] > 0:
                    total[i][j] += total[i][k]

            #game[i][j]에 도달할 수 있는 방법 수를


    return total[-1][-1]

n = int(input())
game =[]
for _ in range(n):
    g = list(map(int, sys.stdin.readline().split()))
    game.append(g)

print(sol(game))