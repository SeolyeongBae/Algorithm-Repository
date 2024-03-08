#문제 유형: 구현? 너무 어려운데...
#으악! 메모리초과 -> C++의 next_permutation을 구현한다.
#10972.다음 순열과 아주 비슷한 문제다.


import sys


n = int(input())

def sol(arr):
    target = -1
    swap_target = -1

    arr = list(arr)

    for i in range(len(arr) - 1, 0, -1):
        if ord(arr[i -1]) < ord(arr[i]): #한 번 틀렸는데, 여기 부등호에 등호를 달아놔서 틀렸음.
            target = i -1
            break

    if target == -1:
        print("".join(arr))
        return

    for j in range(len(arr)-1, target, -1):
        if ord(arr[j]) > ord(arr[target]):
            swap_target = j
            break

    temp = arr[target]
    arr[target] = arr[swap_target]
    arr[swap_target] = temp

    tail_arr = arr[target + 1:]
    ans = arr[:target + 1] + tail_arr[::-1]

    print("".join(ans))
    return

for i in range(n):

    s = str(sys.stdin.readline().strip())
    sol(s)