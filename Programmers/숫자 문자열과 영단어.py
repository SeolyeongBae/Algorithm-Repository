# 시작: 8시 48분
# 종료: 9시 14분... 정말 힘겹게 풀었으나 파이썬은 replace라는 비장의 무기가 있기 때문에 안 사용한 내가 바보가 되었다.

def solution(s):

    answer = ''

    initial = {
        'ze': [4, 0],
        'on': [3, 1],
        'tw': [3, 2],
        'th': [5, 3],
        'fo': [4, 4],
        'fi': [4, 5],
        'si': [3, 6],
        'se': [5, 7],
        'ei': [5, 8],
        'ni': [4, 9]
    }

    while(len(s)!= 0) :
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            word_info = initial[s[:2]]
            answer += str(word_info[1])
            s = s[word_info[0]:]

    return int(answer)
