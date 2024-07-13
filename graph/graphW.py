import math

def createGraph(n):
    M = [ [ math.inf for x in range(n) ] for x in range(n)]
    return M

def size(G):
    return (len(G))

def nodes(G):
    return [*range(0,len(G),1)]

def isEdge(G,i,j):
    return G[i][j] != math.inf

def weight(G,x,y):
    return G[x][y]

def outDegree(G,i):
    k = 0
    for i in range(len(G)):
        if G[i][i] != math.inf:
            k += 1
    return k

def insertEdge(G,i,j,w):
    G[i][j] = w

def deleteEdge(G,i,j):
    G[i][j] = math.inf

def neighbors(G,i):
    N = []
    for j in range(len(G[i])):
        if G[i][j] != math.inf:
            N.append([j,G[i][j]])
    return N

def printGraph(G):
    for i in range(len(G)):
        print(G[i])

def copyGraph(G):
    M = createGraph(len(G))
    for i in range(len(G)):
        for j in range(len(G[i])):
            M[i][j] = G[i][j]
    return M

def copyAsUndirectedGraph(G):
    M = createGraph(len(G))
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] != math.inf:
                M[i][j] = 1
    return M