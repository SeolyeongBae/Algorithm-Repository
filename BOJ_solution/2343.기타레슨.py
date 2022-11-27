#문제 유형: 이분탐색
#시작 시간: 오후 2:20
#1차 제출: 3:07, 틀림

#m개의 블루레이로 녹화, 각 블루레이의 길이는 같음
#한 블루레이의 최대 길이를 최소화하고, 각 비디오를 연달하서 녹화해야 함

#한 블루레이의 최대 길이를 최소화한다는 걸 잘 생각해보쟈!


def sol(arr, m):

    if m == 1: return sum(arr)

    #naive한 접근 -> 인 줄 알았는데 오히려 답이었음

    start = sum(arr)
    end = max(arr)
    ans = 0

    blue_ray = []

    while start >= end:
        tot = (start + end) // 2
        s = 0

        for i in range(len(arr)):
            if s + arr[i] <= tot:
                s += arr[i]
            else:
                # 기댓값보다 커지는 경우, 이 값을 내 값으로 넣을지 다음으로 넘길지 고민해야 한다.
                blue_ray.append(s)
                s = arr[i]
        blue_ray.append(s)
        if len(blue_ray) <= m: #여기가 포인트! 작더라도 계속 작아지도록 <=를 해줬음
            start = tot - 1
            ans = max(blue_ray)
        if len(blue_ray) > m:
            end = tot + 1

        blue_ray = []

    # for i in range(m-1, 0, -1):
    #     index = binary_sum_search(arr, i)
    #     blue_ray.append( sum(arr[:index+1]))
    #
    #     print('쪼갬', arr[:index+1])
    #     arr = arr[index+1:]

    return ans

N, M = map(int, input().split())
guitar = list(map(int, input().split()))

print(sol(guitar, M))


'''

#걸린 반례:
7 6
100 400 300 100 500 101 400


이분 탐색을 사용한 접근-> sum을 매개 변수로 사용해서 죄sum : 우sum의 비율이 1: m-1과 가까운 경우를 찾자
예시의 경우 1~5는 15, 나머지는 30이다. (1:2) 1~6은 21, 나머지는 24다. (1:1..) 1~4는  11, 나머지는 35다. (1:3.3)
    
failed approach: binary search로 mid를 찾았으나, 사실 이건 그냥 속도만 빨랐을 뿐이지 일일히 탐색하는거랑 다르지 않다. 한번에 해서 해를 계산하기 어렵다.
가장 어려웠던 부분은 쪼개는 기준이었다. rate로 하자니 rate 오차가 커도 되는 경우( 100, 500, 101, 400을 3개로 쪼개는 경우)가 있었고
그렇다고 가장 큰 size를 특정해서 하자니 나올 수 있는 가장 큰 size는 일일히 계산해야 했고 평균으로 나오는 값과 괴리감이 컸다.
그래서 실패헌 이분탐색 코드가 아래와 같다.

def binary_sum_search(arr, rate):
    start = 0
    end = len(arr) - 1
    err = sys.maxsize
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        f = arr[:mid+1]
        b = arr[mid+1:]

        v = sum(b) / sum(f)

        print(f, b, v, rate)

        if v == rate:
            return mid
        if v < rate:
            end = mid - 1
        if v > rate:
            start = mid + 1
        # if max(sum(b) / (rate-1), sum(f)) < err:
        #     err = max(sum(b) / rate, sum(f))
        #     ans = mid
        if abs(rate - v) < err:
            err = abs(rate - v)
            ans = mid

    return ans

'''