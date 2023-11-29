# 3차원 탐색??
# bfs로 탐색할떄 가장 큰 값
# 이 문제의 경우 패딩을 깔면 안된다. 53번째 줄의 코드를 쓰는 게 너무 싫었는데 그냥 나의 고집이었다. 패딩을 만들면 시간도 많이 걸리고 메모리도 많이 잡아먹는다.
# 좀 시간이 걸렸던 부분은 3차원 배열의 max값을 찾는 거였다. 그냥 정석적으로 max 만들어주는게 가장 좋은 방법 같다.
# 런타임이 상위 50%인데 어느 부분에서 내가 향상할 수 있을까?
'''
 for i in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            if (0 <= a+i[0] <= h-1) and (0 <= b+i[1] <= n-1) and(0 <= c+i[2] <= m-1):
같은 식으로 미리 여러 set을 만드들어놔서 계산하는 시간을 줄여볼 수 있다.
가장 큰 개선할 수 있는 방법은 visited array를 쓰지 않고 while 한 사이클마다 count를 증가시키는 방법이다!
한 번 while이 돌때마다 익은토마토 근처 토마토들이 큐에 들어가는 거니까 하루가 지난 거랑 같은 논리다.
토마토 익으면 익은토마토로 바꿔서 visited array를 대체할 수 있다.
'''

# 0: 토마토, 1: 익은토마토, -1: 토마토없음
import sys
from collections import deque

M, N, H =map(int, input().split())

# M : 가로칸수
# N: 세로칸수

arr = []
tomato = []

for h in range(H):
    b = []
    for k in range(N):
        a = list(map(int, sys.stdin.readline().split()))
        t = []
        for i in range(M):
            if a[i] == 1:
                t.append(i)
        tomato += [[h, k, i] for i in t]
        b.append(a)
    arr.append(b)

visited = [[[-1 for j in range(M)] for i in range(N)] for k in range(H)]


for t in tomato:
    z, x, y = t
    visited[z][x][y] = 0

def bfs(m):
    queue = deque(tomato)
    count = 0

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while queue:
        prev = queue.popleft()
        [z, x, y] = prev

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx >= N or nx < 0 or ny >=M or ny<0 or nz >=H or nz < 0:
                continue
            if m[nz][nx][ny] == 0:
                if visited[nz][nx][ny] == -1:  # 방문 안했을 경우
                    visited[nz][nx][ny] = visited[z][x][y] + 1

                    if visited[nz][nx][ny]> count:
                        count = visited[nz][nx][ny]

                    m[nz][nx][ny] = 1 # 토마토 익음!
                    queue.append([nz, nx, ny])
                # 이미 방문 했을 경우, 현재의 값이 더 작으면 갱신한다.

    return count


ans = bfs(arr)

for k in arr:
    for j in k:
        for i in j:
            if i == 0:
                print(-1)
                exit(0)

print(ans)
