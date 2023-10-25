# 문제 유형: 자료구조
# 까다로운 점 -> 10개씩 입/출력을 해야 한다.

# 가장 Naive한 방법 : 우선순위 큐를 사용해서 매번 정렬한다 -> 골드 문제다보니 반드시 시간초과가 날 것이다! (그러나 구글링을 해보니 sort 해도 시간만 많이 걸릴 뿐, 가능은 하다)

# 접근1 -> 중앙값과 새로 넣는 값을 비교해서 값의 이동을 예측한다
# 반례) 1, 2, 3에서 4,5,를 넣으면 중앙값이 새로 넣은 값 중에 하나가 되지 않고 기존에 있는 3이라는 값이 된다.

# 기껏해야 홀수 인덱스마다 값이 두개가 들어간다.

# 3개의 케이스를 예측했지만 사실은 아님. 1,2,5에서 두 가지 수가 들어올때 6,7이 올수도 있고 3,4가 올수도 있고 3,6이 들어올수도 있음.
# 접근 2 -> 총 3개(왼) + 1개(중앙) + 3개(오른쪽) 해서 7개의 케이스가 있다.
# 노가다로 구현 -> 중앙값, 중앙값보다 바로 작은값, 중앙값보다 바로 큰값을 담는 어레이를 만드려고 했음...
# 반례) 1,2,3, 5 ,6,7,10 에서 8,9를 넣으면 중앙값이 6이 되고 바로 그 옆의 값은 7이다. 하지만 7에 대한 정보는 저장해놓지 않았으므로 7을 꺼내올 수 없다 -> 접근 틀림

# 답지 봤음. 어프로치는 괜찮았다(중앙값을 기준으로 나눈다는 점에서). 근데 좀 더 나은 풀이로 우선순위 큐 2개를 쓴다. 하나는 작은거 정렬 하나는 큰거정렬, 그렇게 두개의 사이즈를 비교해가며 중앙값을 찾으면 된다.

#까다로운 점 2 : 파이썬 heap는 maxheap이 어렵다! minus 부호를 붙여 처리를 해줘야 한다.

import sys
from heapq import heappush, heappop

def sol(tc):
    for t in tc:
        length = len(t)
        print((length+1)//2)

        left, right, mid = [-t[0]], [], [t[0]]

        #left heap : 중앙값 + 중앙값보다 작은 값
        #right heap: 중앙값보다 큰 값

        for i in range(1, length):
            n = t[i]
            if n <= -left[0]:
                heappush(left, -n)
            else:
                heappush(right, n)

            if( i % 2 == 0): #홀수 숫자 케이스
                if len(left)-len(right) == 3:
                    num = -heappop(left)
                    heappush(right, num)

                if len(right) - len(left) == 1:
                    num = heappop(right)
                    heappush(left, -num)

                mid.append(-left[0])

        s = len(mid) // 10
        r = len(mid) % 10

        for j in range(s):
            arr = mid[(10*j):10*(j+1)]
            print(*arr)

        arr = mid[(10*s):(10*s + r)]
        print(*arr)

    return 0

testcase_num = int(input())
tc = []

for _ in range(testcase_num):
    num = int(input())
    arr = []

    s = num // 10
    r = num % 10

    for i in range(s):
        testcase = list(map(int,sys.stdin.readline().split()))
        arr = arr + testcase

    if r >= 1:
        testcase = list(map(int,sys.stdin.readline().split()))
        arr = arr + testcase

    tc.append(arr)

sol(tc)




