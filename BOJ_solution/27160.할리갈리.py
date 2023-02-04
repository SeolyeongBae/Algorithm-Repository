def sol(h):

    for k, v in h.items():
        if v == 5 : return 'YES'
    return 'NO'

num = int(input())
h = {}

for _ in range(num):
    f, n = input().split()
    n = int(n)
    if (f in h.keys()):
        h[f] += n
    else:
        h[f] = n

print(sol(h))