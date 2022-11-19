#union-find을 통해 공통 조상을 찾으면 어떨까??...
#고민, 어디서부터 탐색을 시작해야 하는 걸까?
#단방향 그래프 사이클 고민?

#반례 -> cycle이 있을때 어떻게 해야 할까?, union-find를 써도 될 법 하지만 한 번 dfs를 돌렸을때 나온 결과물을 모두 넣는다.
#한 번에 해킹할 수 있는 컴퓨터의 번호를 출력한다는 뜻 -> 그 컴퓨터로 시작해서 탐색 걸었을 떄 몇 개의 컴퓨터를 해킹할 수 있는지 적는다.
#계속 꼬였던 이유가 유사 DP를 하려고 시도해서 그런 것! 그냥 탐색만 쭉 해주면 됨.

#파이썬으로 풀었을때 dfs는 죄다 시간초과가 난다.
#심지어 정답 코드를 긁어 넣었는데도 pypy/python 다 시간초과가 난다 ㅠㅠ 따라서 dfs 대신 bfs를 사용해보자~
#습득한 부분: 후가공이 아니라 입력 받으면서 배열 처리하는 법(인접 행렬 만드는 법), bfs에서 visited 만들어서 한다는 거, set로 안하고 하나씩 돌면서 bfs 넣어주는 거,
#테세우스의 배마냥 정답 갈아끼우기를 하면서 쓴 답이다.
'''
딘축한 부분 
1) sys로 입력 처리
2) def sol 없애고 구문 안에 넣음
3) bfs에 인자로 arr 전달 안하고 전역변수 갖다쓰듯이 씀
4) 원래 제로인덱싱 때문에 하나씩 뺴서 썼는데 연산 줄이려고 제로인덱싱 처리 안함
5) 마지막 print에 print(*arr) 이렇게 한거 반복문으로 바꿈
6) 원래 입력 다 받고 전처리해서 인접리스트 만들어줬는데 입력 받으면서 바로바로 만듬

를 하니까 코드도 에뻐지고 통과도 했다. 참고로 이문제 dfs로는 파이썬으로 절대 못 풀 듯... 시간초과 이슈 ㅠㅠ
'''

from collections import deque
import sys

r = sys.stdin.readline

N, M = map(int, r().split())
arr = [[] for _ in range(N+1)]

def bfs(target):

    queue = deque([target])
    visited = [False] * (N+1)
    visited[target] = True

    count = 1

    while queue:
        v = queue.popleft()
        for node in arr[v]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                count += 1

    return count


for _ in range(M):
    a, b = map(int, r().split())
    arr[b].append(a)

answer = []
max_hack = -1
for i in range(1, N+1):
    result = bfs(i)

    if result > max_hack:
        answer = [i]
        max_hack = result
    elif result == max_hack:
        answer.append(i)

for a in answer:
    print(a, end=" ")




''' 전체 풀이

import sys
from collections import deque

r = sys.stdin.readline

def dfs(arr, start, visited, answer):

    visited[start] = True
    answer[0] = answer[0] + 1

    for i in arr[start]:
        if visited[i] == False:
            dfs(arr, i, visited, answer)

def bfs(arr, visited, target):

    queue = deque([target])
    answer = 1

    while queue:
        prev = queue.popleft()

        for node in arr[prev]:
            if visited[node] == False:
                queue.append(node)
                visited[prev] = True
                answer = answer + 1

    return answer


def sol(cnum, tarr):
    # [A, B] -> A가 B를 신뢰한다. => B를 해킹하면 A도 해킹할 수 있다.

    hack_arr = tarr
    # p_arr[i]는 i번째 사람의 부모를 뜻한다.

    answer = []
    max_hack = -1

    for i in range(cnum):
        visited = [False] * cnum
        visited[i] = True
        # visited_count = [0]
        # dfs(hack_arr, i, visited, visited_count)
        # answer.append(visited_count[0])
        # if visited_count[0] > max_hack :
        #     max_hack = visited_count[0]

        result = bfs(hack_arr, visited, i)

        if result > max_hack:
            answer = [i + 1]
            max_hack = result
        elif result == max_hack :
            answer.append(i + 1)

    return answer


N, M = map(int, r().split())
trust_arr = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, r().split())
    trust_arr[b-1].append(a-1)

print(*sol(N, trust_arr))

'''
