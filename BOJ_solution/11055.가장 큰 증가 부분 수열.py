#문제 유형: dp
#증가 부분 수열 중에서 합이 커야 함

def sol(arr):

    #dp[i] : i번째까지의 배열로 갔을때 존재하는 가장 긴 증가하는 부분 수열의 합
    if len(arr) == 1: return arr[0]

    dp = [arr[0]]

    for i in range(1, len(arr)):
        sum = 0

        #dp로 푸는 방법 -> 여기서 내가 더 큰 경우의 값을 가진 상황을 체크하고, (증가하는 수열임을 확인)
        #그리고 그 때의 합이 지금 저장하고 있는 dp의 합보다 큰지 체크함
        #만약에 더 크다면, 총합에 저장함

        for j in range(len(dp)):
            if arr[j] < arr[i] and dp[j] > sum:
                sum = dp[j]

        #앞선 배열 중에 값이 가장 큰, 내가 들어갈 수 있는 증가하고 있는 배열의 합을 가져와서 더해준다.
        dp.append(sum + arr[i])

    return max(dp)


n = int(input())
arr = list(map(int, input().split()))

print(sol(arr))