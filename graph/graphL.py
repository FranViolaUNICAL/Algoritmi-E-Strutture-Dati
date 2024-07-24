def createGraph(n):
    G = []
    for i in range(n):
        G.append([])
    return G

def copyGraph(G):
    n = len(G)
    C = []
    for i in range(n):
        C.append([])
        for j in range(n):
            C[i].append(G[i][j])
    return C


def graph2matrix(G):
    n = len(G)
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            M[i].append(0)
    for i in range(n):
        for j in range(G[i]):
            M[i][j] = 1
    return M

def printGraph(G):
    M = graph2matrix(G)
    for i in range(len(M)):
        print(M[i])

def size(G):
    return len(G)

def nodes(G):
    return list(range(size(G)))

def isEdge(G,x,y):
    return(y in G[x])

def insertEdge(G,x,y):
    if not (y in G[x]):
        G[x].append(y)

def deleteEdge(G,x,y):
    G[x].remove(y)

def neighbors(G,x):
    L = []
    for y in G[x]:
        L.append(y)
    return L

def edges(G):
    ret = []
    for n in nodes(G):
        for y in neighbors(G,n):
            if (n,y) not in ret:
                ret.append((n,y))
            if (y,n) not in ret:
                ret.append((y,n))
    return ret
