import math

def merge_sort(arr, level) :
    mid = len(arr) // 2

    if len(arr) < 2 :
        return arr

    Leftarr = merge_sort(arr[ : mid], level)
    Rightarr = merge_sort(arr[mid : ], level)

    return_array = []

    if (len(Leftarr) >= level and len(Rightarr) >= level) :
        return_array += Leftarr
        return_array += Rightarr
        if (len(Leftarr) == level and len(Rightarr) == level):
            print(*return_array)
        return []

    i = j = 0
    while ( i < len(Leftarr) and j < len(Rightarr) ):
        if Leftarr[i] > Rightarr[j]:
            return_array.append(Rightarr[j])
            j += 1
        else:
            return_array.append(Leftarr[i])
            i += 1

    return_array += Leftarr[i:]
    return_array += Rightarr[j:]

    return return_array



chicken_num = int(input())
taste_score = list(map(int, input().split()))
people = int(input())

merge_sort(taste_score, chicken_num/people)

# level = int(math.log2(chicken_num)) - int(math.log2(people))
