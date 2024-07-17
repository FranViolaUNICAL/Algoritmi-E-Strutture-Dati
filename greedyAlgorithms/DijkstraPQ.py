import math
import GraphA as g
import Heap as h

def Dijkstra(G, s):
    n = g.size(G)
    dist = [ math.inf for i in range(n) ]
    pred = [ -1 for i in range(n) ]
    visited = [ False for i in range(n) ]
    Edges = []
    dist[s] = 0
    Q = h.createHeap()
    h.insertHeap(Q,[s,0])
    while not h.empty(Q):
        [next, weight] = h.deleteMin(Q)
        if not visited[next]:
            visited[next] = True
            Edges.append(pred[next],next,dist[next])
            Adj = g.neighbors(next)
            for [z,w] in Adj:
                d = dist[next] + w
                if (dist[z] > d):
                    dist[z] = d
                    pred[z] = next
                    h.insertHeap(Q,[z,d])
    Edges.pop(0)
    return Edges