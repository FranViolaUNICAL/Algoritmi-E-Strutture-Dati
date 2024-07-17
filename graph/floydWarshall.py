import graphL as g

def Floyd(G):
    C = g.copyGraph(G)
    for i in g.nodes(G):
        g.insertEdge(C,i,i,0)
    for k in g.nodes(C):
        for i in g.nodes(C):
            for j in g.nodes(C):
                w = g.weight(C,i,k) + g.weight(C,k,j)
                if w < g.weight(C,i,j):
                    g.insertEdge(C,i,j,w)
    return C