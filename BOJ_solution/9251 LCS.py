def LCS(str1, str2) :
    lcs = ""
    len1 = len(str1) + 1
    len2 = len(str2) + 1
    dp= [[0] * len1 for _ in range(len2)] #첫줄을 0으로 채우려고(out of range 방지), 따라서 앞으로 index는 -1 해주면 됨.

    for i in range(1, len2):
        for j in range(1, len1):
            letter1 = str1[j-1]
            letter2 = str2[i-1]
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

            if letter1 == letter2 and dp[i][j] < dp[i-1][j-1] + 1 :
                dp[i][j] = dp[i-1][j-1] + 1

    if dp[len2-1][len1-1] == 0 :
        return 0

    i = len2-1
    j = len1-1

    while(i!=0 and j!=0) :
        letter1 = str1[j - 1]
        letter2 = str2[i - 1]
        if letter1 == letter2:
            lcs = lcs + letter1
            i = i-1
            j = j-1
        elif dp[i][j-1] > dp[i-1][j] :
            j = j -1
        else :
            i = i-1

    return lcs



string1=input()
string2=input()
str = LCS(string1, string2)

if str == 0:
    print(0)
else :
    print(len(str))
    print(str[::-1])
