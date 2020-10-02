#Strongly connected component

class Vertex:
    def __init__(self , id):
        self.id = id
        self.timeIn = None
        self.timeOut = None
        self.visited = False
        self.scc = None

def SCC( G ):
    n = len(G)
    V = [None] * n
    for i in range(n):
        V[i] = Vertex(i)
    time = 0

    # if mark is True, algorithm will set belongnes of each Vertex to Strongly Connected Component
    def DFSVisit( vertex , scc , mark):
        nonlocal time
        if mark:
            V[vertex].scc = scc
        V[vertex].visited = True
        time += 1
        V[vertex].timeIn = time
        for child in range(n):
            if G[vertex][child] == 1 and not V[child].visited:
                DFSVisit(child , scc , mark)
        time += 1
        V[vertex].timeOut = time

    # DFS from each unvisited Vertex
    for i in range(n):
        if not V[i].visited:
            DFSVisit(i , 0 , False)

    # Reverse edges
    for i in range(n):
        for j in range(1+i , n):
            G[i][j] , G[j][i] = G[j][i] , G[i][j]

    # array of Vertexes process time in descending order
    order = [None] * len(G)
    for i in range(len(G)):
        order[i] = (V[i].id , V[i].timeOut )
    order.sort( key=lambda x: x[1] , reverse=True)

    # setting all Vertexes as unvisited
    for vertex in V:
        vertex.visited = False

    # marking belongnes to SCC
    scc = 0
    for vertex in order:
        if not V[vertex[0]].visited:
            scc += 1
            DFSVisit( vertex[0] , scc , True )


