# 문제!!! 인덱스로만 센다고 해도, 자리수가 안 맞는거 같은데 어떡하지? --> 뒤집어보자.
# 와 진짜 어렵네... AB BB 이거 어떻게 함?
# 정답 -> 가중치

def sol(words):
    locations = {}
    alphabets = set({})
    matching = {}

    for w in words:
        for i in range(len(w)):
            alphabets.add(w[i])
            if i not in locations:
                locations[i] = [w[i]]
            else:
                locations[i].append(w[i])

    numbers = list(locations.keys())
    numbers.sort()
    numbers.reverse()

    number = 9

    for n in numbers:
        w = locations[n]
        for i in range(len(w)):
            if w[i] not in matching:
                matching[w[i]] = pow(10, n)
            else:
                matching[w[i]] = matching[w[i]] + pow(10, n)

    max_keys = list(dict(sorted(matching.items(), key=lambda item: item[1])).keys()) #딕셔너리 정렬해서 값 큰 순서대로 갖고옴
    max_keys.reverse()

    ans = 0
    for k in max_keys:
        ans += number*matching[k]
        number -= 1

    return ans


N = int(input())
words = []

for _ in range(N):
    words.append(input()[::-1])

print(sol(words))


'''

오답노트

첫 번째 시도 -> 그냥 자리수가 높은 곳에서 많이 나온 숫자가 더 높은 숫자를 가져간다고 생각했음.
AB
CB
같은 경우를 생각했는데 B가 9고 A가 8이어도 A가 9인 경우가 압도적이라고 생각했음
하지만 
AB
BB 같은 경우를 생각한다면..? A는 고작 10의 힘을 쓰지만 B는 12만큼이라서, 내 가정이 틀렸음.
이런 문제에서 중요한 건 어떻게 조건을 따지냐는 건데 가중치라는 걸 사용하면 된다는 걸 깨달았음.

def most_frequent(data):
    return sorted(data, key=lambda x: (-data.count(x), data.index(x)))


def sol(words):
    locations = {}
    alphabets = set({})
    matching = {}
    #일단 알파벳이 고정되어 있지 않음
    #그리디하게 생각했을 때, 가장 높은 자리에 많이 등장한 알파벳이 제일 큰 수를 가지고 가는게 타당함. -> 틀린 판단!! 

    for w in words:
        for i in range(len(w)):
            alphabets.add(w[i])
            if i not in locations:
                locations[i] = [w[i]]
            else:
                locations[i].append(w[i])

    numbers = list(locations.keys())
    numbers.sort()
    numbers.reverse()

    number = 9

    for n in numbers:
        sorted_words = most_frequent(locations[n])
        most = sorted_words[0]

        #만약에 없을 경우
        while True:
            if (most in alphabets):
                alphabets.remove(most)
                matching[most] = number
                number -= 1
            sorted_words = [x for x in sorted_words if x != most]
            if len(sorted_words) == 0: break
            most = sorted_words[0]

    print(locations)
    print(matching)
    ans = 0
    for n in numbers:
        arr = locations[n]
        for i in range(len(arr)):
            print(arr[i], n)
            ans += matching[arr[i]]*pow(10, n)

    print(ans)

    return ans

'''