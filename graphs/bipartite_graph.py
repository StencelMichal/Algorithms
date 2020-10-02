
class Vertex:
    def __init__(self):
        self.color = None


def bipartite( G ):

    V = [None] * len(G)
    for i in range(len(G)):
        V[i] = Vertex()

    ret = True

    def DFS(parent):
        nonlocal ret
        for child in G[parent]:

            if V[child].color != None:
                if V[child].color == V[parent].color:
                    ret = False
            else:
                if V[parent].color == "red":
                    V[child].color = "black"
                else:
                    V[child].color = "red"
                DFS( child )

    for i in range(len(G)):
        if V[i].color == None:
            DFS( i )

    return ret


G = [[1],[0,4],[3],[2,4],[1,3]]
print(bipartite(G))



