def createGraph(n):
    M = [ [0] * n ] * n
    return M

def copyGraph(G):
    n = len(G)
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(G[i][j])
    return C

def printGraph(G):
    for i in range(len(G)):
        print(G[i])

def size(G):
    return len(G)

def nodes(G):
    return list(range(size(G)))

def isEdge(G,i,j):
    return G[i][j] == 1

def insertEdge(G,i,j):
    G[i][j] = 1

def deleteEdge(G,i,j):
    G[i][j] = 0

def outDegree(G,i):
    s = 0;
    for j in range(len(G)):
        s = s + G[i][j]
    return s

def inDegree(G,j):
    s = 0
    for i in range(len(G)):
        s = s + G[i][j]
    return s

def neighbors(G,i):
    L = []
    for j in range(len(G[i])):
        if G[i][j] == 1:
            L.append(i)
    return L