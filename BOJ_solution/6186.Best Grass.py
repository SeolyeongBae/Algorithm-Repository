# 문제 유형: 탐색... 이지만 그냥 구현으로도 풀 수 있다. 하지만 dfs로 한번 풀어보도록 하겠다.
# 처음에 입력 받을때 #의 위치를 미리 target 라는 array에 튜플로 저장한다.
# 그 다음에 target 에 있는 튜플을 가지고 하나씩 dfs를 돌린다. 즉 해당 잔디가 있는 잔디뭉치를 한꺼번에 하나로 센다. 센 잔디는 visited를 True로 돌린다.
# 이때 target에 있는게 정상적으로 pop 됐을때 (방문하지 않은 경우)에만 값이 1 더해진다.

def sol(arr, target, n, m):
    #n : rows
    #m: columns

    visited = [[False for _ in range(m)] for _ in range(n)]
    ans = 0

    for t in target:
        if visited[t[0]][t[1]]:
            continue

        stack = [t]
        ans += 1

        while stack:
            cur = stack.pop()
            visited[cur[0]][cur[1]] = True
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]

                if (not (nx < 0 or nx > n-1 or ny < 0 or ny > m-1)) and not visited[nx][ny] and arr[nx][ny] == '#':
                    stack.append((nx, ny))
    return ans

n, m = list(map(int, input().split()))
grass = []
target = []

for i in range(n):
    g = input()
    grass.append(g)
    for j in range(m):
        if g[j] == '#':
            target.append((i, j))

print(sol(grass, target, n, m))