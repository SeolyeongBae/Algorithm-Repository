#시작 시간: 8시 31분 -> 42분에 해결
#유형: 단순한 구현

def solution(survey, choices):
    score = {
        'A': 0,
        'N': 0,
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
    }

    for i in range(len(survey)) :
        #비동의, 동의
        s = survey[i]
        c = choices[i]

        if c > 4 :
            score[s[1]] += c - 4
        elif c < 4 :
            score[s[0]] += 4 - c

    mbtis = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    answer = ''

    for m in mbtis :
        if score[m[0]] < score[m[1]]:
            answer += m[1]
        else:
            answer += m[0]

    return answer

