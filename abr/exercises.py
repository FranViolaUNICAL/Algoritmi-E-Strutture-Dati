from abr import abr

#Altezza di un albero
def height(T):
    if abr.empty(T):
        return -1
    return max(height(abr.left(T)), height(abr.right(T))) + 1

#Estrazione delle chiavi a distanza h dal nodo radice, da sinistra verso destra
def infixLevel(A,h,B):
    if not abr.empty(A):
        if h == 0:
            B.append(abr.value(A))
        else:
            infixLevel(abr.left(A),h-1,B)
            infixLevel(abr.right(A),h-1,B)

#Sottoalbero con chiave k nel nodo radice
def findSubtree(k,T):
    if abr.empty(T):
        return False
    if k == abr.value(T):
        return T
    if k < abr.value(T):
        return findSubtree(k,abr.left(T))
    if k > abr.value(T):
        return findSubtree(k,abr.right(T))

#Copia di un albero
def copyTree(A):
    A1 = abr.createTree()
    copyTree2(A,A1)
    return A1

def copyTree2(A,A1):
    if not abr.empty(A):
        abr.addNode(A1,abr.value(A))
        copyTree2(abr.left(A),abr.left(A1))
        copyTree2(abr.right(A),abr.right(A1))

#Uguaglianza fra due alberi:
def equal(T1,T2):
    if abr.empty(T1) and abr.empty(T2):
        return True
    if not abr.empty(T1) and not abr.empty(T2) and abr.value(T1) == abr.value(T2):
        return equal(abr.left(T1),abr.left(T2)) and equal(abr.right(T1),abr.right(T2))
    return False

#Verifica se un sotto-albero T1 é contenuto in T2
def subtree(T1,T2):
    return equal(T1, abr.find(abr.value(T1),T2))

#Chiavi piú vicine ad una chiave k
def nearestDown(k,T,v):
    if abr.empty(T):
        return v
    if k == abr.value(T):
        return abr.value(T)
    if k > abr.value(T):
        if abr.value(T) > v:
            v = abr.value(T)
        return nearestDown(k,abr.right(T),v)
    else:
        return nearestDown(k,abr.left(T),v)

def nearestUp(k,T,v):
    if abr.empty(T):
        return v
    if k == abr.value(T):
        return abr.value(T)
    if k < abr.value(T):
        if abr.value(T) < v:
            v = abr.value(T)
        return nearestUp(k,abr.left(T),v)
    else:
        return nearestUp(k,abr.right(T),v)

#Da vettore ordinato ad albero binario

def V2T(V,first,last,T):
    if first <= last:
        middle = (first + last)//2
        abr.addNode(T,V[middle])
        V2T(V,first,middle-1,abr.left(T))
        V2T(V,middle+1,last,abr.right(T))