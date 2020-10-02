
class Vertex:
    def __init__(self):
        self.visited = False

def topologicalSort( G ):
    res = []
    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex()


    def DFSVisit(parent):
        V[parent].visited = True
        for child in G[parent]:
            if not V[child].visited:
                DFSVisit(child)
        res.append(parent)

    for vertex in range(len(G)):
        if not V[vertex].visited:
            DFSVisit( vertex )
    i = 0
    j = len(res)-1
    while i < j:
        res[i] , res[j] = res[j] , res[i]
        i += 1
        j -= 1
    return res

G=[[1,5,6],[],[],[],[2,3,5],[4],[1,4],[1],[6,7],[7,8]]
arr = topologicalSort(G)
print(arr)

B = [[] , [] , [0,1] , [] , [3,2,5] , [6,7] , [] , [] ]
print()
brr = topologicalSort(B)
print(brr)