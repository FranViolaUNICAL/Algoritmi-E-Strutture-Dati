from abr import abr as t
from graph import graphL as g
from itertools import combinations

def subTree(A,B):
    if t.empty(B) and not t.empty(A): # Caso di uscita negativo: B è stato attraversato tutto fino e non è stato trovato un subtree
        return False
    if t.empty(B) and t.empty(A): # Caso di uscita banale: se B è vuoto e A è vuoto allora A è subtree di B
        return True
    if t.value(A) == t.value(B) and t.left(A) == t.left(B) and t.right(A) == t.right(B): # Caso di uscita positivo: I sottoalberi destri e sinistri di A sono uguali a quelli di B, e il valore della radice di A è uguale a quella di B
        return True
    return subTree(A,t.left(B)) or subTree(A,t.right(B))

def main():
    A = t.createTree()
    B = t.createTree()
    t.insert(A,8)
    t.insert(A,6)
    t.insert(A,9)
    t.insert(A,5)
    print(A)
    t.insert(B,6)
    t.insert(B,5)
    print(B)
    print(subTree(B,A))

def vertexCover(G):
    if g.size(G) == 0:
        return []
    possibleCovers = []
    actualCovers = []
    nodes = g.nodes(G)
    while nodes:
        x = nodes.pop(0)
        s = set([x])
        if s not in possibleCovers:
            possibleCovers.append(deepCopy(s))
        for y in nodes:
            s.add(y)
            if s not in possibleCovers:
                possibleCovers.append(deepCopy(s))
    for s in possibleCovers:
        if isVertexCover(G,s):
            actualCovers.append(s)
    return actualCovers

def deepCopy(s):
    ret = set()
    for x in s:
        ret.add(x)
    return ret

def isVertexCover(G,s):
    nodes = g.nodes(G)
    check = []
    for node in s:
        neighbors = g.neighbors(G,node)
        if node not in check:
            check.append(node)
        for x in neighbors:
            if x not in check:
                check.append(x)
    return len(nodes) == len(check)




def main2():
    G = g.createGraph(4)
    g.insertEdge(G,0,1)
    g.insertEdge(G,1,0)
    g.insertEdge(G,2,1)
    g.insertEdge(G,1,2)
    g.insertEdge(G,3,1)
    g.insertEdge(G,1,3)
    print(vertexCover(G))
main2()
