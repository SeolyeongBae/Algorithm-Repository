
def replace( height, width, arr, now, sur, rep) : #now의 값을 가진 원소가 주위에 sur라는 값이 있다면 rep로 대체된다는 뜻
    i = 1
    j = 1
    #replace가 2, surround가 2
    result = [0]
    while (i <= (height // 2) or j <= (width // 2)):
        cheese = 0 #탐색순서 : 시계방향 빙글빙글 1,1에서 출발
        for k in range(j, width - j):
            if arr[i][k] == now and (arr[i - 1][k] == sur or arr[i + 1][k] == sur or arr[i][k-1] == sur or arr[i][k+1] == sur):
                arr[i][k] = rep
                cheese +=1
        for k in range(i, height - i):
            if (arr[k][width - j] == sur or arr[k][width - 2 -j] == sur or arr[k-1][width - 1 - j] == sur or arr[k+1][width - 1 - j] == sur) and arr[k][width - 1 - j] == now:
                arr[k][width - 1 - j] = rep
                cheese += 1
        for k in range(width - j - 1, j - 1, -1):
            if arr[height - 1 - i][k] == now and (arr[height - i][k] == sur or arr[height - i - 2][k] == sur or arr[height - 1 - i][k+1] == sur or arr[height - 1 - i][k-1] == sur):
                arr[height - 1 - i][k] = rep
                cheese += 1
        for k in range(height - 1 - i, i, -1):
            if (arr[k][j - 1] == sur or arr[k][j + 1] == sur or arr[k+1][j] == sur or arr[k-1][j] == sur) and arr[k][j] == now:
                arr[k][j] = rep
                cheese += 1
        result[0] += 1
        result.append(cheese)
        i += 1
        j += 1
    return result

def search_zero(height, width, arr):
    for i in range(0, height) :
        for j in range (0, width):
            if arr[i][j] == 0 and (arr[i][j-1] == 2 or arr[i][j+1] == 2 or arr[i+1][j] == 2 or arr[i-1][j] == 2) :
                arr[i][j] = 2

def replac_zero(height, width, arr):
    arr_count = replace(height, width, arr, 0, 2, 2)

    while (sum(arr_count) - arr_count[0] != 0):
        search_zero(height, width, arr)
        arr_count = replace(height, width, arr, 0, 2, 2)

def melt_cheese(height, width, arr):
    for i in range(0, height) :
        for j in range (0, width):
            if (i == 0 or i == height -1) or (j == 0 or j == width -1 ) :
                arr[i][j] = 2 #엣지는 모두 0으로 인풋되므로 모두 2로 대체함

    count = 0

    replac_zero(height, width, arr)

    while (1):
        arr_rep = replace(height, width, arr, 1, 2, 3)
        replace(height, width, arr, 3, 2, 2)

        replac_zero(height, width, arr)

        count += 1

        if sum(arr_rep) - arr_rep[0] == 0:
            break

        cheese_num = sum(arr_rep) - arr_rep[0]

    result_arr = [count -1, cheese_num]
    return result_arr

arr= list(map(int, input().split())) #세로, 가로 길이다. arr[0]가 세로 길이 arr[1]가 가로 길이

cheese = [list(map(int, input().split())) for i in range(arr[0])]

result = melt_cheese(arr[0], arr[1], cheese)

print(result[0])
print(result[1])