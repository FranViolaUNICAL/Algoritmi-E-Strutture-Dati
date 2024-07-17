from graph import graphL as g
from abr import abr as a

def vertexCover3(G,numberOfVertices):
    if(len(G)==0):
        return 0
    if(len(G)==1 or len(G)==2):
        return 1
    check = allEdges(G)
    ret = []
    for i in range(len(G)):
        edgesReached1 = edgesReached(G,i)
        visited = [i]
        for j in range(len(G)):
            if i != j and j not in visited:
                edgesReached2 = edgesReached(G,j)
                for edge in edgesReached2:
                    if edge not in edgesReached1:
                        edgesReached1.append(edge)
                        if j not in visited:
                            visited.append(j)
        if len(edgesReached1) == len(check):
            ret.append(visited)
    for l in ret:
        if len(l) == numberOfVertices:
            return True
    return False

def vertexCover4(G):
    if(len(G)==0):
        return 0
    if(len(G)==1 or len(G)==2):
        return 1
    check = allEdges(G)
    ret = []
    for i in range(len(G)):
        edgesReached1 = edgesReached(G,i)
        visited = [i]
        for j in range(len(G)):
            if i != j and j not in visited:
                edgesReached2 = edgesReached(G,j)
                for edge in edgesReached2:
                    if edge not in edgesReached1:
                        edgesReached1.append(edge)
                        if j not in visited:
                            visited.append(j)
        if len(edgesReached1) == len(check):
            ret.append(visited)
    min = len(G)
    for l in ret:
        if len(l) < min:
            min = len(l)
    return min


def edgesReached(G,i):
    ret = []
    for j in range(len(G)):
        if(g.isEdge(G,i,j)):
            ret.append([i,j])
        elif(g.isEdge(G,j,i)):
            ret.append([j,i])
    return ret



def allEdges(G):
    ret = []
    for i in range(len(G)):
        for j in range(len(G)):
            if g.isEdge(G,i,j):
                ret.append([i,j])
    return ret



def main1():
    G = g.createGraph(4)
    g.insertEdge(G,0,1)
    g.insertEdge(G,0,2)
    g.insertEdge(G,2,1)
    g.insertEdge(G,2,3)
    g.insertEdge(G,3,0)
    print(vertexCover3(G,2))
    print(vertexCover4(G))

def subTree(A,B):
    if equal(A,B):
        return True
    print(a.left(B))
    print(a.right(B))
    return subTree(A,a.left(B)) or subTree(A,a.right(B))

def equal(A,B):
    if a.empty(A) and a.empty(B):
        return True
    if a.empty(B) or a.empty(A):
        return False
    return a.value(A) == a.value(B) and a.left(A) == a.left(B) and a.right(A) == a.right(B)

def main2():
    A = a.createTree()
    B = a.createTree()
    a.insert(A,5)
    a.insert(A,3)
    a.insert(A,6)
    a.insert(A,4)
    a.insert(A,7)
    a.insert(B,6)
    print(subTree(B,A))

main2()