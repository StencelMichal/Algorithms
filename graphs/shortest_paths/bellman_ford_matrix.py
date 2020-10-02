def bellman_ford( G , source ):
    D = [float("inf")] * len(G)
    P = [None] * len(G)
    D[source] = 0

    # relaksacja
    for i in range(len(G)-1):
        for v in range(len(G)):
            for c in range(len(G)):
                if G[v][c] != None:
                    if D[c] > D[v] + G[v][c]:
                        D[c] = D[v] + G[v][c]
                        P[c] = v

    # weryfikacja
    for v in range(len(G)):
        for c in range(len(G)):
            if G[v][c] != None:
                if D[v] > D[c] + G[v][c]:
                    print("NEGATIV CYCLE")
                    return False

    print(D)
    print(P)

G = [[None, 3, None, None, None, None, 2, None, None],
     [3, None, 2, 1, None, None, None, None, None],
     [None, 2, None, None, 5, None, None, None, None],
     [None, 1, None, None, 1, 7, None, None, None],
     [None, None, 5, 1, None, None, None, None, 20],
     [None, None, None, 7, None, None, 1, 1, 2],
     [2, None, None, None, None, 1, None, 3, None],
     [None, None, None, None, None, 1, None, 3, 8],
     [None, None, None, None, 20, 2, None, 8, None], ]


bellman_ford(G , 0)