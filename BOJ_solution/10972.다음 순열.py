#문제 유형: 구현, 다음 순열 알고리즘

'''
알고리즘 설명:
1, 7, 4, 8, 6, 5, 2의 순서대로 배열이 있다고 하자.

뒤에서부터 배열을 탐색하면서 배열이 "작아지는"순간을 찾는다.
위의 경우 8에서 5를 가는 순간 작아진다.

그러면 4를 i번째, 8을 i+1번째로 한다.
그 다음에, 다시 뒤쪽부터 탐색하면서 4보다 큰 첫 번째 수를 찾는다.
5다.
그러면 5를 j번째라고 한다.


그러면 i와 j를 swap 해준다.

1, 7, 5, 8, 6, 4, 2
그 다음에 5 다음인 8부터 배열 끝까지 정렬해준다. 단 이때 8까지는 계속 증가하던 순서였고, 5와 4가 바뀌어도 뒤에서부터 8까지는 계속 증가한다.
즉 5 다음의 나오는 수를 뒤집는다.

답은 1, 7, 5, 2, 4, 6, 8 이당.


이 알고리즘이 어떤 것을 뜻하냐면, 뒤에서부터 갔을때 계속 수열이 증가하고 있다면 정렬 된 형태라는 뜻이다. (더이상 바꿀 여지가 없음)
arr[i] <= arr[i+1] 인 게 처음 등장했다면 arr[i+1] 부터 끝까지는 감소하는 형태로 정렬되었다.
그렇다면 arr[i:] 안에서 next permutation 을 찾아야 하는데, arr[i] 보다 바로 다음 번째로 큰 숫자를 찾아야 한다.
이때 위 알고리즘에서 arr[i] 보다 큰 첫 번쨰 수를 찾는다는 의미는, arr[i+1:]이 정렬되어 있기 때문에 arr[i:] 내부에서 arr[i] 보다 큰 바로 다음 수를 찾는 것과 마찬가지다.
그래서 arr[i] 와 arr[j] 을 swap해주고, 그 뒤에 있는 요소를 전부 뒤집어주면 된다.

보통 permutaion 을 만들 때는 재귀적인 방법을 사용하니까 그런 식으로 접근하려고 했다.
다만 이번 문제를 알려면 좀 더 새로운 시각으로 배열을 볼 줄 알아야 했고, '증가하는 순서'가 '정렬됨'과 비슷한 의미라는 걸 알아야 했다.
또 감소하는 방향으로 정렬된 건 그 숫자로 만들 수 있는 제일 마지막 순열이라는 사실을 꺠닫지 못해서 알고리즘을 이해하는 데 오랜 시간이 걸렸다.
답을 보고 풀었다.
'''

n = input()
arr = list(map(int, input().split()))

def sol(arr):
    target = -1
    swap_target = -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i -1] <= arr[i]:
            target = i -1
            break

    if target == -1:
        print(-1)
        return

    for j in range(len(arr)-1, target, -1):
        if arr[j] > arr[target]:
            swap_target = j
            break

    temp = arr[target]
    arr[target] = arr[swap_target]
    arr[swap_target] = temp

    tail_arr = arr[target +1 :]
    ans = arr[:target + 1] + tail_arr[::-1]

    print(*ans)

sol(arr)

