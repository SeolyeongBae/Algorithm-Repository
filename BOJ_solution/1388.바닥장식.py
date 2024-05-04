# 문제 유형: 탐색?
# 하지만 그냥 구현으로 푸는 게 더 빠른 것 같다.
# 탐색을 하면 dfs로 해서 - 는 왼쪽에서 오른쪽방향으로, |는 위에서 아래로 모든 블럭이 다 탐색될때까지 하는 것 같다
# 그냥 구현으로 하면 '최초로 - 혹은 |가 생성되는 시점'에 값을 더했다.
# 처음에는 '가로막히는 시점'에 더하려고 했는데, 그러면 배열 맨 끝에 있는 타일에 대한 핸들링이 복잡해져서 '블락 시작 시점'에 값을 추가하기로 했다.

def sol(arr, n, m):

    ans = 0
    prev = ['0' for _ in range(m)]

    for i in range(n):
        f = arr[i]
        for j in range(m):
            if f[j] == '|' and prev[j] != '|':
                ans += 1 #처음 세로 막대기가 나온 시점에 추가!
            if j != 0 and f[j] == '-' and f[j-1] != '-':
                ans += 1 #index error 핸들링
            if j == 0 and f[j] == '-':
                ans += 1
        prev = f

    return ans


floor = []
n, m = list(map(int, input().split()))

for _ in range(n):
    f = input()
    floor.append(f)

print(sol(floor, n, m))