list = [3]


def moo(num):
    for i in range(1, num+1) :
        list.append (list[i - 1] * 2 + (i + 3))
        if (list[i] > 1e9) :
            return



def count_moo(num):
    m = 1

    if num == 1:
        return 'm'

    while num > list[m]:
        m += 1
    #num < list[m] 의 상태임. list[num]이 아니라, 가장 num과 근접한 list[m]의 값을 잡아줌.(포인트인듯!)
    #이떄 num > list[m -1] 이다.

    if num + list[m -1] <= list[m] : # list[m] = list[m-1] + m+3 + list[m-1]. 이거는 num이 저기 앞쪽~ m+3에 포함돼있는지 묻는 거.
        if( num - list[m-1] == 1 ) : #mooo... 의 m일 경우.
            return 'm'
        else :
            return 'o' # 중간에 있으나 m가 아닌 경우?? 모르겠네
        #무조건 num > list[m -1] 인 걸로 했으니까 경우는 중간 구간 아니면 뒷 구간밖에 경우가 안나옴. 따라서 앞구간 문제는 고려하지 않아도 됨.


    return count_moo(num - list[m - 1] - m - 3) #뒷부분?


integer = int(input())

moo(integer)

print(count_moo(integer))
