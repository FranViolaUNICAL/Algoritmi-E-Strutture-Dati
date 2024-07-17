from graph import GraphWL as g
from priorityQueue import heap as h


def Kruskal(G):
    V = []  # Lista per memorizzare tutti gli archi del grafo G

    # Step 1: Raccogli tutti gli archi del grafo con i rispettivi pesi
    for i in g.nodes(G):
        for [j, w] in g.neighbors(i):
            if i < j:  # Evita di aggiungere lo stesso arco due volte
                V.append([[i, j], w])

    # Step 2: Ordina gli archi per peso utilizzando heapSort
    h.heapSort(V)

    # Step 3: Crea una foresta con un insieme separato per ogni nodo
    C = []
    for i in range(len(G)):
        C.append([i])

    T = []  # Lista per memorizzare gli archi dell'MST

    # Step 4: Scorri gli archi ordinati
    for [[i, j], w] in V:
        # Se i nodi i e j non sono nello stesso insieme, aggiungi l'arco all'MST
        if C[i] != C[j]:
            T.append([i, j, w])

            # Unisci gli insiemi contenenti i nodi i e j
            if len(C[i]) >= len(C[j]):
                for k in C[j]:
                    C[i].append(k)
                    C[k] = C[i]  # Aggiorna il riferimento dell'insieme per ogni nodo in C[j]
            else:
                for k in C[i]:
                    C[j].append(k)
                    C[k] = C[j]  # Aggiorna il riferimento dell'insieme per ogni nodo in C[i]

    return T  # Restituisce l'MST come lista di archi