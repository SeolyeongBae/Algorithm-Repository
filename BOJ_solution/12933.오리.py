#문제 유형: 구현... 인데 왜 위상정렬같지?

# 있을 수 있는 오리의 최수 개수란?
# 비트마스킹을 써볼까? -> q,u,a,c,k를 11111 로 해서 31이 채워지면 pop 하는 식으로 하고, 마지막에 31의 개수를 세는 방식을 취했다,

# 이 풀이를 쓰면 속도도 파이썬 치고는 준수하다. 다만 생각하는 시간이 오래 걸리고 짜는 시간이 오래 걸린다.
# 퓰이를 작성할 때 def sol()을 사용해서 함수를 쓰는 게 return을 통해서 일찍 풀이를 끝내는 데 유리해 보인다.
# 한 번 틀렸는데, quac 처럼 완결이 되지 않는 경우를 핸들링하지 않아서 그랬다. 마지막에 31과 0의 개수를 모두 세서 duck의 사이즈와 동일한지 체크해줘서 미완성인 quack이 있다면 -1을 출력했다.


def find_duck(duck, target):
    # duck array에서 target보다 큰 값을 찾는다
    return duck.index(target) if target in duck else -1

def sol(q, duck):
    for i in range(len(q)):
        # quack를 분리하려고 할때 필요한 최소 스택의 수는?
        t = -1
        if q[i] == 'q':
            # 10000 이면 16
            t = find_duck(duck, 31)
            if t == -1:
                t = find_duck(duck, 0)
            duck[t] = 16

        if q[i] == 'u':
            # 11000 이면 24
            t = find_duck(duck, 16)
            duck[t] = duck[t] | 8

        if q[i] == 'a':
            # 11100이면 28
            t = find_duck(duck, 24)
            duck[t] = duck[t] | 4

        if q[i] == 'c':
            # 11110 이면 30
            t = find_duck(duck, 28)
            duck[t] = duck[t] | 2

        if q[i] == 'k':
            # 11111 이면 31
            t = find_duck(duck, 30)
            duck[t] = duck[t] | 1

        if t == -1:
            return -1

    c = duck.count(31)
    z = duck.count(0)

    if c + z == len(duck) :
        return c
    return -1

q = input()

# 오리의 최대 수는 500마리. 실버 문제는 이런 식으로 max size를 미리 계산하면 쉽게 풀리는 경우가 많다.
duck = [0 for _ in range(501)]


print(sol(q, duck))