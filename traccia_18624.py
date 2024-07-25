from graph import graphL as g

def indipendentSetProblem(G):
    nodes = g.nodes(G)
    ret = set()
    while nodes:
        print(nodes)
        x = nodes.pop(0)
        for n in g.neighbors(G,x):
            if n not in ret:
                ret.add(x)
                if n in nodes:
                    nodes.remove(n)
    return ret

def main():
    G = g.createGraph(7)
    g.insertEdge(G,0,1)
    g.insertEdge(G,1,0)
    g.insertEdge(G,1,2)
    g.insertEdge(G,2,1)
    g.insertEdge(G,2,3)
    g.insertEdge(G,3,2)
    g.insertEdge(G,4,3)
    g.insertEdge(G,3,4)
    g.insertEdge(G,4,5)
    g.insertEdge(G,5,4)
    g.insertEdge(G,5,6)
    g.insertEdge(G,6,5)
    print(G)
    print(indipendentSetProblem(G))

def rod_cutting(L, lengths, prices):
    # Creiamo una lista per memorizzare i ricavi massimi
    R = [0] * (L + 1)

    # Per ogni lunghezza del tubo, calcoliamo il massimo ricavo
    for i in range(1, L + 1):
        max_revenue = 0
        for j in range(len(lengths)):
            if lengths[j] <= i:
                max_revenue = max(max_revenue, prices[j] + R[i - lengths[j]])
        R[i] = max_revenue

    return R[L]

# Esempio di utilizzo
L = 8
lengths = [1, 2, 3, 4, 5]  # Lunghezze disponibili
prices = [1, 5, 8, 9, 10]  # Prezzi corrispondenti

max_revenue = rod_cutting(L, lengths, prices)
print("Massimo ricavo:", max_revenue)