from queue import PriorityQueue

class Vertex:
    def __init__(self , id):
        self.id = id
        self.value = float("inf")
        self.parent = None

def prim( G ):
    MST = []
    Q = PriorityQueue()
    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex(i)
    V[0].value = 0
    Q.put((V[0].value , V[0].id))


    while not Q.empty():
        parent = Q.get()[1]
        for i in range(len(G)):
            if G[parent][i] != None:
                if V[i].value > G[parent][i] and V[parent].parent != i:
                    V[i].value = G[parent][i]
                    V[i].parent = parent
                    Q.put((V[i].value , V[i].id))

    for v in V:
        if v.parent != None:
            MST.append((v.id , v.parent))

    print(MST)

G = [[None, 3, None, None, None, None, 2, None, None],
     [3, None, 2, 1, None, None, None, None, None],
     [None, 2, None, None, 5, None, None, None, None],
     [None, 1, None, None, 1, 7, None, None, None],
     [None, None, 5, 1, None, None, None, None, 20],
     [None, None, None, 7, None, None, 1, 1, 2],
     [2, None, None, None, None, 1, None, 3, None],
     [None, None, None, None, None, 1, 3, None, 8],
     [None, None, None, None, 20, 2, None, 8, None], ]

prim(G )

