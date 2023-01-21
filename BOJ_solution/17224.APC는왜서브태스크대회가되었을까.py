#이거 서브태스크 1은 브론즈 맞는데
#서브태스크 2는 조금 어려울지도?? -> hard만 풀면 다푼다는게 힌트였다.

def sol(problems, diff, count):
    problems.sort(key = lambda x:x[1])
    #hard 난이도 기준으로 정렬

    score = 0

    #거꾸로 봐야함
    for i in range(len(problems)):
        if count == 0: break
        [easy, hard] = problems[i]
        if easy > diff :
            continue
        else:
            count -= 1
            if hard > diff :
                score += 100
            else :
                score += 140


    return score


[N, L, K] = list(map(int, input().split()))
#L 이하의 난이도의 문제를 풀 수 있고, K개보다 많은 문제를 해결할 수 없다.
difficulty = []

for _ in range(N):
    d = list(map(int, input().split()))
    difficulty.append(d)

print(sol(difficulty, L, K))
