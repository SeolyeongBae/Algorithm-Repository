import sys
num = int(input())
stack = []

for _ in range(num):
    a = sys.stdin.readline().split()

    c = a[0]
    if c == 'push':
        number = a[1]
        stack.append(number)

    if c == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    if c == 'size':
        print(len(stack))

    if c == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if c == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)


