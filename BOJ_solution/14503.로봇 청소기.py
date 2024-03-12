import sys

back_move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
post_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

up = 0
right = 1
down = 2
left = 3

def sol(r, c, direction, arr):
    clean = 0
    current_x = r
    current_y = c

    while (True):
        if arr[current_x][current_y] == 0:
            clean += 1
            arr[current_x][current_y] = -1

        if arr[current_x-1][current_y] != 0 and arr[current_x+1][current_y] != 0 and arr[current_x][current_y-1] != 0 and arr[current_x][current_y+1] != 0:
            #넷 전부 다 청소되지 않은 빈 칸이 없는 경우
            nx = current_x + back_move[direction][0]
            ny = current_y + back_move[direction][1]
            if arr[nx][ny] != 1:
                current_x = nx
                current_y = ny
                continue
            else:
                break
        else:
            #한 칸이라도 남아서 청소가 가능한 경우
            direction = (direction + 3) % 4
            nx = current_x + post_move[direction][0]
            ny = current_y + post_move[direction][1]
            if arr[nx][ny] == 0:
                current_x = nx
                current_y = ny
            continue

    return clean

n = list(map(int, input().split()))
r,c,d= list(map(int, input().split()))




arr =[]


#0은 청소되지 않았고, 1은 벽이 있음.

for _ in range(n[0]):
    l = list(map(int,sys.stdin.readline().split()))
    arr.append(l)


print(sol(r,c,d,arr))