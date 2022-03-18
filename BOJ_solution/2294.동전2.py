#문제 유형 : DP
#동전 1에서 실패한 접근이 여기서는 먹혔다. 앞으로 DP를 풀때 최적의 해를 구하는 건지, 또는 모든 경우를 따지는 건지 잘 고려해봐야겠다. 모든 경우를 고려하는 경우에는 계산의 간결화를 위해 DP를 쓰는 셈이다!!

def coin (coin_num, value, coins) :

    arr = [100101] * (value+1)

    #index of arr : index라는 값을 만들 수 있는 경우의 수

    for i in range(value+1) :

        if i in coins :
            arr[i] = 1

        for j in coins :
            if i - j >= 0 :
                arr[i] = min(arr[i], arr[i-j]+1)


    if arr[value] >= 100101 :
        return -1
    else :
        return arr[value] 


input_list = list(map(int, input().split()))
coin_value = []

for i in range(input_list[0]) :
    temp = int(input())
    coin_value.append(temp)

print(coin(input_list[0], input_list[1], coin_value))

