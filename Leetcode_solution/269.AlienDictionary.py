from queue import Queue

def LanguageOrder(words) :

    graph = {} #Use Dictionary to get the information.
    list={} #Make the adjacency list to contain the information.

    #Step 0. Setup the basic information to get information of graph
    for word in words:
        for i in word:
            if i in graph:
                continue
            graph[i] = 0 #Assign a value to the dictionary

    #Step 1. Make a graph
    words_sub = words[1:]
    for first_word, second_word in zip(words, words_sub):
        length = min(len(first_word), len(second_word))

        for k in range(0, length) :
            chr1 = first_word[k]
            chr2 = second_word[k]

            if chr1 != chr2:
                if not chr1 in list :
                    list[chr1] = set([])
                if chr2 not in list[chr1]:
                    list[chr1].add(chr2)  #denote the information for linked relation
                    graph[chr2] += 1  #denote the num of output degree
                break
            else:
                #예외처리. 만약 계속 같은 문자만 나오는데, 먼저 나오는 문자의 길이가 길다면 안 된다.
                #예시, abcd, abc 순서, 따라서 여기는 return을 해서 예외를 처리해주면 된다.
                if len(second_word) < len(first_word):
                    return ""

    #Step 2. topological sort by using queue
    dic = []

    q = Queue()
    for output, vert in graph.items(): #for topological sort, put the vertexs have no input edges into queue
        if vert == 0:
            q.put(output)

    while (not q.empty()): #until the queue empty, do topological sort.
        front = q.get()
        dic.append(front)

        if front in list:
            for e in list[front]:
                graph[e] -= 1 #delete the vertex, so the value decrese 1
                if graph[e] == 0:
                    q.put(e)

    if len(dic) < len(graph): #if it is true, it means there is a cycle in graph.
        return ""

    str = "".join(dic)
    return str

words = ["xwt","xwaf","aw","att","wftt"]
print(LanguageOrder(words))