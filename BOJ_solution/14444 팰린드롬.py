def LCS(str1, str2) :
    lcs = ""
    len1 = len(str1) + 1
    len2 = len(str2) + 1

    k = 2
    check = 0
    dp = [[0] * len1 for _ in range(k)]  # 첫줄을 0으로 채우려고(out of range 방지), 따라서 앞으로 index는 -1 해주면 됨.

    while (k<=len2) :
        # 제한조건 : 만약 중간까지 갔는데 일치하는 게 없으면... 그 b인덱스 뒤쪽부터는 날려도 되지 않을까?
        # 예시, beakj 까지 맞는 게 없음. 그러면 세로 인덱스로 쭉 내려갈때 j번 이후로는 그냥 냅다 리턴해도 되는 거 아닐까?
        #baekjoon
        #noojkeab 여기서 한 줄씩 늘릴때, k가 2일때 처음 만나게 된다. 그러며는 이떄 만나는 애가 j다 k가 append할때 j부터는 필요 없이 걍 냅다 리턴해도 된다는 뜻이지?

        i = k-1
        for j in range(1, len1):
            letter1 = str1[j-1]
            letter2 = str2[i-1]
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

            if letter1 == letter2 and dp[i][j] < dp[i-1][j-1] + 1 :
                if dp[i][j] == 0 and check == 0 : flag = j
                check = check +1
                dp[i][j] = dp[i-1][j-1] + 1

        k = k + 1

        if k == len1 - flag +2 :
            break
        dp.append([0] * len1)

    return dp[k-2][len1-1]



string1=input()
string2=string1[::-1]

print(LCS(string1, string2))

