#다리끼리는 겹쳐질수 없다!!
#시간초과 + 메모리초과 ;;
#경우의 수 각각을 구하는게 아니라 그냥 스근하게 조합 해주면 되는 거였다(처음에 combination을 사용해서 속도가 엄청 느렸다)
#빠른 풀이 -> 1팩부터 30팩까지 저장해둔 어레이를 만들어서 사용한다

import math

def sol(B):
    for bridge in B :
        [N, M] = bridge
        #M개의 다리 중 N개의 조합을 뽑는 경우의수

        print(int(math.factorial(M) / (math.factorial(N) * math.factorial(M-N))))


    return 0

T = int(input())
bridges = []
for _ in range(T):
    b = list(map(int, input().split()))
    bridges.append(b)

sol(bridges)