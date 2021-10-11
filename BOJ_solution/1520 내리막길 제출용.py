import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def reach(height, width, arr):

    top = stack[-1]
    y = top[0]
    x = top[1]

    if (x == 0 and y == 0) :
        go[y][x] = 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #끄트머리에 있는 애들 거르기
        if (y == 0 and i == 1) or (y == height -1 and i == 0) or (x== 0 and i == 3) or (x == width -1 and i == 2):
            continue

        elif ((ny, nx) == top ) :
            continue

        if arr[ny][nx] > arr[y][x] and ((go[ny][nx] == -1) or (go[ny][nx] > 0)):
            stack.append((ny, nx))

            if ((go[ny][nx] == -1) ) :
                go[ny][nx] = 0
                reach(height, width, arr)

            go[y][x] += go[ny][nx]

            stack.pop()


arr= list(map(int, input().split())) #세로, 가로 길이다. arr[0]가 세로 길이 arr[1]가 가로 길이

map = [list(map(int, input().split())) for i in range(arr[0])]


stack = []

go = [[-1] * arr[1] for _ in range(arr[0])]

stack.append((arr[0] - 1, arr[1] - 1))  # 스택 초기 좌표 지정

reach(arr[0], arr[1], map)

print(go[arr[0] -1][arr[1] -1]+1)

