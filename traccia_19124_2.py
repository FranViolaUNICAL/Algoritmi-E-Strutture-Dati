from graph import graphL as g
#A = [5,[],[]]
#A[0] = VALUE(A)
#A[1] = LEFT(A)
#A[2] = RIGHT(A)
#t.insert(A,2) dove A é l'albero e 2 é la chiave del nodo che voglio inserire
#A = [5,[2,[],[]],[]]
#t.insert(A,1) dove A é l'albero e 1 é la chiave del nodo che voglio inserire
#A = [5,[2,[],[]],[]]
#t.insert(left(A),1) viene chiamato ricorsivamente all'interno della chiamata t.insert(A,1)
#A = [2,[1,[],[]],[]]
#           5 ricorsiva([5,[2,[],[]],[]],z1,z2)
#          / \
#         2   - ricorsiva([2,[],[]]) -ricorsiva([])
#        / \
#       1   -
#      / \
def isNull(A):
    return A == []
def inserisci(A,x):
    None
def left(A):
    return A[1]

def right(A):
    return A[2]

def info(A):
    return A[0]

def creaAlbero():
    return []


def findvals(A,z1,z2):
    return findvalsRicorsiva(A,z1,z2,0)

def findvalsRicorsiva(A,z1,z2,i):
    if isNull(A):
        return False # CONDIZIONE DI STOP, CASO BASE, CONDIZIONE DI USCITA

    if i != 0:
        if not isNull(left(A)) or not isNull(right(A)):
            if controllaSottoalberoSinistro(left(A),info(A),z1) or controllaSottoalberoDestro(right(A),info(A),z2):
                return True

    return findvalsRicorsiva(left(A),z1,z2,i+1) or findvalsRicorsiva(right(A),z1,z2,i+1)


def controllaSottoalberoSinistro(A,k,z1):
    if isNull(left(A)) and isNull(right(A)): # SE SIAMO IN UN NODO FOGLIA
        if k * info(A) != z1: # SE NON VIENE RISPETTATO IL CALCOLO CHIESTO SULLA TRACCIA (INFO(P) * INFO(Q) == Z1)
            return False ## RITORNO FALSE ED ESCO DALLA FUNZIONE RICORSIVA
        else: ## SE INVECE SONO IN UN NODO FOGLIA E VIENE RISPETTATO IL CALCOLO
            return True ## RITORNO TRUE ED ESCO DALLA FUNZIONE RICORSIVA
    else: ## SE NON SONO IN UN NODO FOGLIA, CHIAMO LA FUNZIONE RICORSIVA SUL SOTTOALBERO DESTRO E SINISTRO
        return controllaSottoalberoSinistro(left(A),k,z1) and controllaSottoalberoSinistro(right(A),k,z1) ## QUESTE CHIAMATE RITORNERANNO UN VALORE BOOLEANO

def controllaSottoalberoDestro(A,k,z2):
    if isNull(left(A)) and isNull(right(A)) or isNull(A): ## SE SIAMO IN UN NODO FOGLIA
        return False ## SIGNIFICA CHE NON HO TROVATO MAI TRUE, ALLORA RITORNO FALSE (UN ALTRA CHIAMATA POTREBBE TORNARE TRUE, LA FUNZIONE IN QUEL CASO NATURALMENTE RITORNEREBBE TRUE DATO CHE SIAMO IN OR)

    if not isNull(left(A)) or not isNull(right(A)): ## SE NON SIAMO IN UN NODO FOGLIA
        if k + info(A) == z2: ## SE IL CALCOLO DELLA TRACCIA VIENE RISPETTATTO
            return True ## ABBIAMO TROVATO IL NOSTRO NODO

    return controllaSottoalberoDestro(left(A),k,z2) or controllaSottoalberoDestro(right(A),k,z2) ## ALTRIMENTI PROPAGO LA CHIAMATA RICORSIVA FINO A CHE NON OTTENGO UNA RISPOSTA

## SECONDO ESERCIZIO

def raggiungibile(G,x1,x2,x3):
    if depthVisit(G,x2, x3):
        return False

    if depthVisit(G, x1, x3):
        return True

def depthVisit(G,s,d):
    Stack = s
    Visited = []
    while Stack != []:
        next = Stack.pop(len(Stack)-1)
        if next == d:
            return True
        if not next in Visited:
            Visited.append(next)
            Adj = g.neighbors(G,next)
            for [j,w] in Adj:
                if not j in Visited:
                    Stack.append(j)
    return False
