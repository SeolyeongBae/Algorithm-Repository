def backpack(num, max_w, weight, value):
    table = [[0] * (max_w + 1) for _ in range(num + 1)]

    for i in range (num + 1) :
        for w in range (max_w + 1):
            if i == 0 or w == 0 :
                table[i][w] = 0
            elif w < weight[i-1] :
                table[i][w] = table[i-1][w]
            else:
                table[i][w] = max(value[i-1] + table[i-1][w-weight[i-1]], table[i-1][w])

    return table[num][max_w]


arr= list(map(int, input().split()))

weight = []
value = []

for i in range(arr[0]):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

print(backpack(arr[0], arr[1], weight, value))

