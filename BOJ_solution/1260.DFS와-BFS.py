#탐색
#인접 리스트를 딕셔너리로 쓰고자 발악한 자의 최후..
#dfs를 재귀적으로 하는 걸 잠시 잊어버린 듯 했다
#맹점 : append 하고 sort를 안했었다.

from collections import deque

def dfs(start, graph):

    visted_dfs[start] = True
    stack = graph[start][:]

    print(start, end=' ')

    # graph[start].remove(graph[start][0])
    # graph[stack[0]].remove(start)
    # 간선 제거 할필요 없음!

    for i in stack:
        if not visted_dfs[i]:
            dfs(i, graph)


def bfs(start, graph):
    print('\n', end = '')
    visted_bfs[start] = True
    q = deque([start])
    while q :
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visted_bfs[i]:
                q.append(i)
                visted_bfs[i] = True

input_list = list(map(int, input().split()))
dic = {}

for i in range(1,input_list[0]+1):
    dic[i] = []

for i in range(input_list[1]):
    line_list = list(map(int, input().split()))

    dic[line_list[0]].append(line_list[1])
    dic[line_list[1]].append(line_list[0])


    dic[line_list[0]].sort()
    dic[line_list[1]].sort()

visted_dfs = [False] * (input_list[0]+1)
visted_bfs = [False] * (input_list[0]+1)

print(dic)

dfs(input_list[2], dic)
bfs(input_list[2], dic)
#print(bfs(input_list[0],input_list[2], dic))
    
