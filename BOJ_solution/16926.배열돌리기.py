#유형: 구현,시간: 2:47 시작
#문제 이해를 처음에 잘못함... (배열 90도 회전이라 생각)
#해결 방법 : 의지의 한국인 기법, 다음 인덱스를 계산하지 않고 재귀로 해서 돌아간 인덱스가 어디인지 찾는 방법을 사용했다.
#하지만 다 풀고 정답을 찾아보니 num 횟수 만큼 for 문을 돌려 한칸씩 shift 시키는게 가장 좋은 해답인 것 같다...

def sol(matrix, num):

    col_num = len(matrix[0])
    row_num = len(matrix)

    rotated = [[0 for c in range(col_num)] for r in range(row_num)]

    #approach 1 : 껍질 하나씩

    for i in range(col_num):
        #한껍데기씩 함
        row_size = row_num - i - 1
        col_size = col_num - i - 1 #끝이 되는 인덱스

        #i번부터 row_size -1 호까지

        if row_size + 1 < i or col_size< i +1 :
            break

        for j in range(i, row_size + 1): #세로
            a, b = calc_next(j, i, 'D', num, row_size, col_size)
            c, d = calc_next(j, col_size, 'U', num, row_size, col_size)
            if rotated[a][b] != 0 or rotated[c][d] != 0:
                print_matrix(rotated)
                return
            rotated[a][b] = matrix[j][i]
            rotated[c][d] = matrix[j][col_size]



        for k in range(i + 1, col_size ): #가로
            a, b = calc_next(i, k, 'L', num, row_size, col_size)
            c, d = calc_next(row_size, k, 'R', num, row_size, col_size)
            if rotated[a][b] != 0 or rotated[c][d] != 0:
                print_matrix(rotated)
                return
            rotated[a][b] = matrix[i][k]
            rotated[c][d] = matrix[row_size][k]

    print_matrix(rotated)
    return



def calc_next(i, j, direction, amount, r, c):
    if amount == 0:
        return i, j


    if direction == 'D':
        req_hor = r - i if amount > (r - i) else amount
        return calc_next(i + req_hor , j, 'R', amount - req_hor, r, c)

    elif direction == 'U':
        t = i - (row_num - r) if amount > i - (row_num - r) else amount
        return calc_next(i - t, j, 'L', amount - t, r, c)

    elif direction == 'L':
        t = j - (col_num - c) if amount > j - (col_num - c) else amount
        return calc_next(i , j - t, 'D', amount- t, r, c)

    else :
        req_ver = c - j if amount > (c - j) else amount
        return calc_next(i , j +  req_ver, 'U', amount - req_ver, r, c)



def print_matrix(matrix):
    for m in matrix:
        print(*m)

row, col, rotate_times = map(int, input().split())
arr = []
for _ in range(row):
    temp = list(map(int, input().split()))
    arr.append(temp)

col_num = len(arr[0]) - 1
row_num = len(arr) - 1

sol(arr, rotate_times)