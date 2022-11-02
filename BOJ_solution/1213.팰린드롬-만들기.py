#문제 유형: 문자, 구현
#dict.keys를 몰라서 좀 헤맸다~ dict.keys()를 하면 배열로 리턴이 되지 않아서 좀 까다롭다 ㅎㅎ

def sol(name):
    pdict = {}
    for i in range(len(name)):
        if name[i] in pdict:
            pdict[name[i]] = pdict[name[i]] + 1
        else:
            pdict[name[i]] = 1

    # 팰린드롬 가능한지 체크
    odd_flag = 0
    for n in pdict.values():
        if n % 2 != 0:
            odd_flag = odd_flag + 1
        if odd_flag > 1:
            return "I'm Sorry Hansoo"

    # 팰린드롬 생성
    half = ''
    odd_char = ''

    keys = list(pdict.keys())
    keys.sort()
    for k in keys:
        if pdict[k] % 2 == 1:
            odd_char = k
            pdict[k] = pdict[k] - 1

        num = pdict[k] // 2  # 팰린드롬을 만들어야 하는 글자 수
        half = half + k * num

    reverse_half = half[::-1]

    return half + odd_char + reverse_half


name = input()

print(sol(name))
