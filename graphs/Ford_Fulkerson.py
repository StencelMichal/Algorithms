from queue import Queue

def pArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="  ")
        print()

class Vertex:
    def __init__(self):
        self.parent = None
        self.cost = float("inf")
        self.visited = False

def BFS( G , V , source , target):
    Q = Queue()
    Q.put(source)

    while not Q.empty():
        parent = Q.get()
        for child in range(len(G)):
            if G[parent][child] > 0 and not V[child].visited:
                V[child].parent = parent
                V[child].visited = True
                Q.put(child)

    return V[target].visited

def FordFulkerson( G , source , target):

    # licznik maksymalnego przepływu
    maxFlow = 0

    # tworzymy tablice wierzchołków
    V = [ Vertex() for i in range(len(G)) ]

    # tworzymy kopie grafu w ktora jest potrzebna jeśli chcemy
    # wiedzieć jak konkretnie popłynie przepływ
    copy = [G[i].copy() for i in range(len(G))]

    # powiększamy przepływ dopóki da się uzyskać lepszy wynik
    # możemy do zrobić jeśli po przeszukaniu grafu nadal udało nam się dotrzeć
    # do naszego celu
    while BFS(G,V,source , target):
        flow = float("inf")
        t = target
        # sprawdzamy minimium o jakie udało nam się powiększyć przepływ
        while( t != source):
            parent = V[t].parent
            if G[parent][t] < flow:
                flow = G[parent][t]
            t = parent

        maxFlow += flow

        t = target
        # modyfikujemy sieć residulną
        while (t != source):
            parent = V[t].parent
            G[parent][t] -= flow
            G[t][parent] += flow
            t = parent

        # ustawiamy wartości na początkowe przed kolejnym przeszukaniem grafu
        for vertex in V:
                vertex.visited = False
                vertex.parent = None
                vertex.cost = float("inf")


    # # # #
    # dalsza cześć to tworzenie grafu przepływu
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != copy[i][j] and copy[i][j] == 0:
                copy[i][j] = G[i][j]
            else:
                copy[i][j] = 0

    for i in range(len(G)):
        for j in range( i+1, len(G) ):
            copy[i][j] , copy[j][i] = copy[j][i] , copy[i][j]



    return maxFlow , copy

G = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

A = [[0,4,3,0,0,0],
     [0,0,2,2,0,0],
     [0,0,0,2,2,0],
     [0,0,0,0,0,4],
     [0,0,0,0,0,5],
     [0,0,0,0,0,0]]


c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
maxflow , dupa = FordFulkerson(c , 0 , 3) # wypisze 3
print(maxflow)

maxflowG , flowG = FordFulkerson(G , 0 , 5)
maxflowA , flowA = FordFulkerson(A , 0 , 5)

print(maxflowA)
pArr(flowA)
print()
print()
print(FordFulkerson(G , 0 , 3))