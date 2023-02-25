def isPalindrome(x):
    x = str(x)

    if len(x) % 2 == 0:
        num = len(x) // 2
        f = x[:num]
        e = x[num:][::-1]

        return f == e

    mid = len(x) // 2
    f = x[:mid]
    e = x[mid+1:][::-1]

    return f == e

# return str(x) == str(x)[::-1] 팰린드롬인지 따질떄는 그냥 이거만 해도 됐다는 걸 늦게 알았다...

print(isPalindrome(12321))