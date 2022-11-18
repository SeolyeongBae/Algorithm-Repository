# 문제 유형 DP
# 전투력이 높은 병사가 앞으로 와야 한다
# 중간중간 전투력이 낮은 애를 삭제하면서도 병사의 수가 최대 -> 가장 긴 증가하는 수열이랑 맥락이 비슷하다.


# 이분 탐색을 사용한 풀이
# 이해가 안 갔던 부분: 11053 풀이에 기록한 오답과 같은 접근인데, 대체 왜 저게 되지? 였음
# 안된다고 생각했던 이유가 1 2 6 8 5 6 7 일때 맨 뒤에것만 심사를 해서  1, 2, 6 ,8에서 1, 2, 5 로 바꿔야 할때 커버가 안된다.
# 하지만 dp와 다르게 생각할 게, 여기서 따로 만드는 어레이는 최종 결과가 아니라 단지 길이를 리턴하기 위한 점이라는 거. 즉 그 어레이는 진짜 어레이가 아니다
# 즉 위와 같은 상황에서 들어온 배열이 1 2 6 8 5 일떄  1, 2, 6, 8 으로 만든 상태에서 5를 만나면 1, 2, 5가 되는게 아니라 1, 2, 5, 8으로 갱신되는 거다.
# 벡터의 길이는 여전히 4니까 최종 길이는 변화하지 않는다! -> 이분 탐색을 사용해서 어디에 넣을 지 결정하는 알고리즘임

def binary_search(arr, target): #target보다 큰 수가 나오는 처음 나오는 index를 return하는 binary search
    if len(arr) == 0:
        return 0
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid #arr에 중복이 있는 경우 중복처리도 해줘야 할 듯 함, 하지만 증가한다는 전제라 없다!!

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
    #end를 리턴해도 되나?!

def sol(arr):
    arr.reverse()

    if len(arr) == 1:
        return 0

    lis = []

    for i in arr:
        target_index = binary_search(lis, i)
        if target_index == len(lis):
            lis.append(i)
            continue
        lis[target_index] = i

    return len(arr) -len(lis)


army_num = int(input())
army_list = list(map(int, input().split()))

print(sol(army_list))

'''
DP를 사용한 풀이

def sol(arr):

    if len(arr) == 1:
        return 0

    dp = [1]
    #dp[i] = 조건을 만족하면서 남아있는 가장 긴 병사의 수가 최대인 경우

    #n log n이니까... merge sort와 비슷하게 하면 되나?
    #머지소트처럼 두개씩 쪼갠 다음에 하나씩 붙이는거임
    #그러면 자동으로 합병했을 때

    for i in range(1, len(arr)):
        max_length = 0

        for j in range(i):
            #내가 더 큰 상황
            if (arr[j] > arr[i]) and (dp[j] > max_length):
                max_length = dp[j]

        dp.append(max_length + 1)

    print(dp)
    return len(arr) - max(dp)

'''
