from graph import GraphWL as g
from abr import abr as t

def verificaLivelli(A,h,k):
    B = A.copy()
    keys_below_h = []
    find_keys_below_h(B,h,keys_below_h,1)
    print(keys_below_h)
    count_keys_above_k(A,k,keys_below_h,1)
    return keys_below_h


def find_keys_below_h(B,h,l,i):
    if t.empty(B):
        return

    if i < h:
        find_keys_below_h(t.left(B),h,l,i+1)
        find_keys_below_h(t.right(B),h,l,i+1)


    if i >= h:
        n = t.value(B)
        double = [n,0]
        if double not in l:
            l.append([n,0])
        find_keys_below_h(t.right(B),h,l,i+1)
        find_keys_below_h(t.left(B),h,l,i+1)


def count_keys_above_k(A,k,l,i):
    if i >= k:
        return l

    else:
        n = t.value(A)
        print(n)
        for double in l:
            if double[0] == n:
                print(double)
                double[1] += 1
        count_keys_above_k(t.right(A),k,l,i+1)
        count_keys_above_k(t.left(A),k,l,i+1)

T = t.createTree()
t.insert(T,9)
t.insert(T,8)
t.insert(T,10)
t.insert(T,11)
t.insert(T,7)
t.insert(T,8)
t.insert(T,9)
t.insert(T,9)
t.insert(T,3)
print(T)
print(verificaLivelli(T,3,2))


def calculate_in_weights(G, y):
    ret = 0
    for node in g.nodes(G):
        if g.isEdge(G,node,y):
            ret += g.weight(G,node,y)
    return ret

def peso_in(G,x,k):
    in_weights = [0 for i in g.nodes(G)]
    for y in g.nodes(G):
        in_weights[y] = calculate_in_weights(G,y)
        if in_weights[y] == k and y != x:
            return False
    return in_weights[x] == k

G = g.createGraph(5)
g.insertEdge(G,0,1,2)
g.insertEdge(G,0,2,3)
g.insertEdge(G,0,3,4)
g.insertEdge(G,0,4,5)

print(peso_in(G,1,2))

