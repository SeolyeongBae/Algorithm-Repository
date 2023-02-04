#이렇게 Naive 하게 문제를 풀어도 되나? 이런 게 왜 실버 4지 라는 의문이 들었고
#역시 채점 현황을 보니 시간 초과가 떡하니 박혀 있었다...
#해시를 여기서!! 사용 하는 것인가~!
#처음 접근 -> 배열을 사용했지만, 딕셔너리로 한번 해보자!
#문제 자체는 쉽지만, 해시를 사용한 자료구조 즉 딕셔너리를 떠올려야만 풀 수 있는 문제였다.

N, M = map(int, input().split())
listen = {}
dbj = []
for _ in range(N):
    p = input()
    listen[p] = p

for _ in range(M):
    s = input()
    if s in listen:
        dbj.append(s)

print(len(dbj))
dbj.sort()
#사전순으로 출력을 안했다 ㅎㅎ;;
for i in range(len(dbj)):
    print(dbj[i])