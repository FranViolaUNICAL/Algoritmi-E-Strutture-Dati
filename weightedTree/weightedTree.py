def tree(x, L ,R ,k):
    return [[x, L, R],k]

def leafNode(x,k):
    return [[x,[],[]],k]

def key(T):
    return [T[0][0]]

def left(T):
    return T[0][1]

def right(T):
    return T[0][2]

def weight(T):
    return T[1]

def empty(T):
    return T == []

def leaf(T):
    return empty(left(T)) and empty(right(T))

