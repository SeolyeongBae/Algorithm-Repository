#문제 유형: DP 의심했으나 브루트포스였다.
#O^3으로 해결했다. 더 빠른 방법이 있을까?

import sys

def sol(rect):

    #dp인가??
    #가장 naive한 방법: 브루트포스로 따진다.
    #가장 큰 변의 길이: max(len(rect), len(rect[0]))
    #여기서부터 하나씩 찾아나가면 될까?
    #각 한 자리 숫자니까 0~9의 케이스가 있음.
    n = len(rect)
    m = len(rect[0])

    ans = 0

    info = [[ 0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            #탐색 방향은 왼->오, 위->아래임
            target = rect[i][j]

            for k in range(j, m):
                if rect[i][k] == target and (k - j + 1) > ans:
                    #지금 같은 행에 똑같은 값을 발견한 것
                    if i+k-j <= n-1 and target == rect[i + k - j][j] and target == rect[i + k - j][k]:
                        ans = (k - j + 1)
    return ans * ans

N, M = list(map(int, input().split()))
rect =[]

for _ in range(N):
    r = sys.stdin.readline().strip()
    rect.append(r)


print(sol(rect))