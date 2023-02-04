from collections import deque

def sol(N, K):

    #1번부터 N명
    #1, 2, 3, 4, 5, 6, 7 에서 K가 3이면
    #3, 6 빠짐
    #1, 2, 4, 5, 7
    #2, 7 빠짐

    #circular linked list인가? (파이썬으로 어떻게 구현하지?)
    #큐를 쓰면 되는 거구나!!!!

    count = 1
    ans = []
    queue = deque([i for i in range(1, N+1)])
    while len(queue) > 0 :
        p = queue.popleft()
        if count % K == 0:
            ans.append(str(p))
        else:
            queue.append(p)
        count += 1

    return "<"+", ".join(ans)+">"


N, K = map(int, input().split())
print(sol(N,K))