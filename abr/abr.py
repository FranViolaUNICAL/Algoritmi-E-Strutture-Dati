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

#Inserimento di una chiave
def insert(A,x):
    if(empty(A)):
        addNode(A,x)
    else:
        if x <= value(A):
            insert(left(A),x)
        else:
            insert(right(A),x)

#Ricerca di una chiave
def search(A,x):
    if empty(A):
        return False
    elif x == value(A):
        return True
    elif x < value(A):
        return search(left(A),x)
    else:
        return search(right(A),x)

#Cancella una chiave
def delete(A,x):
    if empty(A):
        return
    if value(A) == x:
        if empty(left(A)) and empty(right(A)):
            deleteNode(A)
        elif empty(left(A)) and not empty(right(A)):
            copyNode(A,right(A))
        elif empty(right(A)) and not empty(left(A)):
            copyNode(A,left(A))
        else:
            y = findMax(left(A))
            setValue(A,y)
            delete(left(A),y)
    elif x < value(A):
        delete(left(A),x)
    else:
        delete(right(A),x)

#Visita dell'albero
def infix(A,B):
    if not empty(A):
        infix(left(A),B)
        B.append(value(A))
        infix(right(A),B)

def prefix(A,B):
    if not empty(A):
        B.append(value(A))
        prefix(left(A),B)
        prefix(right(A),B)

def postfix(A,B):
    if not empty(A):
        postfix(left(A),B)
        postfix(right(A),B)
        B.append(value(A))

def breadthfirst(Q,B):
    #Q é una lista di alberi che devono essere visitati
    while Q != []:
        A = Q[0]
        B.append(value(A))
        if not empty(left(A)):
            Q.append(left(A))
        if not empty(right(A)):
            Q.append(right(A))
        Q.pop(0)