def createTree():
    return []

def empty(A):
    return A == []

def value(A):
    return A[0]

def left(A):
    return A[1]

def right(A):
    return A[2]

def setValue(A,x):
    A[0] = x

def setLeft(A,x):
    A[1] = x

def setRight(A,x):
    A[2] = x

def findMax(A):
    if empty(right(A)):
        return value(A)
    return findMax(right(A))

def addNode(A,x):
    A.append(x)
    A.append([])
    A.append([])

def deleteNode(A):
    A.pop()
    A.pop()
    A.pop()

def copyNode(A,B):
    A[0] = B[0]
    A[1] = B[1]
    A[2] = B[2]

def depth(A):
    if empty(A):
        return 0
    return max(depth(left(A)),depth(right(A))) + 1

def bal(A):
    """
    Calcola il fattore di bilanciamento dell'albero A.

    A : nodo
        Il nodo dell'albero binario.

    Ritorna:
    int
        La differenza tra le profondità del sottoalbero sinistro e destro.
    """
    if empty(A):
        return 0
    return depth(left(A)) - depth(right(A))

def rightRotate(A):
    """
    Effettua una rotazione a destra sul nodo A.

    A : nodo
        Il nodo dell'albero binario.

    Ritorna:
    nodo
        La nuova radice del sottoalbero dopo la rotazione.
    """
    T = A
    A = left(A)
    setLeft(T,right(A))
    setRight(A,T)
    return A

def leftRotate(A):
    """
    Effettua una rotazione a sinistra sul nodo A.

    A : nodo
        Il nodo dell'albero binario.

    Ritorna:
    nodo
        La nuova radice del sottoalbero dopo la rotazione.
    """
    T = A
    A = right(A)
    setRight(T,left(A))
    setLeft(A,T)
    return A

def rotate(A):
    """
    Applica le rotazioni necessarie per bilanciare l'albero A.

    A : nodo
        Il nodo dell'albero binario.

    Ritorna:
    nodo
        La nuova radice del sottoalbero bilanciato.
    """
    if bal(A) == 2 and not empty(left(A)) and bal(left(A)) >= 0:
        A = rightRotate(A)
    if bal(A) == -2 and not empty(right(A)) and bal(right(A)) <= 0:
        A = leftRotate(A)
    if bal(A) == 2 and not empty(left(A)) and bal(left(A)) < 0:
        setLeft(A,leftRotate(left(A)))
        A = rightRotate(A)
    if bal(A) == -2 and not empty(right(A)) and bal(right(A)) > 0:
        setRight(A,rightRotate(right(A)))
        A = leftRotate(A)
    return A

def search(A,x):
    """
    Cerca il valore x nell'albero A.

    A : nodo
        Il nodo dell'albero binario.
    x : qualsiasi tipo comparabile
        Il valore da cercare.

    Ritorna:
    bool
        True se il valore è trovato, False altrimenti.
    """
    if empty(A):
        return False
    if x == value(A):
        return True
    if x < value(A):
        return search(left(A),x)
    else:
        return search(right(A),x)


def insert(A,x):
    if empty(A):
        addNode(A,x)
    elif x <= value(A):
        setLeft(A,insert(left(A),x))
    else:
        setRight(A,insert(right(A),x))
    return rotate(A)

def delete(A,x):
    """
    Elimina il nodo con valore x dall'albero A (AVL) e ritorna l'albero aggiornato.

    Parametri:
    - A: nodo radice dell'albero (BST)
    - x: valore da eliminare

    Ritorna:
    - L'albero A aggiornato dopo l'eliminazione del nodo con valore x

    Operazioni:
    - Se l'albero è vuoto (A == None), ritorna l'albero stesso.
    - Se x è uguale a value(A):
        - Se entrambi i sottoalberi sono vuoti, elimina il nodo corrente.
        - Se uno dei sottoalberi è vuoto, copia l'altro sottoalbero.
        - Se entrambi i sottoalberi sono presenti, trova il massimo nel sottoalbero sinistro,
          lo sostituisce con il nodo corrente e elimina il nodo con valore massimo.
    - Se x è minore di value(A), continua la ricerca nel sottoalbero sinistro.
    - Se x è maggiore di value(A), continua la ricerca nel sottoalbero destro.
    - Alla fine dell'eliminazione, esegue una rotazione per bilanciare l'albero (se necessario).
    """
    if empty(A):
        return A
    if x == value(A):
        if empty(left(A)) and empty(right(A)):
            deleteNode(A)
        elif empty(left(A)) and not empty(right(A)):
            copyNode(A,right(A))
        elif not empty(left(A)) and empty(right(A)):
            copyNode(A,left(A))
        else:
            y = findMax(left(A))
            setValue(A,y)
            setLeft(A,delete(left(A),y))
    elif x < value(A):
        setLeft(A,delete(left(A),x))
    else:
        setRight(A,delete(right(A),x))
    return rotate(A)