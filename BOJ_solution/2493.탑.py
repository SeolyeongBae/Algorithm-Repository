#keypoint: 나는 원래 있던 게 무시될까봐 priorty queue를 사용해서 가장 작은 값을 맨 앞으로 보내려고 우선순위 큐를 사용함
#하지만 이 문제도 그렇고, 전에 있던 two point 정렬 문제도 그렇고 '고려하지 않아도 되는, 어차피 일어나게 되는 케이스'가 있었음을 알게 됨
#stack를 쓴다고 하자.

'''
 6, 9, 5, 7, 4의 순서로 있음. 뒤에서부터 간다
 4를 스택에 넣음,
 7을 만남. 7을 만났으므로 4를 스택에서 뺌, 스택은 7이 있음
 5를 만남. 7, 5가 스택에 있음.
 9를 만남, 7과 5가 스택에서 빠짐

 -> 만약에 9가 아니라 6을 만났다면?
 맨 위에 있는 5는 빠지고 6이 들어감, 7, 6 이렇게 있음

 내가 걱정했던 상황은, 스택을 사용했을 떄 특정 수보다 큰 수가 앞에 있으면 어떡하지 싶은 것이였다.
 하지만 스택을 사용하면 큰 값은 아래에 쌓이고, 작은 값은 위로 쌓인다. 그럴 일이 없다는 것이다.
 해당 사항을 직관적으로 바로 알기 힘들었고, 작은 값을 무조건 앞으로 올려주기 위해서 우선순위 큐를 사용해 시간이 느리게 나왔던 것이다.
'''

def sol(t):
    ans = [0] * len(t)
    q = []

    for i in range(len(t)-1, -1, -1):
        c = (t[i], i)
        if len(q) == 0:
            q.append(c)
            continue
        else:
            while(len(q) != 0):
                print(q)
                top = q[-1]
                if t[i] >= top[0]:
                    ans[top[1]] = i + 1
                    q.pop()
                else:
                    break
            q.append(c)

    return ans

N = input()
towers = list(map(int, input().split()))

print(*sol(towers))


'''


def sol(t):

    #높이가 1 이상 100,000,000 이하면 2차원 배열로 할 만한간가?
    #하지만 탑의 개수가 최대 500 000개이므로 무조건 노가다하는건 아닐 듯 함

    #일단 맨 오른쪽에서부터 접근한다.
    #맨 뒤에서부터 가다가, 만나면 pop한다.
    #근데 왜 스택이지?
    #priorty-queue를 쓰자. -> python3으로 3800ms가 나오는 풀이를 써버렸다.
    #더 빠르게 할 순 없을까?

    q = PriorityQueue()
    ans = [0] * len(t)

    for i in range(len(t)-1, -1, -1):
        c = (t[i], i)
        if q.empty():
            q.put(c)
            continue
        else:
            while(q.empty() == False):
                top = q.get()
                if t[i] >= top[0]:
                    ans[top[1]] = i + 1
                else:
                    q.put(top)
                    break
            q.put(c)

    return ans


'''