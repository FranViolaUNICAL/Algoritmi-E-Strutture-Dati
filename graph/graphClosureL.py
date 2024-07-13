from graph import GraphWL as g

def closure(G):
    C = g.copyAsUndirectedGraph(G)
    for k in g.nodes(G):
        g.insertEdge(C,k,k,1)
    for k in g.nodes(G):
        for i in g.nodes(G):
            for j in g.nodes(G):
                if g.isEdge(C,i,k) and g.isEdge(C,k,j):
                    g.insertEdge(C,i,j,1)
    return C

