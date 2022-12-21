def sol(L, P, people):

    maximum = P * L
    answer = []

    for i in people:
        answer.append(i - maximum)
    return answer


L, P = map(int, input().split())
people = list(map(int, input().split()))

print(*sol(L, P, people))
