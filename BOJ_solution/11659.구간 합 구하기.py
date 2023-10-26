# 문제 유형: 누적합
# 1트 성공 -> 중요한 점 : 맨 처음 엘리먼트를 0으로 해서 1번째를 버퍼할 수 있는 게 필요했음.
# 그러나 실행시간이 느렸다?
# 다른 사람의 정답코드를 보니 accumulate 라는 라이버르리를 사용해서 누적합을 계산하거나, sys.stdout.write를 통해 출력해 시간을 아낀 듯 하다.

import sys

[n, m] = list(map(int, input().split()))

nums = list(map(int, input().split()))
s = [0]

for i in range(1, len(nums)+1):
    s.append(s[i-1] + nums[i-1])

for _ in range(m):
    [start, end] = list(map(int, sys.stdin.readline().split()))

    print(s[end] - s[start - 1])