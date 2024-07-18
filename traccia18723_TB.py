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

def verificaLiv(A,h):
    return verificaLivRicorsiva(A,h,0,[])

def verificaLivRicorsiva(A,h,i,l):
    if isNull(A):
        return l

    if i > h:
        for i in range(len(l)):
            if l[i][0] == info(A):
                l[i][1] += 1
            if i == len(l) - 1:
                l.append([info(A),1])

    verificaLivRicorsiva(left(A),h,i+1,l)
    verificaLivRicorsiva(right(A),h,i+1,l)

def gradoMinimoOut(G,x): # Complessitá Theta(n^2) poiché giriamo tutti i nodi due volte.
    gradoOut = [0 for _ in range(g.size(G))]
    for k in g.nodes(G):
        for y in g.nodes(G):
            if g.isEdge(G,k,y):
                gradoOut[k] += 1
    return min(gradoOut) == gradoOut[x]
