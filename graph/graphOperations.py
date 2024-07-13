from graph import graph as g

def edges(pred):
    E = []
    for i in range(len(pred)):
        if pred[i] != -1:
            E.append([pred[i],i])
    return E

def breadthVisit(G,s):
    Queue = [s]
    Visited = []
    while Queue != []
        next = Queue.pop(0)
        if not next in Visited:
            Visited.append(next)
            Adj = g.neighbors(G,next)
            for [j,w] in Adj:
                if not j in Visited:
                    Queue.append(j)
    return Visited

def depthVisit(G,s):
    Stack = s
    Visited = []
    while Stack != []:
        next = Stack.pop(len(Stack)-1)
        if not next in Visited:
            Visited.append(next)
            Adj = g.neighbors(G,next)
            for [j,w] in Adj:
                if not j in Visited:
                    Stack.append(j)
    return Visited

def depthVisitRec(G,s):
    Visited = [s]
    depthVisitRec2(G,s,Visited)
    return Visited

def depthVisitRec2(G,x,Visited):
    Adj = g.neighbors(G,x)
    for [j,w] in Adj:
        if not j in Visited:
            Visited.append(j)
            depthVisitRec2(G,j,Visited)

def cyclicGraph(G):
    Visited = []
    CPath = []
    for x in g.nodes(G):
        if not x in Visited and cyclicPath(G,x,Visited,CPath):
            return True
    return False

def cyclicPath(G,x,Visited,CPath):
    Visited.append(x)
    CPath.append(x)
    Adj = g.neighbors(G,x)
    for [j,w] in Adj:
        if j in CPath:
            return True
        elif cyclicPath(G,j,Visited,CPath):
            return True
    CPath.pop(len(CPath)-1)
    return False

