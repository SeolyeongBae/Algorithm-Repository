def budget(evaluation):
    profit = 0

    length = len(evaluation)
    inc_num = 0
    dec_num = 0

    inc_flag = 0
    dec_flag = 0

    same_flag = 0

    for i in range(length-1):
        # 값 부여
        if evaluation[i] < evaluation[i+1] :
            if inc_flag != 1:
                inc_num = inc_num+1

            if dec_num != 0 :

                dec_flag = 1

        elif evaluation[i] == evaluation[i+1] : #같을 경우 구별

            if (evaluation[i] == evaluation[i+1] and i == 0) or (evaluation[i] == evaluation[i+1] and evaluation[i] == evaluation[i-1])  :
                profit = profit + 1

                continue
            elif dec_num != 0: #만약 감소하고 있는 중이었다면 감소를 중지

                dec_flag = 1
                profit = profit + 1
                same_flag = 1
            elif inc_num !=0: #만약 증가하고 있던 중이었다면 증가를 중지

                inc_flag = 1
                same_flag = 1


        else :
            dec_num = dec_num +1

            if inc_num !=0 :

                inc_flag = 1

        #연산 수행
        if inc_flag == 1 and ((dec_flag == 1) or (same_flag == 1) or ((i == length -2) and (evaluation[i+1]< evaluation[i]))):

            if (inc_num) >= (dec_num):
                #증가하는 횟수보다 감소하는 횟수가 적다 -> 감소의 블럭 수는 유지, 증가를 +1로 함.
                inc_num = inc_num +1
                dec_num = dec_num -1


            profit = profit + inc_num * (inc_num + 1) / 2
            inc_flag = 0

            if ((i == length -2) and (evaluation[i+1]< evaluation[i])) :
                dec_num = dec_num + 1
            inc_num = 1


        if dec_flag == 1 :
            dec_num = dec_num +1

            value = dec_num * (dec_num + 1) / 2 - 1
            profit = profit + value

            dec_num = 0
            dec_flag = 0


        if same_flag == 1:

            inc_num = 0
            dec_num = 0
            dec_flag = 0
            same_flag = 0
            continue #초기화


    if inc_num != 0 and dec_num == 0:
        inc_num= inc_num +1
        profit = profit + inc_num * (inc_num + 1) / 2
    elif dec_num != 0 and inc_num!= 0:
        profit = profit + dec_num * (dec_num + 1) / 2
    elif dec_num != 0 and inc_num == 0:
        dec_num = dec_num + 1
        profit = profit + dec_num * (dec_num + 1) / 2
    elif evaluation[length-2] == evaluation[length-1] :
        profit = profit + 1

    profit = int(profit) * 1000
    return profit


print(budget((  [2,2,1,2,2] )))