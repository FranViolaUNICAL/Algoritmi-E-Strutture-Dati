from graph import graphL as g
import weightedTree as t
from priorityQueue import heap as h

# Funzione per copiare una lista C in una nuova lista D
def copyList(C):
    D = []
    for i in range(len(C)):
        D.append(C[i])
    return D

# Funzione ricorsiva per generare i codici di Huffman
def codeGeneration(T, S, C):
    if t.leaf(T):  # Se il nodo è una foglia
        D = copyList(C)  # Crea una copia di C
        S.append([t.key(T), D])  # Aggiunge la coppia [simbolo, codice] a S
    else:  # Se il nodo non è una foglia
        C.append(0)  # Aggiunge 0 alla lista dei codici
        codeGeneration(t.left(T), S, C)  # Ricorre sul sottoalbero sinistro
        C.pop()  # Rimuove l'ultimo elemento (0)
        C.append(1)  # Aggiunge 1 alla lista dei codici
        codeGeneration(t.right(T), S, C)  # Ricorre sul sottoalbero destro
        C.pop()  # Rimuove l'ultimo elemento (1)

# Funzione principale per costruire l'albero di Huffman e generare i codici
def Huffman(L):
    Q = h.createHeap()  # Crea un heap vuoto
    n = len(L)  # Numero di simboli
    for [x, k] in L:  # Per ogni simbolo e la sua frequenza
        T = t.leafNode(x, k)  # Crea un nodo foglia
        h.insertHeap(Q, T)  # Inserisce il nodo foglia nell'heap
    for i in range(n-1):  # Ripete n-1 volte
        A = h.deleteMin(Q)  # Estrae il nodo con la minima frequenza
        B = h.deleteMin(Q)  # Estrae il secondo nodo con la minima frequenza
        C = t.tree('+', A, B, t.weight(A) + t.weight(B))  # Crea un nuovo nodo combinando A e B
        h.insertHeap(Q, C)  # Inserisce il nuovo nodo nell'heap
    T = h.deleteMin(Q)  # L'ultimo nodo rimanente è la radice dell'albero di Huffman
    S = []  # Lista per memorizzare i codici di Huffman
    print("---", T)  # Stampa l'albero di Huffman per debug
    codeGeneration(T, S, [])  # Genera i codici di Huffman
    return S  # Restituisce la lista dei codici di Huffman

def main():
    L = [ ['a',45], ['b',13],['c',12],['d',16],['e',9],['f',5] ]
    T = Huffman(L)
    print()
    print("---HUFFMAN---")
    print(T)


main()