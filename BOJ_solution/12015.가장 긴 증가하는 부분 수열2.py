#문제 유형 : 이분 탐색, 18353번 병사 배치하기와 동일하다.
#병사 배치하기는 DP로 풀 수 있지만 12015번은 오로지 이분 탐색으로만 풀 수 있다.
# bisect_left이라는 파이썬 내장함수를 사용해도 된다...

def binary_search(arr, target):
    if len(arr) == 0:
        return 0

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1

    if mid == len(arr) - 1 and arr[mid] < target:
        return len(arr)

    if arr[mid] < target:
        return mid + 1
    if arr[mid] > target:
        return mid


def sol(arr):

    if len(arr) == 1:
        return 1

    lis = []

    for i in arr:
        target_index = binary_search(lis, i)
        if target_index == len(lis):
            lis.append(i)
            continue
        lis[target_index] = i

    return len(lis)


arr_size = int(input())
num_list = list(map(int, input().split()))

print(sol(num_list))