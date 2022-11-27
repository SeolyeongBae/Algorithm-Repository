#문제 유형: 탐색, 트리, 재귀
#항상 A가 루트 노드가 된다.
#진심으로 15분컷 했다... 출력 시간을 조금 더 줄이려면 배열에 append 하는 거 대신에 print(aa, end="") 로 하는 방법도 좋을 듯~

def pre_order(tree, r, o): #전위순회 Root -> L -> R
    if r == '.': return
    o.append(r)

    pre_order(tree, tree[r][0], o)
    pre_order(tree, tree[r][1], o)

def in_order(tree, r, o): #중위순회 L -> Root -> R
    if r == '.' : return
    in_order(tree, tree[r][0], o)
    o.append(r)
    in_order(tree, tree[r][1], o)


def post_order(tree, r, o): #후위순회 L -> R -> Root
    if r == '.' : return
    post_order(tree, tree[r][0], o)
    post_order(tree, tree[r][1], o)
    o.append(r)



def sol(tree):

    pre = []
    ino = []
    post = []

    pre_order(tree, 'A', pre)
    in_order(tree, 'A', ino)
    post_order(tree, 'A', post)

    print("".join(pre))
    print("".join(ino))
    print("".join(post))

    return 0


nodes = int(input())
t = {}
for _ in range(nodes):
    P, L, R = input().split()
    t[P] = (L, R)

sol(t)