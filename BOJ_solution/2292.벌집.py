#칸의 수
# 1칸, 6칸, 6 + 1*6, 6 + 2*6, 6 + 3*6 ,,,
#[1, 7, 19, 37, 61...]
#[0, 1*6, (1+1)*6 + 1*6, (1+2)*6+ 3*6, (1+3)*6 + 6*6]
#[0, 1, 3, 6, 10 ]
# i번째 인덱스는 앞에 있는 거에 i*6을 더한다.

N = int(input())

honey = [1]
answer = -1

if N == 1: answer = 1

while(answer == -1):
    h = honey[-1] + len(honey) * 6
    if h == N:
        answer = len(honey) + 1
    elif h > N:
        answer = len(honey) + 1
    else:
        honey.append(h)

print(answer)


