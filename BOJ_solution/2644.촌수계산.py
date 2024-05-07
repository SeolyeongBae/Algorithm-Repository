import sys

# bfs를 활용한 풀이 -> 많이 느리다.
# 예외가 존재하는가? 일단 한 사람의 부모는 한명이라고 문제 조건에서 걸었다.
# cycle이 생기는 것도 불가능하다.
# 이때 숫자의 대소에 따라서 누가 더 촌수가 높은지 구별하는 것은 불가능하다.
# 탐색을 해서 더 cost가 작은 쪽으로 결정하는 게 좋은 것 같다.
# 여기서는 bfs를 해보자.

# 시간이 다른 풀이에 비해 많이 걸리는 편이었는데, collections에서 deque를 import해오는 데 시간이 많이 걸렸던 것이다..!!
# 파이썬에서 queue를 쓰는 방법에 무조건 collections를 import하지 않고, pop(0) 이라는 메서드를 통해도 구현이 가능하다는 것을 알았다.


def sol(nums, target, adj_list):
    ans = [0] * (nums + 1) # 탐색 한번 했을때 촌수

    q = [target[0]]

    while(q):
        t = q.pop(0)
        ans[t] += 1

        adj_nodes = adj_list[t]

        for n in adj_nodes:
            if n == target[1]:
                return ans[t]
            if ans[n] == 0:
                q.append(n)
                ans[n] = ans[t]

    return -1

'''

# 촌수 계산하는 법 -> 공통된 조상까지 갈때 걸리는 길을 재는 형식으로 했다. 유니온-파인드 같은 접근으로 풀이한 듯.
# x의 조상까지 쭉 계보를 계산하고 y의 조상까지 쭉 계보를 계산하고, 중간에 겹치는 지점을 찾는 접근이었다.

def sol(p_num, tar, rel):
    # [부모, 자식] -> [7,3]이라면 7이 3의 부모

    p_arr = [0 for _ in range(p_num + 1)]
    # p_arr[i]는 i번째 사람의 부모를 뜻한다.

    for r in rel:
        p_arr[r[1]] = r[0]

    answer = 0  # 촌수

    # 촌수 계산하는 법 -> 공통된 조상까지 갈때 걸리는 길을 잰다.

    r_arr1 = clac_family(p_arr, tar[0])
    r_arr2 = clac_family(p_arr, tar[1])

    #한 명이 조상일 때
    if len(r_arr1) == 0 and len(r_arr2) != 0:
        if tar[0] in r_arr2 :
            return r_arr2.index(tar[0]) + 1
        else:
            return -1
    elif len(r_arr1) != 0 and len(r_arr2) == 0:
        if tar[1] in r_arr1:
            return r_arr1.index(tar[1]) + 1
        else:
            return -1
    elif len(r_arr1) == 0 and len(r_arr2) == 0:
        return -1

    #조상이 다른 경우
    if r_arr2[-1] != r_arr1[-1]:
        return -1

    #공통된 부분을 찾는 방법
    flag = -1
    for r in r_arr1:
        if r in r_arr2:
            flag = r
            break

    level1 = r_arr1.index(flag)
    level2 = r_arr2.index(flag)

    answer = level1 + 1 + level2 + 1

    return answer


def clac_family(p_arr, my_num):
    t = p_arr[my_num]
    ancestor = []

    while (t!= 0):
        ancestor.append(t)
        t = p_arr[t]

    return ancestor
'''

people_num = int(input())
target = list(map(int, sys.stdin.readline().split()))
connections = int(input())
adj_list = [[] for _ in range(people_num + 1)]

for _ in range(connections):
    r = list(map(int, sys.stdin.readline().split()))
    adj_list[r[0]].append(r[1])
    adj_list[r[1]].append(r[0])

print(sol(people_num, target, adj_list))


