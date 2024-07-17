from abr import abr as t
from graph import graph as g

def simmetria(A,h):
    return simmetriaRicorsiva(A,h,0)

def simmetriaRicorsiva(A,h,l):
    if t.empty(A): # Theta(1)
        return None

    if l % 2 == 0: # Theta(1)
        if not t.empty(t.left(A)) and not t.empty(t.right(A)): #Theta(1)
            if speculari(t.left(A), t.right(A)):
                if profondita(A,0) > h:
                    return A

    sinistra = simmetria(t.left(A),h,l+1)
    if sinistra != None:
        return sinistra

    destra = simmetria(t.right(A),h,l+1)
    if destra != None:
        return destra

    return None


def speculari(A,B):
    if t.empty(A) and not t.empty(B): #Theta(1)
        return False
    if not t.empty(A) and t.empty(B): #Theta(1)
        return False
    if t.empty(A) and t.empty(B): #Theta(1)
        return True
    else:
        return t.value(A) == t.value(B) and speculari(t.left(A), t.left(B)) and speculari(t.right(A), t.right(B))


def profondita(A,i):
    if t.empty(A):
        return 0
    return 1 + max(profondita(t.left(A),i),profondita(t.right(A),i))



def overlap(G,x,y):
    xNeighbors = []
    yNeighbors = []
    for n in g.nodes(G):
        if g.isEdge(G,n,x):
            xNeighbors += n
        if g.isEdge(G,n,y):
            yNeighbors += n
    overlappingNeighbors = []
    for n in xNeighbors:
        if n in yNeighbors:
            overlappingNeighbors += n
    return len(overlappingNeighbors) / min(len(xNeighbors),len(yNeighbors))


