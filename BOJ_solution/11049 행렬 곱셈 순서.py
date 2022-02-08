import sys

def minScore(nums) :

    n = len(nums)
    bowling_score = [[0] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(1, n-i):
            k = i + j
            if k == j :
                bowling_score[j][k] = 0
                continue
            bowling_score[j][k] = sys.maxsize

            for m in range(j, k):
                temp = bowling_score[j][m]+bowling_score[m+1][k]+nums[j-1]*nums[m]*nums[k]
                if temp < bowling_score[j][k] :
                    bowling_score[j][k] = temp

    return bowling_score[1][n-1]

n = int(input())
nums = []
for i in range(n) :
    arr = [list(map(int, input().split()))]
    if (i == 0) :
        nums.append(arr[0][0])
    nums.append(arr[0][1])

print(minScore(nums))
