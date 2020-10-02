class Node:
    def __init__(self):
        self.next = None
        self.val = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def put(self , x):
        newNode = Node()
        newNode.val = x
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def get(self):
        ret = self.head
        self.head = self.head.next
        return ret.val

class Vertex:
    def __init__(self , id ):
        self.id = id
        self.d = 0
        self.visited = False
        self.parent = None


def BFS( G, s ):
# G to macierz opisująca graf: G[i][j]==1 jeśli jest
# wierzchołek z i do j. W przeciwnym razie G[i][j]=0
# s to numer wierzchołka źródłowego


    # tu proszę umieścić swoją implementację
    Q = Queue()
    listVertex = []

    for i in range(len(G)):
        listVertex.append( Vertex( i ) )

    Q.put(s)
    while not Q.isEmpty():
        vertexP = listVertex[Q.get()]
        for i in range(len(G[vertexP.id])):
            if G[vertexP.id][i] == 1:
                vertex = listVertex[i]
                if not vertex.visited:
                    vertex.visited = True
                    vertex.d = vertexP.d + 1
                    vertex.parent = vertexP.id
                    Q.put(vertex.id)

    ret = []
    for vertex in listVertex:
        ret.append( (vertex.parent , vertex.d) )

    return ret






# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )
