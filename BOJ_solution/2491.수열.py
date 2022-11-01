#유형 : DP
#수열을 안써도 될거같긴 하다...
#for문을 한번만 돌아도 해결할 수 있을 것 같다.

def sol(series):
    dec = [1 for _ in range(len(series))]
    inc = [1 for _ in range(len(series))] #연속으로 커지는 수열

    for i in range(1, len(series)) : #앞 -> 뒤로 이동하며 증가하는거 확인
        if series[i] >= series[i -1]:
            inc[i] = inc[i-1] + 1

    for j in range(len(series)-1, 0, -1): #뒤 -> 앞으로 이동하며 감소하는거 확인
        if series[j] <= series[j -1] :
            dec[j-1] = dec[j] + 1

    return max(max(inc), max(dec))


series_len = int(input())
series = list(map(int, input().split()))

print(sol(series))