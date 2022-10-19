# -*- coding: utf-8 -*-
#문제 유형 : 그리디, 구현

# 아이디어 : 비어 있으면 꽂고, 이때 같은 거 있으면 안꽂고, 꽉 차 있으면 안 쓸 걸 뽑는다

#오답노트

#근데 여기서 꽉 차있을 경우 '나중에' 테스크가 잡히는 친구를 뽑았어야 했다 이걸 배열 전체 범위로 생각했어야 했는데 플러그 개수만큼만 생각해버렸다.
#또, 생각을 잘못했던 게 나중에 테스크가 오는게 아니라 테스크가 있는 빈도가 적은 애를 뽑아야 한다고 오판했다. 테스크가 적어도 많은 애보다 앞에 오면 아직 뽑지 말아야 한다.
#구현의 어려웠던 점도 그렇다. maximum = index_list.index(max(index_list))이 부분 코드 (78번쨰 줄 부근)을 생각하기 어려웠다.
#최댓값을 가지는 것의 인덱스를 리턴하는 건데, 이때 if ... in을 사용했다. 따라서 저 인덱스는 플러그의 인덱스와 동일하다.
#if 문을 유연하게 짜는 방법을 생각해봐야겠다.


def sol(holes, num, list) :

    plug = 0 

    sub_array = [0] * (num+1)
    sub_slice_array = [0] * (num+1)

    concent = [0] * holes

    list = list + [0] * (holes-1) #슬라이싱을 위한 꼬리붙이기

    for i in list :
        sub_array[i] = sub_array[i] + 1 #제로인덱싱을 사용하지 않는다.

    for j in range(num) :
        
        empty = -2
        last = []

        if list[j] == 0 :
            break

        #뭘 뽑을건지 찾는다
        for k in range(holes) :
            if concent[k] == list[j] : #만약에 빈 공간이 있더라도, 같은 태스크가 있으면 일단 그거부터 실행한다 
                sub_array[ list[j] ] = sub_array[ list[j] ] -1 
                empty = -1
                break
            elif not concent[k] : #비어 있는 콘센트가 있는 경우
                empty = k
            elif sub_array[concent[k]] == 0 :
                last.append(k)
        
        if empty == -2 : #꽂을 자리 없어서 쫓겨난 경우다, 이제 뭘 뽑을지 정해야 한다
            #만약 앞으로 꼽을 일 없는 콘센트일 경우
            if last : #하나는 있다는 뜻이다!
                plug = plug + 1
                concent[last[0]] = list[j] #아무거나, 걍 0을 골라준다.
                sub_array[ list[j] ] = sub_array[ list[j] ] -1  #테스크를 빼준다
                continue

            #나포함 num개의 코드를 중에 내가 여길 꼽지 않으면 겹치는게 있다는 걸 아는 경우
            slice_array = list[j :] #내 뒤에 task들...

            for i in range( len(slice_array)) :
                if not sub_slice_array[slice_array[i]] :
                    sub_slice_array[slice_array[i]] = i
                else :
                    sub_slice_array[slice_array[i]] = min(i,sub_slice_array[slice_array[i]])
            #쭉 돌면서 남은 것들이 가장 일찍 나오는 인덱스를 서브 슬라이스 어레이에 저장한다.

            hole_target = -1
            index_list = []
            maximum = -1

            for k in range(holes) :
                #그리고 구멍 중에 가장 큰 인덱스를 가지는 애를 뽑는다
                # if sub_slice_array[concent[k]] > maximum :
                #     maximum = sub_slice_array[concent[k]] 
                #     hole_target = k
                if concent[k] in slice_array:
                    # 멀티탭 인덱스 위치 값 가져오기.
                    hole_target = slice_array.index(concent[k])
                
                index_list.append(hole_target)


            maximum = index_list.index(max(index_list))
            plug = plug + 1
            concent[maximum] = list[j]
            sub_array[ list[j] ] = sub_array[ list[j] ] -1  #테스크를 빼준다
                
        if empty >= 0 :
           #0보다 크면 같은 태스크가 없지만, 빈자리는 있다는 뜻이다.
           concent[empty] = list[j] # 콘센트를 꼽아준다
           sub_array[ list[j] ] = sub_array[ list[j] ] -1 #남은 일을 1 줄여준다
    
    #print(sub_array)
    #print(concent)

    return plug



condition = list(map(int, input().split()))
tasks = list(map(int, input().split())) 

hole = condition[0]
tot_task = condition[1]

print(sol(hole, tot_task, tasks))
