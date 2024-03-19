#헤맸던 부분은... dfs를 잘못 짠것 같다....
#그래도 기본적인 아이디어는 맞았던 것 같다.
#물에 잠긴 경우에는 -1을 저장해서 아예 접근하지 않도록 했는데 그 부분이 문제를 일으킨 것 같은 느낌이 든다...
#그리고 재미있는 건, 1부터 100까지 모두 돌면 시간이 많이 거리니까 set을 이용해서 탐색할 높이를 줄여줬는데 set 생성하는 시간이나 1부터 100까지 도는 시간이나
#크게 다를 게 없었다.


import sys
sys.setrecursionlimit(100000)


# 나의 전제: 안전 영역은 점차 증가 한다(반례가 있을까?)그러다가 감소하는 순간을 return 하면 된다.
# 백트래킹으로 생각했을떄

def dfs(arr, visited, i, j, target):

    up = (i-1, j)
    down = (i+1, j)
    left = (i, j-1)
    right = (i, j+1)
    stack = [up, down, left, right]

    for s in stack:
        r = (s[0] < 0 or s[1] < 0 or s[0] > len(arr) - 1 or s[1] > len(arr) - 1)
        if not r:
            v = visited[s[0]][s[1]]
            b = arr[s[0]][s[1]] > target
            if (not v) and b:
                visited[s[0]][s[1]] = True
                dfs(arr, visited, s[0], s[1], target)

def sol(arr, s):
    m = 1
    l = len(arr)

    # 제일 작은놈이 부모인 그래프를 만들고, 거기 기준으로 깊이우선탐색을 한다.
    for rain in s:
        visited = [[False for _ in range(l)] for _ in range(l)]
        head = []
        # s로부터 강수량을 꺼낸다.

        for i in range(l):
            for j in range(l):
                if not visited[i][j] and arr[i][j] > rain:  # 이미 방문했거나 침수된 경우
                    head.append((i, j)) #물에 안 잠긴 구역을 탐색
                    visited[i][j] = True
                    dfs(arr, visited, i, j, rain)
        m = max(m, len(head))
    return m


n = int(input())
arr = []
t = set({})
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)
    t = t | set(a)

print(sol(arr, t))
