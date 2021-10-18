def maxScore(nums) :
    nums.insert(0, 1)
    nums.append(1)

    n = len(nums)
    bowling_score = [[-1] * n for _ in range(n)]
    array_divide = 0

    for i in range(n):
        for j in range(n-i):
            k = i + j
            if k == j :
                bowling_score[j][k] = 0
                continue
            for m in range(j, k):
                temp = bowling_score[j][m]+bowling_score[m+1][k]+nums[j-1]*nums[m]*nums[k]
                if temp > bowling_score[j][k] :
                    bowling_score[j][k] = temp
                    array_divide = m

    return bowling_score[0][n-1]-nums[array_divide]



nums = [1,3,5,6,2]

print(maxScore(nums))
