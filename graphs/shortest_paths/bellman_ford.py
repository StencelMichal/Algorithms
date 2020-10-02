
def bellman_ford( G , source , target=None ):
    D = [float("inf")] * len(G)
    P = [None] * len(G)
    D[source] = 0

    # relaksacja wykonywana n-1 razy
    for i in range(len(G)-1):
        #relaksacja każdej krawędzi
        for v in range(len(G)):
            for c in G[v]:
                if D[c[0]] > D[v] + c[1]:
                    D[c[0]] = D[v] + c[1]
                    P[c[0]] = v

    # weryfikacja
    for v in range(len(G)):
        for c in G[v]:
            if D[v] > D[c[0]] + c[1]:
                print("NEGATIV CYCLE")
                return False

    print(D)
    print(P)

    if target != None:
        distance = D[target]
        res = [target]
        while target != source:
            res.append(P[target])
            target = P[target]
        i = 0
        j = len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return distance , res



G=[[(1,3) , (6,2)] , [(0,3),(2,2),(3,1)] , [(1,2),(4,5)] , [(1,1),(4,1),(5,7)] , [(2,5),(3,1),(8,20)] ,
   [(3,7),(8,2),(6,1),(7,1)] , [(0,2),(5,1),(7,3)] ,[(7,3),(5,1),(8,8)] , [(5,2),(7,8),(5,20)]]

route = bellman_ford( G , 0 ,6)
print(route)
