def create():
    return []

def min(Q):
    if len(Q) == 0:
        return None
    return Q[0]

def insert(Q,x):
    """
     Inserisce l'elemento x nella heap Q e ripristina la proprietà di min-heap.

     Q : list
         La heap rappresentata come una lista.
     x : qualsiasi tipo comparabile
         L'elemento da inserire nella heap.
     """
    Q.append(x)  # Aggiunge l'elemento alla fine della lista
    i = len(Q) - 1  # Indice dell'ultimo elemento inserito
    # Ripristina la proprietà di min-heap risalendo l'albero
    while i > 0 and Q[i] < Q[(i - 1) // 2]:
        Q[i], Q[(i - 1) // 2] = Q[(i - 1) // 2], Q[i]  # Scambia con il genitore se necessario
        i = (i - 1) // 2  # Aggiorna l'indice al genitore

def deleteMin(Q):
    """
    Rimuove e restituisce il minimo elemento dalla heap Q e ripristina la proprietà di min-heap.

    Q : list
        La heap rappresentata come una lista.

    Ritorna:
    qualsiasi tipo comparabile
        Il valore minimo nella heap, o None se la heap è vuota.
    """
    if len(Q) == 0:
        return None  # Se la heap è vuota, restituisce None
    min = Q[0]  # Il minimo è la radice della heap
    last = len(Q) - 1  # Indice dell'ultimo elemento
    Q[0] = Q[last]  # Sostituisce la radice con l'ultimo elemento
    Q.pop(last)  # Rimuove l'ultimo elemento dalla lista
    last -= 1  # Aggiorna l'indice dell'ultimo elemento
    i = 0  # Inizia dalla radice
    # Ripristina la proprietà di min-heap scendendo l'albero
    while (2 * i + 1 <= last and Q[i] > Q[2 * i + 1]) or (2 * i + 2 <= last and Q[i] > Q[2 * i + 2]):
        if 2 * i + 2 > last or Q[2 * i + 1] <= Q[2 * i + 2]:
            Q[i], Q[2 * i + 1] = Q[2 * i + 1], Q[i]  # Scambia con il figlio sinistro
            i = 2 * i + 1  # Aggiorna l'indice al figlio sinistro
        else:
            Q[i], Q[2 * i + 2] = Q[2 * i + 2], Q[i]  # Scambia con il figlio destro
            i = 2 * i + 2  # Aggiorna l'indice al figlio destro
    return min  # Restituisce il valore minimo rimosso