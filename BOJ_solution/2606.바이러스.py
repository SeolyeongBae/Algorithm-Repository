#문제 유형 : 탐색
#문제 푸는 목적 : bfs 연습
#약간 1325번 하위호환 문제, 대신에 방향이 없는 그래프다.

from collections import deque


def bfs(arr, visited, target):

    queue = deque([target])
    #queue = Queue()를 써도 되긴 함 근데 while 조건문이 (not q.empty()) 요거가 된다...

    while queue:
        prev = queue.popleft()
        graph = []

        for i in range(len(arr[prev])):
            if arr[prev][i] == 1 and visited[i] == False:
                graph.append(i)

        if visited[prev] == False:
            visited[prev] = True
            queue += set(graph)


def sol(cnum, arr):
    #인접 행렬을 만든다 -> 방향이 없기 때문에

    adj_arr = [[0 for _ in range(cnum)] for _ in range(cnum)]
    for p in arr:
        first = p[0] -1
        second = p[1] -1

        adj_arr[first][second] = 1
        adj_arr[second][first] = 1

    visited = [False] * cnum

    bfs(adj_arr, visited, 0)


    answer = 0
    for i in visited :
        if i == True:
            answer = answer + 1
    return answer -1



cnum = int(input())
pair_num = int(input())
pairs = []
for _ in range(pair_num):
    pair = list(map(int, input().split()))
    pairs.append(pair)

print(sol(cnum, pairs))