#유형 : DP
#수열을 안써도 될거같긴 하다...
#for문을 한번만 돌아도 해결할 수 있을 것 같다.

def sol(s):

    dp_inc = [0 for _ in range(len(s))] #0으로 채워진 DP 어레이를 생성
    dp_inc[0] = 1
    ans = 1
    #dp[i] 는 s[i]를 끝점으로 가지는 수열 중에 제일 길이가 긴 경우
    #아 불연속이 아니라 연속이구나..!

    for i in range(1, len(s)):
        if s[i-1] <= s[i]:
            dp_inc[i] = dp_inc[i-1] + 1
        else:
            dp_inc[i] = 1
        if dp_inc[i] > ans:
            ans = dp_inc[i]

    s.reverse()

    dp_dec = [0 for _ in range(len(s))] #0으로 채워진 DP 어레이를 생성
    dp_dec[0] = 1

    for i in range(1, len(s)):
        if s[i-1] <= s[i]:
            dp_dec[i] = dp_dec[i-1] + 1
        else:
            dp_dec[i] = 1
        if dp_dec[i] > ans:
            ans = dp_dec[i]

    return ans

# def sol(series):
#     dec = [1 for _ in range(len(series))]
#     inc = [1 for _ in range(len(series))] #연속으로 커지는 수열
#
#     for i in range(1, len(series)) : #앞 -> 뒤로 이동하며 증가하는거 확인
#         if series[i] >= series[i -1]:
#             inc[i] = inc[i-1] + 1
#
#     for j in range(len(series)-1, 0, -1): #뒤 -> 앞으로 이동하며 감소하는거 확인
#         if series[j] <= series[j -1] :
#             dec[j-1] = dec[j] + 1
#
#     return max(max(inc), max(dec))


series_len = int(input())
series = list(map(int, input().split()))

print(sol(series))