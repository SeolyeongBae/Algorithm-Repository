
#유형: DP
#1차 시도: 2차원 테이블 만들고 구현
#2차 시도: proift를 비교해서 값을 넣었을 떄 더 큰 경우를 고려하지 못함
#3차 시도: 반례 발견, 로직을 뒤에서 거꾸로 오면서 값을 넣는것으로 수정함.

def sol (table):
    dp = [0] * (len(table)+ 1)
    week = [-1] * (len(table))
    #0일차부터 시작

    # max(dp[i]) = i일차에 얻을 수 있는 maximum profit
    # dp[i] 는 i일차의 상담을 시작하거나 혹은 시작하지 않은 경우의 상담 상태다.

    for i in range(len(table)-1, -1, -1):

        appointment = table[i]
        times = appointment[0]
        profits = appointment[1]

        #만약에 초과하는 경우 넘겨준다
        if (i + times) > len(table):
            dp[i] = dp[i+1]
        else:
            dp[i] = max(profits + dp[i+times], dp[i+1])

    return max(dp)


day = int(input())
meeting_table = []

for _ in range(day):
    schedule = list(map(int, input().split()))
    meeting_table.append(schedule)


print(sol(meeting_table))


###틀린 답

'''
def wrong_sol (table):

    record = [[-1]* len(table)]
    #0일차 주간
    #안에 있는건 주차별

    dp = [0]
    #0일차부터 시작

    # max(dp[i]) = i일차에 얻을 수 있는 maximum profit
    # dp[i] 는 i일차의 상담을 시작하거나 혹은 시작하지 않은 경우의 상담 상태다.

    for i in range(len(table)):
        appointment = table[i]
        times = appointment[0]
        profits = appointment[1]

        prev = record[i][::]

        if (i + times) > len(table):
            #7일인 경우에 6일째 인덱스는 5, 가능한 숫자는 2, 합쳐서 7넘으면 안됨
            record.append(prev)
            dp.append(dp[i])
            continue

        if prev[i] == -1:
            #일단 비어있으면 채울수 있을떄 무조건 채운다.
            for k in range(times):
                prev[i+k] = (i+1)
            #일정표를 채워준다.

            dp.append(dp[i] + profits)
        else:
            #넣을 자리가 없다면 전에 어디서 넣을수 있는지 탐색
            max_profit = -1

            for t in range(i+1):
                target = record[i-t]

                if (dp[i - t] + profits) < dp[i]:
                    continue

                if target[i] == -1 and max_profit < dp[i - t]:
                    prev = target[::]
                    max_profit = dp[i - t]

            if (max_profit + profits) < dp[i]:
                record.append(record[i][::])
                dp.append(dp[i])
                continue

            for k in range(times):
                prev[i+k] = (i+1)

            dp.append(max_profit + profits)

        record.append(prev)
    return max(dp)
    
'''