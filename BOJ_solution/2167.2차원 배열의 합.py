#시간 초과!?!??! 가 났다 -> pypy 로 해결!! ^^
#이런 누적합의 경우 accmulate를 쓰면 속도가 더 빠르다고 한다.
#나는 매번 연산을 해 줬지만, semi-dp 느낌으로 저장받으면서 열 단위로 누족합을 계산한 arr를 받아, 필요한 값만 바로 가져온다면 조금 더 효율이 향상됐을 것 같다.

def sol(mat, s):

    for t in range(len(s)):
        [i, j, x, y] = s[t]
        sum = 0

        for a in range(i-1, x):
            for b in range(j-1, y):
                sum += mat[a][b]

        print(sum)

    return


N, M = map(int, input().split())

mat = []
for _ in range(N):
    r = list(map(int, input().split()))
    mat.append(r)

K = int(input())
s = []
for _ in range(K):
    i = list(map(int, input().split()))
    s.append(i)

sol(mat, s)
