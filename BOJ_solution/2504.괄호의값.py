# 문제 유형 : 구현
#시작시간: 1:15 -> 2시간 넘게 품.. ㅠㅠ

#() -> 2
#[] -> 3

#오답노트 : 처음에는 괄호에서 시작하는대로 하려고 별의별 뻘짓을 다하다가, 재귀로도 해보다가... 어떻게 재는지 몰라서 계속 하다가 결국 while문으로 노가다하는 방식을 선택했다.
#하지만 더하는 상황, 곱하는 상황을 분간하기가 너무 어려웠다...

#굉장히 잘 한 답을 보니까 곱하는 걸 나중에 하는게 아니라 시작하면서 곱한다는 점이 좋아 보였고, 그리고 내 안에 브라켓이 있는지 체크할때 stack이 아니라 원본 어레이를 활용했다.
#여는 걸 넣을때 값을 곱한다. 닫힌 괄호를 만나면 tmp를 전체 결과인 res에 넣고 괄호를 나눠준다.

#아, 그러면 이게 어떻게 보면 분배법칙이 성립하는 셈이다
#(()[[]])
# 2 * ( 2 + 3 * 3 )
# 인데 이거를 2 * 2 + 2 * 3 * 3 이라고 풀어서 넣은 거다!
# 여는 괄호를 할때 ( ( 로 4가 곱해진거고, ) 가 닫혔으니 4를 더해주고 ()만큼은 덧셈에 효력이 없으니 2로 나눠주는 감성이다.
# 내 생각에는 오늘 밤새 이걸 풀었다고 해도 이 방법은 절대 생각 못했을 것 같다. while 문으로 어떻게든 꾸역꾸역 구현했지만 답을 보고 앞으로 쓸 수 있는 하나의 테크닉을 배웠다.



def sol(arr):
    stack = [arr[0]]

    score = []
    result = []
    depth = []
    flag = 0

    for i in range(1, len(arr)):
        top = ''
        if len(stack) != 0: top = stack[-1]

        if (top == '[' and arr[i] == ']') or (top == '(' and arr[i] == ')'):
            depth.append(flag)
            flag = flag - 1

            stack.pop()
            result.append(arr[i])
            if top == '[': n = 3
            if top == '(': n = 2

            score.append(n)

        else:
            flag = flag + 1
            stack.append(arr[i])

    if len(stack) != 0:
       return 0

    max_value = max(depth)

    while max_value > 0 :
        new_d = []
        new_s = []
        for i in range(len(depth) -1):

            if depth[i] == max_value and depth[i] == depth[i + 1]:
                score[i+1] += score[i]
            elif depth[i] == max_value and (depth[i+1] + 1 == (depth[i])):
                score[i+1] *= score[i]
            elif depth[i] != max_value:
                new_s.append(score[i])
                new_d.append(depth[i])
        new_d.append(depth[-1])
        new_s.append(score[-1])

        depth = new_d
        score = new_s
        max_value = max(depth)

    return sum(score)

bracket_arr = input()

print(sol(bracket_arr))