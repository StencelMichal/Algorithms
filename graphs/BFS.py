from queue import Queue

class Vertex:
    def __init__(self):
        self.d = 0
        self.visited = False
        self.parent = None


def BFSlist( G, source ):
    Q = Queue()
    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex()

    V[source].visited = True
    Q.put(source)
    while not Q.empty():
        parent = Q.get()
        for child in G[parent]:
            if not V[child].visited:
                    V[child].visited = True
                    V[child].d = V[parent].d + 1
                    V[child].parent = parent
                    Q.put(child)

    for v in V:
        print(v.parent)

def BFSmatrix( G, source ):
    Q = Queue()
    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex()

    V[source].visited = True
    Q.put(source)
    while not Q.empty():
        parent = Q.get()
        for c in range(len(G)):
            if G[parent][c] == 1:
                if not V[c].visited:
                        V[c].visited = True
                        V[c].d = V[parent].d + 1
                        V[c].parent = parent
                        Q.put(c)

    for v in V:
        print(v.parent )




G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]

A = [[1,5],[2,3,4],[1],[1],[1],[0,6,7],[5],[5,8],[7]]

B = [[None,1,None,None,None,1,None,None,None],
     [1,None,1,1,1,None,None,None,None],
     [None,1,None,None,None,None,None,None,None],
     [None,1,None,None,None,None,None,None,None],
     [None,1,None,None,None,None,None,None,None],
     [1,None,None,None,None,None,1,1,None],
     [None,None,None,None,None,1,None,None,None],
     [None,None,None,None,None,1,None,None,1],
     [None,None,None,None,None,None,None,1,None]]
BFSlist(A,0)
print()
BFSmatrix(B,0)
print()
BFSmatrix(G , 0)