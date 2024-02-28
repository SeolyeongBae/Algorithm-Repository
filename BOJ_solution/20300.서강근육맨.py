import sys

N = int(input())
data = list(map(int, sys.stdin.readline().split()))

# 운동기구를 최대 두 개 까지 선택할수 있가
# 이전에 사용하지 않은 운동기구를 사용한다
# 한번 PT를 받을때 근손실이 M보다 적게 했을때 사용이 가능하게 해야함
# M의 최솟값을 구하자!

data.sort()
m = 0

if len(data) % 2 == 1:
    m = data[-1]
    data.pop()

data_reverse = data[::]
data_reverse.reverse()

for i in range(len(data)):
    temp = data_reverse[i] + data[i]
    if temp > m:
        m = temp

print(m)



'''
아주 naive하게 생각했을 떄, 짝수면 젤 작은거 + 젤 큰거 하면 되는거 아님? 생각했는데 아니었다
1 10 11 12면
optimal은 21이다 ...

어떻게 해야 할까?

if len(data) % 2 == 0:
    print(max(data) + min(data))
else:
    print(max(data))
'''