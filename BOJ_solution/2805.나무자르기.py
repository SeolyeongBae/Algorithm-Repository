# 유형: 이분탐색
# 실수했던 부분 : 나무 길이가 10인데 15만큼 칼이 있으면 sum 할때 0이 들어가야 하나, 마이너스 값이 들어가고 있었다.

def sol (arr, M):
    arr.sort()
    s = 0
    e = arr[-1] #제일 큰 값

    answer = 0

    while s <= e:
        total = 0
        mid = (s + e) // 2

        for a in arr:
            if a >= mid:
                total += (a - mid)
        if total >= M:
            s = mid + 1
            answer = mid
        else:
            e = mid - 1

    print(answer)
    return 0

[N, M] = list(map(int, input().split()))
trees = list(map(int, input().split()))

sol(trees, M)