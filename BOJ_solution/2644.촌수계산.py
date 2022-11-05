# 주어진 사람의 촌수를 판별하는 문제
# 어떻게든 풀었다!!

#DFS, BFS를 사용한 풀이를 해보자.
#촌수를 계산하느 직관적인 방법으로 해결함.

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


people_num = int(input())
target = list(map(int, input().split()))
connections = int(input())
relation_arr = []

for _ in range(connections):
    relation = list(map(int, input().split()))
    relation_arr.append(relation)

print(sol(people_num, target, relation_arr))


