#오답노트!
#처음 접근 : value 를 만드는 방법은 value-coins[0]+value-coins[1]+...+value-coins[coin_num]이다!
#그러나 틀린 이유: 그렇다면 3을 만드는 방법은 3-2= 1을 만드는 방법과 3-1= 2를 만드는 방법의 합이다
#하지만, 그렇다면 1을 만드는 방법은 1이므로 1+2, 2을 만드는 방법은 1+1, 2이므로 1+1+1, 2+1이다. 하지만 순서는 신경쓰지 않으므로 1+2와 2+1가 겹친다 => 멘붕
#답은 동전 하나로만 만드는 방법으로 배열을 채우고, 그 다음에 동전 하나를 더 넣어서 만드는 방법을 구하고... 하는 형식이다. 이 방식을 잘 생각하지 못했다.


def coin (coin_num, value, coins) :

    arr = [0] * (value+1)

    #index of arr : index라는 값을 만들 수 있는 경우의 수

    # for i in range(value+1) :
    #     if i in coins :
    #         arr[i] = arr[i] + 1

    #     for j in coins :
    #         if i - j >= 0 :
    #             arr[i] = arr[i]+arr[i-j]

    for i in coins :
        for j in range(value+1):
            if j == i :
                arr[j] = arr[j] +1

            if j - i >= 0:
                arr[j] = arr[j]+arr[j-i]

    return arr[value]



input_list = list(map(int, input().split()))
coin_value = []

for i in range(input_list[0]) :
    temp = int(input())
    coin_value.append(temp)

print(coin(input_list[0], input_list[1], coin_value))

