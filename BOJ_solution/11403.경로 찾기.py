#문제 유형: 탐색? 모든 지점에 대해서 dfs 탐색을 돌렸다.
#기존에 터졌던이유 -> 브루트포스를 해버려서?

import sys

def sol(arr):

    l = len(arr)
    answer = [[0 for _ in range(l)] for _ in range(l)]

    for src in range(l):
        stack = [src]
            #src랑 이어져 있는애들 다 탐색한다. 기존에 이 방법을 node 하나씩이 아니라 모든 src, dest로 해서 시간초과가 됐다.

        while stack:
            t = stack.pop()


            for i in range(l):
                if arr[t][i] == 1 and answer[src][i] == 0:
                    # arr[t][i] == 1은 t -> i가 이어져 있다는 의미다. answer[src][i] == 0은 아직 업데이트 안됐다는 것.
                    answer[src][i] = 1 # 출발점이 src고, 지금 stack에 들어 있던 값은 src에서 접근할 수 있는 값이다. 따라서 src -> i도 연결되어 있다. (1이다)
                    stack.append(i) # i를 넣어준다.

    return answer


n = int(input())
arr =[]

for _ in range(n):
    r = list(map(int,sys.stdin.readline().split()))
    arr.append(r)

for r in sol(arr):
    print(*r)
