from graph import graph as g

def closure(G):
    """
    Calcola la chiusura transitiva del grafo diretto G e ritorna il grafo chiuso C.

    La chiusura transitiva di un grafo G è un grafo in cui esiste un arco diretto da un nodo i a un nodo j
    se e solo se esiste un cammino (possibilmente vuoto) da i a j in G.

    Parametri:
    - G: grafo diretto (rappresentato in una struttura supportata dalla libreria 'g')

    Ritorna:
    - C: grafo diretto che rappresenta la chiusura transitiva di G

    Passi:
    1. Copia il grafo G nel grafo C.
    2. Aggiungi un arco diretto (i, i) per ogni nodo i in C per includere i cammini di lunghezza zero.
    3. Per ogni tripla di nodi (i, j, k), se esiste un arco da i a k e un arco da k a j, aggiungi un arco da i a j.
    """
    C = g.copyGraph(G)
    for i in g.nodes(C):
        g.insertEdge(C,i,i)
    for k in g.nodes(C):
        for i in g.nodes(C):
            for j in g.nodes(C):
                if g.isEdge(C,i,k) and g.isEdge(C,k,j):
                    g.insertEdge(C,i,j)
    return C