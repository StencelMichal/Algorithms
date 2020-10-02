
def pArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="  ")
        print()

def floyd_warshall( G , routes=False):
    n = len(G)

    D = [None] * n
    P = [None] * n
    for i in range(n):
        D[i] = [float("inf")] * n
        P[i] = [None] * n

    for i in range(n):
        for j in range(n):
            if G[i][j] != None:
                D[i][j] = G[i][j]

    for i in range(n):
        D[i][i] = 0
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

    pArr(D)

    def route(i , j):
        nonlocal r
        if P[i][j] != None:
            route(i, P[i][j])
            r += "|"
            r += str(P[i][j])
            r += "|"
            route(P[i][j], j)

    if routes:
        print("ROUTES:")
        for i in range(len(G)):
            for j in range(len(G)):
                if i != j:
                    print(i, "->" , j ," ", end="")
                    r ="|"+str(i)+"|"
                    route(i , j)
                    r += "|" + str(j) + "|"
                    print(r,end=" ")
                    print("cost:" , D[i][j])



G = [[None,3,None,None,None,None,2,None,None],
     [3,None,2,1,None,None,None,None,None],
     [None,2,None,None,5,None,None,None,None],
     [None,1,None,None,1,7,None,None,None],
     [None,None,5,1,None,None,None,None,20],
     [None,None,None,7,None,None,1,1,2],
     [2,None,None,None,None,1,None,3,None],
     [None,None,None,None,None,1,None,3,8],
     [None,None,None,None,20,2,None,8,None],]

floyd_warshall(G , True)

#G=[[(1,3) , (6,2)] , [(0,3),(2,2),(3,1)] , [(1,2),(4,5)] , [(1,1),(4,1),(5,7)] , [(2,5),(3,1),(8,20)] ,
 #  [(3,7),(8,2),(6,1),(7,1)] , [(0,2),(5,1),(7,3)] ,[(7,3),(5,1),(8,8)] , [(5,2),(7,8),(4,20)]]


