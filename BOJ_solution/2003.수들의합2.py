# 누적합 + 브루트포스로 풀었는데 시간이 엄청나게 많이 걸렸음.
# 누적합 + 투포인터로 접근하니 시간이 몹시 크게 줄었음.

def sol(arr, target):

    # 누적합 문제같은데??

    tsum = [0 for _ in range(len(arr) + 1)]
    for i in range(1, len(arr) + 1):
        tsum[i] = tsum[i-1] + arr[i-1]

    # 누적합 어레이에서 두 수의 차가 target이 되는 경우를 찾는다.
    # 가장 naive한 방법: 브루트포스를 해서 O(n^2)로 푼다
    # 조금 더 빠른 방법: 이분탐색을 구현해서 O(nlogn)으로 푼다
    # 실버 4고 시간초과가 나지 않을 것이므로 나이브한 방법으로 풀이하겠음.
    # 하지만 정말 빠른 방법 -> 투포인터

    # 누적합으로 브루트포스 사용한 경우
    # ans = 0
    #
    # for i in range(len(arr) + 1):
    #     current = tsum[i]
    #     to_find = current + target
    #     # 누적합 배열에서 같은 값은 없다.(자연수만 arr에 들어 있기 때문)
    #
    #     ans += tsum[i:].count(to_find) # 중복으로 세는 것을 방지한다.

    #투포인터로 구현한 경우
    ans = 0
    start = 0
    end = 1
    # 이분탐색처럼 생각해서 end를 맨 끝에 뒀지만, 그렇게 생각하면 안된다...
    # O(n)으로 해결이 가능하다.

    while (start <= end and end <= len(arr)):
        res = tsum[end] - tsum[start]

        if res == target:
            ans += 1
            start += 1
            end += 1

        elif res > target:
            start += 1

        elif res < target:
            end += 1

    return ans


N, M = list(map(int, input().split()))
series = list(map(int, input().split()))

print(sol(series, M))