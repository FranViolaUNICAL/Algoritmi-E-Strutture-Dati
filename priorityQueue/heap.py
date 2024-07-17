def createTree():
    return []

def key(T):
    return T[0]

def left(T):
    return T[1]

def right(T):
    return T[2]

def emptyTree(T):
    return T == []

def setKey(T,x):
    T[0] = x

def swapKeys(A1,A2):
    k = key(A1)
    setKey(A1,key(A2))
    setKey(A2,k)

def addLeafNode(T,x):
    T.append(x)
    T.append([])
    T.append([])

def deleteLeafNode(T):
    T.pop()
    T.pop()
    T.pop()

def createHeap():
    return [ createTree(), 0]

def size(H):
    return H[1]

def tree(H):
    return H[0]

def setSize(H,n):
    H[1] = n

def emptyHeap(H):
    return size(H) == 0

def min(H):
    if emptyHeap(H):
        print("Errore: heap vuoto")
        return None
    return key(tree(H))

## int to bitstring

def int2string(i):
    s = []
    while i > 0:
        s.append(i % 2)
        i = int(i / 2)
    s.pop()
    return s

def last(s):
    return s[len(s)-1]

#Inserire una chiave x nell'heap dopo aver calcolato il persorso da seguire
def insertTree(T, s, x):
    if s == []:
        addLeafNode(T,x)
    elif last(s) == 0:
        s.pop()
        insertTree(left(T), s, x)
        if key(T) > key(left(T)):
            swapKeys(T,left(T))
    else:
        s.pop()
        insertTree(right(T), s, x)
        if key(T) > key(right(T)):
            swapKeys(T,right(T))

def insertHeap(H,x):
    setSize(H,size(H) + 1)
    s = int2string(size(H))
    insertTree(tree(H), s, x)

#Estrazione Minimo
def deleteMin(H):
    """
    Funzione deleteMin(H):
        A = radice della heap H
        min = chiave(A)
        n = dimensione(H)

        Se n < 1:
            Ritorna None
        Se n == 1:
            Imposta dimensione(H) a 0
            Elimina il nodo foglia H
            Ritorna min

        s = rappresentazione binaria di n
        p = A
        Per ogni cifra di s (da destra a sinistra):
            Se la cifra è 0, p = figlio sinistro di p
            Altrimenti, p = figlio destro di p

        Elimina il nodo foglia p
        Decrementa la dimensione di H
        Imposta la chiave di A al valore dell'ultimo nodo

        p = A
        Mentre la proprietà di heap è violata:
            Se il figlio sinistro è minore o non esiste il figlio destro:
                Scambia i valori di p e del figlio sinistro
                p = figlio sinistro
            Altrimenti:
                Scambia i valori di p e del figlio destro
                p = figlio destro

        Ritorna min
    """
    A = tree(H)
    min = key(A)
    n = size(H)
    if n < 1:
        return None
    if n == 1:
        setSize(H,0)
        deleteLeafNode(A)
        return min
    s = int2string(n)
    p = tree(H)
    while len(s) > 0:
        if last(s) == 0:
            p = left(p)
        else:
            p = right(p)
        s.pop()
    x = key(p)
    deleteLeafNode(p)
    setSize(H,size(H) - 1)
    setKey(A,x)
    p = A
    while(not emptyTree(left(p)) and key(p) > key(left(p)) or (not emptyTree(right(p))) and key(p) > key(right(p))):
        if(emptyTree(right(p)) or (key(left(p)) <= key(right(p)))):
            swapKeys(p,left(p))
            p = left(p)
        else:
            swapKeys(p,right(p))
            p = right(p)
    return min

# Mapping di un Heap in una Priority Queue
def insertPQ(H,i,Q):
    if H != []:
        Q[i] = H[i]
        insertPQ(H[1],2*i+1,Q)
        insertPQ(H[2],2*i+2,Q)

def tree2list(H):
    Q = []
    for i in range(H[1] + 1):
        Q.append(0)
    insertPQ(H[0],0,Q)
    return Q

## Heap Sort
def heapSort(A):
    H = createHeap()
    for i in range(len(A)):
        insertHeap(H,A[i])
    for i in range(len(A)):
        A[i] = deleteMin(H)

