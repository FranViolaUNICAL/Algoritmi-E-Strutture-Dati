import math

def createGraph(n):
    L = [ [] for x in range(n)]
    return L

def size(G):
    return len(G)

def nodes(G):
    return [*range(0,len(G),1)]

def isEdge(G,i,j):
    for [x,k] in G[i]:
        if x == j:
            return True
    return False

def weight(G,i,j):
    for [x,w] in G[i]:
        if x == j:
            return w
    else:
        return math.inf

def outDegree(G,i):
    return len(G[i])

def inDegree(G,j):
    k = 0
    for i in range(len(G)):
        for [x,w] in G[i]:
            if x == j:
                k += 1
    return k

def insertEdge(G,i,j,w):
    for [x,k] in G[i]:
        if x == j:
            k = w
            return
    G[i].append((j,w))

def deleteEdge(G,i,j):
    c = 0
    for [x,w] in G[i]:
        if x == j:
            G[i].pop(c)
        c+=1

def neighbors(G,i):
    L = []
    for k in G[i]:
        L.append(k)
    return L

def printGraph(G):
    for i in nodes(G):
        print(i, ">", G[i])

def copyGraph(G):
    M = createGraph(len(G))
    for i in range(len(G)):
        for [j,w] in G[i]:
            M[i].append([j,w])
    return M

def copyAsUndirectedGraph(G):
    M = createGraph(len(G))
    for i in range(len(G)):
        for [j,w] in G[i]:
            M[i].append([j,1])
    return M