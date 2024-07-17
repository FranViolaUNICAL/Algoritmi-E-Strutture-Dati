from graph import graphL as g
from abr import abr as t
def jaccard(G,x,y):
    if g.size(G) == 0:
        return 0
    neighborsForX = set(G[x])
    neighborsForY = set(G[y])
    intersection = neighborsForX.intersection(neighborsForY)
    union = neighborsForX.union(neighborsForY)
    if len(union) == 0:
        return 0
    return len(intersection) / len(union)

def sommaEsatta(A,B,s):
    return sommaEsattaRicorsiva(A,B,s,0,0,t.value(A))

def sommaEsattaRicorsiva(A,B,s,sumT,level,radix):
    if sumT == s:
        if level % 2 == 0:
            return t.value(A) >= numberOfNodes(t.right(B))
        else:
            return t.value(A) <= numberOfNodes(t.left(B))
    if t.empty(t.right(A)) and t.empty(t.left(A)):
        return None

    level += 1
    n = t.value(A) + t.value(t.left(A)) + t.value(t.right(A))
    if (n + sumT) > s:
        sumT = 0
    sommaEsattaRicorsiva(t.right(A),B,s,sumT,level,t.value(t.right(A)))
    sommaEsattaRicorsiva(t.left(A),B,s,sumT,level,t.value(t.left(A)))



def numberOfNodes(A):
    ret = 0
    r = t.right(A)
    l = t.left(A)
    while not t.empty(r) and not t.empty(l):
        r = t.right(r)
        l = t.left(l)
        ret += 1
    while not t.empty(r):
        r = t.right(r)
        ret += 1
    while not t.empty(l):
        l = t.left(l)
        ret += 1
    return ret