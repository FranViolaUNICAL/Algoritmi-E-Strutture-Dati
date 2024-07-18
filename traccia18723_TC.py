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


def verificaInfo(A,B,r1,r2,k):
    if isNull(A):
        return True

    if info(A) <= r1 or info(A) >= r2:
        if not contaNodiFoglia(B, info(A) + abs(r1+r2)) <= k:
            return False

    return verificaInfo(left(A),B,r1,r2,k) and verificaInfo(right(A),B,r1,r2,k)


def contaNodiFoglia(B,n):
    if isNull(B):
        return 0
    count = 0
    if isNull(left(B)) and isNull(right(B)) and info(B) < n:
        count = 1
    return count + contaNodiFoglia(left(B),n) + contaNodiFoglia(right(B),n)

def coppia(G,k):
    neighbors = [[] for _ in range(g.size(G))]
    for n in g.nodes(G):
        for x in g.nodes(G):
            if g.isEdge(G,n,x) or g.isEdge(G,x,n):
                if x not in neighbors[n]:
                    neighbors[n].append(x)
                if n not in neighbors[x]:
                    neighbors[x].append(n)

    overlap = []
    for i in range(len(neighbors)):
        for j in range(i+1,len(neighbors)):
            overlap.append([i,j,0])
            for x in neighbors[i]:
                if x in neighbors[j]:
                    overlap[i][2] += 1

    for overlappingNeighbors in overlap:
        if overlappingNeighbors[2] == k:
            return overlappingNeighbors
    return None


