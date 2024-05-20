#문제 유형: 이분탐색. 방법을 잘 찾아서 잘 풀었다.
#다만 maximum 갱신을 놓쳤던 점, 그리고 저지 사이트에 포맷을 잘못 정해서 많이 틀렸다,,,

def sol(arr, target):
    total = sum(arr)
    arr.sort()
    if total <= target:
        return arr[-1]
    else:
        # 살짝 나무자르기 감성이다.
        # 예산 상한을 k라고 하고, 예산이 target보다 클 경우에는 k를 낮춘다. 예산이 target보다 작을 경우 k를 높인다.
        #이분탐색으로 구현.

        s = 0
        e = arr[-1] #제일 큰 값
        maximum = 0 #시작은 0이라고 해야한다..!

        while s <= e:
            mid = (s + e) // 2
            budget = 0

            for i in range(len(arr)):
                if arr[i] >= mid: #mid(예산 상한)보다 큰 값이 나타난 경우
                    if i == 0:
                        budget = mid * len(arr)
                    else:
                        budget = sum(arr[:i]) + mid * (len(arr) - i)
                    break

            #오답노트: 여기서 같은 경우 바로 리턴해버렸는데, 거기서 answer 갱신을 안했다.
            if budget < target:
                maximum = max(mid, maximum)
                s = mid + 1
            elif budget > target:
                e = mid - 1
            else:
                return max(mid, maximum)

    return maximum

N = int(input())
req = list(map(int, input().split()))
M = int(input())

print(sol(req, M))


