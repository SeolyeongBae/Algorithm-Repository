# 문제 유형: 누적합!
# 처음에 1,2로 하는게 아니라 1, -1로 변형해서 처리해주는 게 좋다.
# 누적합을 그래프처럼 생각하는 게 키포인트다. 문제는 'i부터 j까지 모두 더했을 때 값이 최대인 구간'을 찾는다는 의미다.
# 따라서 누적합의 max - min을 계산하자.
# 혹은 둘다 플러스나 둘 다 마이너스일 경우에는 maximum, minimum 값을 바로 넣도록 핸들링하는 게 좋다.

RIGHT = 2

def sol(arr):
    if arr[0] == RIGHT:
        arr[0] = -1
    s = [arr[0]]

    for i in range(1, len(arr)):
        add = -1 if arr[i] == RIGHT else arr[i]
        s.append(s[i - 1] + add)

    maximum = max(s)
    minimum = min(s)

    answer = max(maximum, maximum - minimum)
    answer = max(answer, -minimum)

    print(answer)


N = int(input())
a = list(map(int, input().split()))

sol(a)

# i : 인접한 개수

# 연속된 k개를 골랐을 때 1의 개수와 2의 개수가 같아야 한다.
# 1*x + 2*y = s
# x + y = k

# y = s - k
# x = 2k - s

# x - y는 그러면 2k - s - s + k = 3k - 2s 겠구나
# 3k - 2s의 가장 큰 값을 구해야 한다!

# dp[k] = k개를 칠했을 때 얻는 가장 큰 깨달음
# 하지만 점화식이 바로 떠오르질 않는다..! dp의 요건을 충족시키기 어려워 보인다.
