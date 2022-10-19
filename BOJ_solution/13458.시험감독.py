#알고리즘 유형 : 그냥 수학

def sol (c_num, s_arr, main, sub):

    total_supervisor = 0

    for s in s_arr:
        #메인감독관
        total_supervisor = total_supervisor + 1

        if s < main:
            continue
        else:
            remain_s = s - main
            sub_num = remain_s // sub
            sub_remain = remain_s % sub

            total_supervisor = total_supervisor + sub_num
            if sub_remain != 0 :
                total_supervisor = total_supervisor + 1


    return total_supervisor


class_num = int(input())
student_arr = list(map(int, input().split()))
supervisor =list(map(int, input().split()))

print(sol(class_num, student_arr, supervisor[0], supervisor[1]))