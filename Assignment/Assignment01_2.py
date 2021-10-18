def rotateMat(mat) :
    num = len(mat)
    for i in range(0, num):
        for j in range(0, i+1):
            if (i == j and i > (num-1)//2 ):
                continue
            else :
                temp = mat[i][j]
                mat[i][j] = mat[num-1-i][num-1-j]
                mat[num - 1 - i][num - 1 - j] = temp


    return mat


#issue : 중복 방문을 어떻게 처리하지?

map = [[1,3,4],[2,4,6],[6,2,6]]

arr = rotateMat(map)

a = 0
while a < len(map):  # 세로 크기
    b = 0
    while b < len(map):  # 가로 크기
        print(arr[a][b], end=' ')
        b += 1  # 가로 인덱스를 1 증가시킴
    print()
    a += 1  # 세로 인덱스를 1 증가시킴