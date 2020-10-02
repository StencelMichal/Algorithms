from queue import PriorityQueue

def dijkstra( G  , source , target=None):
    d = [float("inf")] * len(G)
    p = [None] * len(G)

    d[source] = 0
    Q = PriorityQueue()
    Q.put((d[source] , source))
    while not Q.empty():
        parent = Q.get()
        for child in G[parent[1]]:
            if d[child[0]] > d[parent[1]] + child[1]:
                d[child[0]] = d[parent[1]] + child[1]
                p[child[0]] = parent[1]
                Q.put((d[child[0]] , child[0]))

    print(d)
    print(p)
    if target != None:
        res = [target]
        while target != source:
            res.append(p[target])
            target = p[target]
        i = 0
        j = len(res)-1
        while i < j:
            res[i] , res[j] = res[j] , res[i]
            i += 1
            j -= 1
        return res



G=[[(1,3) , (6,2)] , [(0,3),(2,2),(3,1)] , [(1,2),(4,5)] , [(1,1),(4,1),(5,7)] , [(2,5),(3,1),(8,20)] ,
   [(3,7),(8,2),(6,1),(7,1)] , [(0,2),(5,1),(7,3)] ,[(7,3),(5,1),(8,8)] , [(5,2),(7,8),(5,20)]]
route = dijkstra(G , 0 , 8)
print(route)



