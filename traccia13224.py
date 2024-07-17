from graph import GraphWL as g
def verifica(A,B,s):
    return verificaRicorsiva(A,B,s,True)

def verificaRicorsiva(A,B,s):
    if isNull(A):
        return None
    else:
        if isNull(left(A)) and isNull(right(A)):
            if not esisteSottoAlberoIdoneo(B,0,info(A),s):
                return False
        else:
            verificaRicorsiva(left(A),B,s)
            verificaRicorsiva(right(A),B,s)
    return True


def esisteSottoAlberoIdoneo(B,i,value,s):
    if isNull(B):
        return False

    if i % 2 == 0:
        if not isNull(left(B)) and not isNull(right(B)):
            if sommaSottoAlbero(B,0) > s:
                return True

    return esisteSottoAlberoIdoneo(left(B),i+1,value,s) or esisteSottoAlberoIdoneo(right(B),i+1,value,s)

def sommaSottoAlbero(B,s):
    if isNull(B):
        return s
    return info(B) + sommaSottoAlbero(left(B),s) + sommaSottoAlbero(right(B),s)


def isNull(A):
    return A == []

def inserisci(A,x):
    None

def addNode(A,x):
    A.append(x)
    A.append([])
    A.append([])

def size(A):
    if isNull(A):
        return 0
    return 1 + size(left(A)) + size(right(A))

def left(A):
    return A[1]

def right(A):
    return A[2]

def info(A):
    return A[0]

def creaAlbero():
    return []


def almenoK(G,x,k,d):
    i = 0
    for n in g.nodes(G):
        if g.isEdge(n,x) and g.weight(G,n,x) < d:
            n += 1
            if i == k:
                return True
    return False