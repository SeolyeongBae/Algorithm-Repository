def mergeSort(arr) :
    mid = len(arr) // 2

    if len(arr) < 2:
        return arr

    Leftarr = mergeSort(arr[: mid])
    Rightarr = mergeSort(arr[mid:])

    return_array = []

    i = j = 0
    while (i < len(Leftarr) and j < len(Rightarr)):
        if Leftarr[i] > Rightarr[j]:
            return_array.append(Rightarr[j])
            j += 1
        else:
            return_array.append(Leftarr[i])
            i += 1

    return_array += Leftarr[i:]
    return_array += Rightarr[j:]

    return return_array


def findTarget(numArr, target):

    if target in numArr:
        order = numArr.index(target)
    else :
        for i in range(0, len(numArr)) :
            if numArr[i] > target :
                return i + 1

    return order + 1


def solve(nums, target) :

    return findTarget(mergeSort(nums), target)


arr= [13,59,30,40,10]

target = 59

print(solve(arr, target))