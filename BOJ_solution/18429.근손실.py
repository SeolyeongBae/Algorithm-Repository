from itertools import permutations

#유형 : 완전탐색

def sol(days, dec, kit):
    #days늰 kit의 수와 같다.
    kit_numbers = permut(kit, days)
    # kit_numbers = list(permutations(kit)) , 모듈을 사용해서 문제를 해결하는 경우
    answer = 0

    for routine in kit_numbers :
        power = 500
        for inc in routine:
            power = power + inc - dec
            if power < 500:
                break
        if power >= 500:
            answer = answer + 1

    return answer

#permutation 을 쓰지 못하는 경우를 대비하여 직업 함수 구현해보기
#list 중에서 k개 뽑는 경우
def permut(targets, k):
    length = len(targets)
    i_array = list(range(length))
    return_arr = []

    def generate(chosen, index_arr):
        if len(chosen) == k:
            return_arr.append(chosen)
            return

        if len(index_arr) == 0:
            return

        for i in index_arr:
            chosen_arr = chosen[::]
            chosen_arr.append(targets[i])

            new_index_arr = index_arr[::]
            new_index_arr.remove(i)

            generate(chosen_arr[::], new_index_arr)

    generate([], i_array)

    return return_arr


exercise_info = list(map(int, input().split()))
exercise_kit = list(map(int, input().split()))

print(sol(exercise_info[0], exercise_info[1], exercise_kit))
