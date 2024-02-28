import sys


[N, M] = map(int, input().split())

pokemon = [sys.stdin.readline().strip() for i in range(N)]
query = [sys.stdin.readline().strip() for i in range(M)]

for q in query:

    if q.isdigit():
        print(pokemon[int(q) -1])
    else:
        print(pokemon.index(q)+1)

# index가 시간이 많이 소요되므로 dictionoary를 겉아 이용하면 쉬워 보인다
# zip은 뭘까?