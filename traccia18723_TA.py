from graph import graphL as g
def isNull(A):
    return A == []
def inserisci(A,x):
    None
def left(A):
    return A[1]

def right(A):
    return A[2]

def info(A):
    return A[0]

def creaAlbero():
    return []

def verificaIntervallo(A,B,v1,v2,k):
    if isNull(A):
        return True
    if v1 <= info(A) <= v2:
        if not numeroNodi(left(B),info(A),0) + numeroNodi(right(B),info(A),0) == k:
            return False

    return verificaIntervallo(left(A),B,v1,v2,k) and verificaIntervallo(right(A),B,v1,v2,k)

def numeroNodi(B,x):
    if isNull(B):
        return 0
    if info(B) == x:
        return 1 + numeroNodi(left(B),x) + numeroNodi(right(B),x)
    else:
        return 0 + numeroNodi(left(B),x) + numeroNodi(right(B),x)


def coppiaMax(G):
    neighbors = [[] for i in range(len(G))]
    for x in g.nodes(G):
        for y in g.nodes(G):
            if g.isEdge(G,y,x):
                neighbors[x].append(y)
    ret = []
    for i in range(len(G)):
        n = neighbors[i]
        counter = [[i,0] for i in range(0,len(G))]
        for x in n:
            for j in range(i,len(G)):
                k = neighbors[j]
                if x in k:
                    counter[j][1] += 1
        ret.append(counter)

    trueRet = [0,0]
    for x in ret:
        for y in x:
            if trueRet[1] <= y[1]:
                trueRet = y
    return trueRet


