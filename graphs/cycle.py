
class Vertex:
    def __init__(self):
        self.visited = False
        self.parent = None

def cycle ( G ):

    V = [ Vertex() for i in range(len(G))]
    isCycle = False

    def DFSVisit(parent):
        nonlocal isCycle
        V[parent].visited = True
        for child in G[parent]:
            if not V[child].visited and not isCycle:
                V[child].parent = parent
                DFSVisit(child)
            elif child != V[child].parent:
                isCycle = True

    for vertex in range(len(G)):
        if not V[vertex].visited:
            DFSVisit( vertex )

    return isCycle

G = [[1],[0,2,3],[1,3],[1,2,4],[3,5],[4]]
G2 = [ [ 1] , [2 ] , [ 3] , [ ] , [5,0 ] , [ ] ]
print(cycle(G))
print(cycle(G2))