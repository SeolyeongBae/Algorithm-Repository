def sol(num) :
    p = [0, 1, 1]

    if num == 1 or num == 2: return 1

    for i in range(3, num +1):
        p.append(p[i - 1] + p [i - 2])

    return p[-1]

num = int(input())

print(sol(num))

