#문제 유형: 구현
#틀린 이유: 돌리고 나서의 상태를 기준이라고 잘못 생각함. 돌리기 전이었음. new_gear를 사용하고 해결함

import sys

def turn_left(arr):
    sliced = arr[1:]
    sliced.append(arr[0])
    return sliced

def turn_right(arr):
    sliced = [arr[-1]] + arr[:len(arr)-1]
    return sliced

def sol(gear, turn):
    #맞닿는 번호(제로인덱싱)
    # (2, 6) 이다.
    # 회전은 한 칸 한다.

    for t in turn:
        gear_num = t[0] - 1
        right_turn_dir = t[1]
        left_turn_dir = t[1]

        new_gear = gear[::]

        if t[1] == 1:
            new_gear[gear_num] = turn_right(gear[gear_num])
        else:
            new_gear[gear_num] = turn_left(gear[gear_num])

        #돌아가는 여부 기준은 돌아가고 나서가 아니라 돌아가기 이전이므로 먼저 주변 톱니를 돌리고 본인은
        for i in range(gear_num+1, 4):
            #인접한 것들끼리(변한 기어의 다음 기어의 회전을 결정)
            if gear[i-1][2] != gear[i][6]:
                #맞닿은 게 같지 않다면
                if right_turn_dir == -1: #전 기어가 반시계방향으로 돌았으면
                    new_gear[i] = turn_right(gear[i]) #시계방향으로 돈다
                    right_turn_dir = 1
                else:
                    new_gear[i] = turn_left(gear[i])
                    right_turn_dir = -1

            else:
                #맞닿은 게 같은 경우 회전하지 않는다.
                break

        if gear_num == 0:
            #예외처리 해주려고 1번 부분의 왼쪽은 없으니 return 해주려고 했는데 여기서 에러 겪음
            gear = new_gear
            continue

        for j in range(gear_num-1, -1, -1):
            #인접한 것들끼리(변한 기어의 다음 기어의 회전을 결정)
            if gear[j][2] != gear[j+1][6] :
                #맞닿은 게 같지 않다면
                if left_turn_dir == -1: #전 기어가 반시계방향으로 돌았으면
                    new_gear[j] = turn_right(gear[j]) #시계방향으로 돈다
                    left_turn_dir = 1
                else:
                    new_gear[j] = turn_left(gear[j])
                    left_turn_dir = -1
            else:
                #맞닿은 게 같은 경우 회전하지 않는다.
                break
        gear = new_gear

    score = 0

    for i in range(4):
        score += int(gear[i][0]) * (1<<i)

    return score

gear =[]
turn = []

#0은 청소되지 않았고, 1은 벽이 있음.
for _ in range(4):
    l = list(input())
    gear.append(l)

t = int(input())

for _ in range(t):
    l = list(map(int,sys.stdin.readline().split()))
    turn.append(l)


print(sol(gear, turn))



