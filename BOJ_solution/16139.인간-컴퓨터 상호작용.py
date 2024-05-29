#문제 유형: 누적합

import sys

def sol(string, arr):

    cum_sum = [[0 for _ in range(26)]]
    # 누적합을 사용해서 풀었다.
    # a 는 97, 아스키코드를 이용해서 변환했다.
    for st in string:
        idx = ord(st) - 97
        a = cum_sum[-1][::] #맨 마지막 배열을 따와서
        a[idx] += 1 # 누적합으로 해당 글자가 나온 횟수를 더해줌
        cum_sum.append(a)

    for a in arr:
        target = a[0]
        s = int(a[1])
        e = int(a[2])

        s_arr = cum_sum[s]
        e_arr = cum_sum[e+1]
        t_idx = ord(target) - 97

        print(e_arr[t_idx] - s_arr[t_idx])

        #가장 naive하게 푸는 법 -> slicing하고 나서 하나씩 세기 (108ms)

        # curr = string[s:e+1]
        # ans = 0
        # for j in range(len(curr)):
        #     if curr[j] == target:
        #         ans += 1
        # print(ans)

    return 0

s = input()
n = int(input())
questions = []

#입력 시에 옵션이 섞여있어서 int로 mapping 하지 않음
for _ in range(n):
    q = list(sys.stdin.readline().split())
    questions.append(q)

sol(s, questions)