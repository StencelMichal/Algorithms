#reprezentacja listowa grafu
class Vertex:
    def __init__(self ):
        self.visited = False
        self.parent = None
        self.timeIn = None
        self.timeOut = None

def DFSlist( G ):

    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex()

    def DFSvisit(parent):
        nonlocal time
        time += 1
        V[parent].visited = True
        V[parent].timeIn = time
        for child in G[parent]:
            if not V[child].visited:
                V[child].parent = parent
                DFSvisit(child)
        time += 1
        V[parent].timeOut = time

    time = 0
    DFSvisit( 0 )

    for v in V:
        print(v.parent , v.timeIn , v.timeOut)

def DFSmatrix( G ):

    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex()

    def DFSvisit(parent):
        nonlocal time
        time += 1
        V[parent].visited = True
        V[parent].timeIn = time
        for c in range(len(G)):
            if G[parent][c] == 1:
                if not V[c].visited:
                    V[c].parent = parent
                    DFSvisit(c)
        time += 1
        V[parent].timeOut = time

    time = 0
    DFSvisit( 0 )

    for v in V:
        print(v.parent , v.timeIn , v.timeOut)



G = [[1,2],[0,2,3],[3,1,0],[]]
A = [[1,5],[2,3,4],[1],[1],[1],[0,6,7],[5],[5,8],[7]]
DFSlist(G)
print()
DFSlist(A)
print()
B = [[None,1,None,None,None,1,None,None,None],
     [1,None,1,1,1,None,None,None,None],
     [None,1,None,None,None,None,None,None,None],
     [None,1,None,None,None,None,None,None,None],
     [None,1,None,None,None,None,None,None,None],
     [1,None,None,None,None,None,1,1,None],
     [None,None,None,None,None,1,None,None,None],
     [None,None,None,None,None,1,None,None,1],
     [None,None,None,None,None,None,None,1,None]]

DFSmatrix(B)
