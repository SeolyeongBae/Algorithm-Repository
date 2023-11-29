import sys
from collections import deque

N, M = map(int, input().split())
padding = '0' * (M+2)
arr = [padding]

for _ in range(N):
    a = '0' + str(sys.stdin.readline().split()[0]) + '0'
    arr.append(a)

arr.append(padding)
# 패딩 추가

# 목표: 1,1에서 N, M으로 이동할 수 있는 최소의 경우

# dfs, bfs?
visited = [[-1 for j in range(M + 2)] for i in range(N + 2)]
visited[1][1] = 0

def bfs(m):
    queue = deque([[1, 1]])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        prev = queue.popleft()
        [x, y] = prev

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if m[nx][ny] == '1':
                if visited[nx][ny] == -1:  # 방문 안했을 경우
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    return 0


bfs(arr)
print(visited[N][M] + 1)
