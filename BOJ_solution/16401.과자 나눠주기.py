#문제 유형: 이분탐색.
#못 풀었던 이유: 인덱스의 이분탐색이라고 생각했어서 '몫의 합' 개념을 어떻게 접목시켜야 하는지 몰라서 헤맸다
#하지만 이 문제는 0부터 i 의 이분탐색이 아니라 1부터 max(snack)의 이분탐색이었다!
#처음에 무식하게 for문을 돌면서 찾았으므로, 거기서 이분탐색으로 접근하겠다는 발상을 했었어야 됐다.

import sys

def binary_search(arr, target):
    return 0

def sol(m, snacks):
    # 최대한 긴 과자를 나눠주면서, 과자의 길이가 모두 같아야 한다.
    # snack는 sort된 상태

    # 알고리즘?
    #과자가 m개 이상 있는 경우?
    #하지만 1, 1, 5개에서 2명한테 주는 경우는 5를 2개로 뽀개는게 좋다.
    #브루트 포스로 접근: 과자의 개수를 m=0 으로 해서 하나씩 늘려 나갔을 때 몫의 합이 조카의 수보다 작은지를 체크한다. -> 당연하지만 타임아웃.
    '''
    for i in range(1, max(snacks)):
        arr = [(j // i) for j in snacks]
        s = sum(arr)

        if s < m: #과자의 수가 조카의 수보다 적다면.
            break
    '''
    #이러면 시간초과가 나는데, 어떻게 줄여야 할까? -> 반복문을 1부터 snack의 maximum으로 하지 말고, 이분 탐색으로 돌린다.

    s = 1
    e = max(snacks)
    cnt = sum(snacks) #과자 길이를 1씩 잘라줬다고 가정했을 때

    ans = 0

    if cnt < m :
        return 0

    #탐색 대상은 index가 아니라 1부터 max(snacks) 사이인거임!
    while (s <= e):
        mid = (s + e) // 2
        arr = [(j // mid) for j in snacks]
        cnt = sum(arr)

        if cnt >= m:
            #더 큼직하게 잘라봐도 된다. 일단 이 값까지는 m 이상이므로 보장한다는 의미.
            s = mid + 1
            ans = mid
        else:
            e = mid - 1

    return ans

M, N = list(map(int, input().split()))
snacks = list(map(int, sys.stdin.readline().split()))

print(sol(M, snacks))
