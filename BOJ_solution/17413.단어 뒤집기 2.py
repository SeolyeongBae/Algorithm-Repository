# 단어 뒤집기 2... 정규표현식을 사용하는 걸까?
# 규칙 1. 태그 단어 안쪽은 뒤집지 않는다
# 규칙 2. 띄어쓰기만 뒤집는다

# 풀이 후기: 이런 문제의 경우 어떻게 규칙을 세울 수 있는 지 잘 모르겠다.

s = input()

l_slice = s.split('<')
r_slice = []

for i in l_slice:
    s = i.split('>')

    #일단 <, > 로 나눈다.

    if len(s) == 1: #tag가 포함되어 있지 않은 경우
        splitted_b = s[0].split()
        reversed_b = [i[::-1] for i in splitted_b]
        r_slice.append(' '.join(reversed_b))

    if len(s) >= 2: #tag가 포함된 경우에는 > 뒤쪽에 나오는 문자가 tag 바깥 문자이므로, 바깥 문제에 대해서만 reverse 처리릏 해준다.
        b = s[1]
        splitted_b = b.split()
        reversed_b = [i[::-1] for i in splitted_b]
        s[1] =' '.join(reversed_b)

        r_slice.append('>'.join(s))

print('<'.join(r_slice))