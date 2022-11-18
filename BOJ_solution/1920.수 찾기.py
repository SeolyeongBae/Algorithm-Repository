#문제 유형 : 이분탐색
#이분탐색을 구현해보자!

#문제 유형 : 이분탐색
#이분탐색을 구현해보자!

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1 #mid가 아니니까 mid -1 을 한다.
        elif arr[mid] < target:
            start = mid + 1

    return -1


def sol(nums, targets):
    nums.sort()

    for t in targets:
        search_result = binary_search(nums, t)

        if search_result == -1:
            print(0)
        else:
            print(1)



ns = int(input())
num_list = list(map(int, input().split()))

ts= int(input())
target_list = list(map(int, input().split()))

sol(num_list, target_list)




