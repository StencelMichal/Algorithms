# graf w postaci macierzowej

def sink ( G ):

    i = 0
    j = 0

    while j < len(G) and i < len(G):
        if G[i][j] == 0:
            j += 1
        else:
            i += 1

    if j < len(G)-1:
        return False

    for j in range(len(G)):
        if G[i][j] == 1:
            return False
        if G[j][i] == 0:
            if i != j:
                return False

    return True



G = [[0,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,1,0]]
print(sink(G))
