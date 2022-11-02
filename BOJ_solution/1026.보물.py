# 문제 유형 : 그리디 문제, 당장 눈앞에 있는 최적해를 구해야 한다.
# 서로의 곱이 최소화가 되는 경우는 무엇일까?
# 최댓값 * 최솟값을 곱하는 경우말고는 잘 없다..


def sol(N, A, B):

    A.sort()
    B.sort()
    B.reverse()

    answer = 0
    for i in range(N):
        answer = answer + A[i] * B[i]
    return answer


N = int(input())
A_series = list(map(int, input().split()))
B_series =  list(map(int, input().split()))

print(sol(N, A_series, B_series))