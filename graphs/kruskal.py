
class Node:
    def __init__(self , id):
        self.id = id
        self.parent = self
        self.rank = 0

def find_set( x ):
    if x != x.parent:
        x.parent = find_set( x.parent )
    return x.parent

def union( x, y ):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal( G ):
    edges = []
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != None:
                edges.append(( G[i][j] , i , j))

    edges.sort(key=lambda x: x[0])

    Ver = [None] * len(G)
    for i in range(len(G)):
        Ver[i] = Node(i)

    MST = []
    for e in edges:
        if find_set(Ver[e[1]]) != find_set(Ver[e[2]]):
            MST.append(e)
            union(Ver[e[1]] , Ver[e[2]])

    for e in MST:
        print(e[0] , e[1] , e[2])

G = [[None,2,6,None,1,None,None],
     [2,None,None,3,None,None,None],
     [6,None,None,None,None,8,None],
     [None,3,None,None,2,None,1],
     [1,None,None,2,None,5,None],
     [None,None,8,None,5,None,7],
     [None,None,None,1,None,7,None]]

kruskal(G)



