# 어떻게 풀어야 할까?
# 맨 뒤부터 탐색하면서 더 차이가 작으면서 큰 수를 넣으면서 리스트 갱신?
# DP로 풀면 최적의 해를 보장하지 못한다고 생각했는데... 아닌가?
# 예를 들면 1, 2, 6, 8, 5, 6, 7
# dp로 풀려면? dp[i]는 i번째를 맨 끝으로 하는 가장 긴 배열! 이렇게 해서 dp로 풀면 된다~

def sol(arr):

    if len(arr) == 1:
        return 1

    dp = [1]
    #dp[i] = arr의 i번째를 끝으로 하는 가장 긴 증가하는 부분 수열의 길이

    for i in range(1, len(arr)):
        max_length = 0

        for j in range(i):
            #내가 더 큰 상황
            if (arr[j] < arr[i]) and (dp[j] > max_length):
                max_length = dp[j]

        dp.append(max_length + 1)


    return max(dp)


arr_size = int(input())
num_list = list(map(int, input().split()))

print(sol(num_list))

'''
틀린 풀이 : 배열에 하나씩 추가해가면서 맨 뒤에 원소만 비교해서 넣거나 빼거나 하는 경우
틀리는 케이스 : 
7
1 2 6 8 5 6 7
틀린 이유: 맨 뒤에것만 심사를 해서  1, 2, 6 ,8에서 1, 2, 5 로 바꿔야 할때 커버가 안된다.

def wrong_sol(arr):

    arr_len = len(arr)

    if arr_len == 1:
        return 1

    dp = [arr[0], arr[1]]

    for i in range(2, arr_len):
        dplen = len(dp)

        #일단 증가하면 넣음
        if arr[i] > dp[dplen - 1]:
            dp.append(arr[i])
            continue

        #만약에 작은데 각이 보이면
        if arr[i] > dp[dplen - 2] and ((arr[i] - dp[dplen-2]) <= (dp[dplen-1] - dp[dplen-2])):
            dp.pop()
            dp.append(arr[i])

    print(dp)
    return len(dp)


'''
