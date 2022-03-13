#알고리즘 유형 : 완전탐색 

# 오답노트 
# 1. 파이썬은 몫을 음수로 구할 때 문제가 있다. 처음에 따로 음수일 때 처리를 해줬는데, 그냥 나누고 int 처리하는게 훨씬 타당하다.
# 2. 계속 고전한 이유는 음수 처리였다. 정답 코드를 긁어와 임의의 테스트케이스를 넣어봤는데, 내 답과 숫자가 1 차이나서 단번에 문제를 알아차렸다.
# 3. 파이썬 사용에 미숙해서, permutation 사용 등에 익숙치 못해 코드가 많이 지저분하다. 
# 4. 처음에 재귀가 돌지 않아 문제가 무엇인지 살펴봤더니, 깊은 복사와 얕은 복사 때문이었다. 슬라이싱을 통해 얕은 복사 처리를 해줬다.
# 5. 그러나 복사를 신경쓰지 않고, 함수의 인수로 연산자의 개수를 넣어주는 방법이 더 타당할 것 같다.

from collections import _OrderedDictValuesView
import sys

maxima = -sys.maxsize
minima = sys.maxsize

def sol( n, nl, ol):

    global maxima
    global minima

    if sum(ol) == 0 : 
        if nl[nums-1] > maxima : maxima = nl[nums-1]
        if nl[nums-1] < minima : minima = nl[nums-1]

    #재귀 탐색 -> 브루트포스로! 연산자를 줄세운다. 
    #하나씩 꼽아서 맨 앞에 세워보는 걸로?!

    if (ol[0]) :
        add_list = nl[:]
        add_list[nums-n+1] = add(nl, nums-n)
        aol = ol[:]
        aol[0] = aol[0] -1
        sol(n-1, add_list, aol)

    if (ol[1]) :
        sub_list = nl[:]
        sub_list[nums-n+1] = sub(nl, nums-n)
        sbol = ol[:]
        sbol[1] = sbol[1]-1
        sol(n-1, sub_list, sbol)

    if (ol[2]) :
        mut_list = nl[:]
        mut_list[nums-n+1] = mut(nl, nums-n)
        mol = ol[:]
        mol[2] = mol[2]-1
        sol( n-1, mut_list, mol)

    if (ol[3]) :
        dvi_list = nl[:]
        dvi_list[nums-n+1] = dvi(nl, nums-n)
        dol = ol[:]
        dol[3] = dol[3]-1
        sol( n-1, dvi_list, dol)
    


def add (arr, index ):
    return arr[index] + arr[index+1]
    
def sub (arr, index) :
    return arr[index] - arr[index+1]

def mut (arr, index) :
    return arr[index] * arr[index+1]
    
def dvi (arr, index) :
    
    return  int(arr[index] / arr[index+1])


nums = int(input())
num_list = list(map(int, input().split()))
opr_list = list(map(int, input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈의 개수

sol(nums, num_list, opr_list)

print(maxima)
print(minima)
