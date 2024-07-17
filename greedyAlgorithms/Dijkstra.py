from graph import GraphWL as g
import math


def minVertex(D, V):
    """
    Trova il vertice con la minima distanza che non è stato ancora visitato.

    Parametri:
    - D: lista delle distanze dai nodi di partenza
    - V: lista dei nodi visitati (True se il nodo è stato visitato, False altrimenti)

    Ritorna:
    - y: indice del nodo con la minima distanza non ancora visitato
    """
    x = math.inf  # Inizializza x all'infinito
    y = -1  # Inizializza y a -1 per indicare che nessun nodo è stato trovato

    for i in range(len(D)):  # Scorri tutti i nodi
        if (not V[i]) and (D[i] < x):  # Se il nodo non è stato visitato e la sua distanza è minore di x
            y = i  # Aggiorna y con l'indice del nodo
            x = D[i]  # Aggiorna x con la distanza del nodo

    return y  # Ritorna l'indice del nodo con la minima distanza


def Dijkstra(G, s):
    """
    Esegue l'algoritmo di Dijkstra per trovare il percorso più breve da un nodo sorgente s a tutti gli altri nodi.

    Parametri:
    - G: grafo diretto rappresentato in una struttura supportata dalla libreria 'g'
    - s: nodo sorgente

    Ritorna:
    - Edges: lista dei percorsi minimi con [nodo predecessore, nodo attuale, distanza]
    """
    n = g.size(G)  # Numero di nodi nel grafo
    dist = [math.inf for i in range(n)]  # Inizializza tutte le distanze a infinito
    pred = [-1 for i in range(n)]  # Inizializza tutti i predecessori a -1
    visited = [False for i in range(n)]  # Inizializza tutti i nodi come non visitati
    Edges = []  # Lista per memorizzare i percorsi minimi
    dist[s] = 0  # La distanza dal nodo sorgente a se stesso è 0

    for i in range(n):  # Itera su tutti i nodi
        next = minVertex(dist, visited)  # Trova il nodo non visitato con la distanza minima
        if next == -1:  # Se non ci sono più nodi da visitare, ritorna i percorsi trovati
            return Edges

        visited[next] = True  # Segna il nodo come visitato
        Edges.append([pred[next], next, dist[next]])  # Aggiungi il nodo corrente ai percorsi minimi

        Adj = g.neighbors(G, next)  # Ottieni i vicini del nodo corrente
        for [z, w] in Adj:  # Scorri tutti i vicini
            if not visited[z]:  # Se il vicino non è stato visitato
                d = dist[next] + w  # Calcola la distanza dal nodo corrente al vicino
                if d < dist[z]:  # Se la distanza calcolata è minore della distanza attuale
                    dist[z] = d  # Aggiorna la distanza del vicino
                    pred[z] = next  # Aggiorna il predecessore del vicino

    return Edges  # Ritorna la lista dei percorsi minimi


def Prim(G, s):
    """
    Esegue l'algoritmo di Prim per trovare l'albero di copertura minimo (MST) di un grafo non orientato connesso.

    Parametri:
    - G: grafo non orientato rappresentato in una struttura supportata dalla libreria 'g'
    - s: nodo sorgente da cui iniziare la costruzione dell'MST

    Ritorna:
    - MST: lista di archi che costituiscono l'albero di copertura minimo
    """
    n = g.size(G)  # Numero di nodi nel grafo
    dist = [math.inf for i in range(n)]  # Inizializza tutte le distanze a infinito
    pred = [-1 for i in range(n)]  # Inizializza tutti i predecessori a -1
    visited = [False for i in range(n)]  # Inizializza tutti i nodi come non visitati
    MST = []  # Lista per memorizzare gli archi dell'albero di copertura minimo
    dist[s] = 0  # La distanza dal nodo sorgente a se stesso è 0

    for i in range(n):  # Itera su tutti i nodi
        next = minVertex(dist, visited)  # Trova il nodo non visitato con la distanza minima
        if next == -1:  # Se non ci sono più nodi da visitare, ritorna l'MST trovato
            return MST

        visited[next] = True  # Segna il nodo come visitato
        if pred[next] != -1:
            MST.append([pred[next], next, dist[next]])  # Aggiungi l'arco corrente all'MST

        Adj = g.neighbors(G, next)  # Ottieni i vicini del nodo corrente
        for [z, w] in Adj:  # Scorri tutti i vicini
            if not visited[z] and w < dist[z]:  # Se il vicino non è stato visitato e il peso dell'arco è minore della distanza attuale
                dist[z] = w  # Aggiorna la distanza del vicino
                pred[z] = next  # Aggiorna il predecessore del vicino

    return MST  # Ritorna la lista degli archi dell'albero di copertura minimo


