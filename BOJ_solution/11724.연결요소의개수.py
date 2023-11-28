import sys
sys.setrecursionlimit(100000)

# 틀렸던 이유 -> 6 0 케이스를 고려하지 않음
# 진짜 틀렸더 이유 -> 6 2 에서 그러면 자연스럽게 2개는 영구 고립임.
# 간선에 없는 node라면 아무 연결고리가 없다는 사실을 헷갈렸음. 다음에 이런 문제를 푼다면 가능한 테스트케이스를 조건을 보고 한번 생각해보고 문제를 풀어야겠다.

[M, N] = list(map(int, input().split()))
graph = {}

# M: 정점의 개수
# N : 간선의 개수

for _ in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 in graph:
        graph[n1].append(n2)
    else:
        graph[n1] = [n2]

    if n2 in graph:
        graph[n2].append(n1)
    else:
        graph[n2] = [n1]

#어떻게 풀까? dfs로 풀어보자.
def sol(graph):
    visited = [-1] * (M + 1)

    def dfs(node):
        if visited[node] == 0:
            return
        visited[node] += 1
        next = graph[node]
        for n in next:
            if visited[n] == -1:
                dfs(n)
        return

    ans = 0

    for k in range(1, M+1):
        if visited[k] == -1:
            ans += 1
            if k in graph:
                dfs(k)
    print(ans)


sol(graph)