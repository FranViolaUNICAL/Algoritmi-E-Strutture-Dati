import itertools

from graph import graphL as g
from itertools import combinations

def cliqueProblem(G):
    nodes = g.nodes(G)
    allAvailableSets = [] #0,1,2,3,01,02,03,
    cliqueSets = []
    ret = []

    for L in range(1,len(nodes)+1):
        for subset in itertools.combinations(nodes,L):
            allAvailableSets.append(subset)

    for set in allAvailableSets:
        if isClique(G,set):
            cliqueSets.append(set)

    moreThanFour = lambda x: len(x) >= 4

    for x in filter(moreThanFour, cliqueSets):
        ret.append(x)

    print(allAvailableSets)
    return ret


def deepCopy(s):
    ret = set({})
    for n in s:
        ret.add(n)
    return ret

def isClique(G,node):
    for n in node:
        check = set({})
        for x in node:
            check.add(x)
        check.remove(n)
        neighbors = g.neighbors(G,n)
        for x in neighbors:
            if x in check:
                check.remove(x)
        if len(check) != 0:
            return False
    return True

def main():
    G = g.createGraph(5)
    g.insertEdge(G,0,1)
    g.insertEdge(G,1,0)
    g.insertEdge(G,0,2)
    g.insertEdge(G,2,0)
    g.insertEdge(G,3,0)
    g.insertEdge(G,0,3)
    g.insertEdge(G,1,2)
    g.insertEdge(G,2,1)
    g.insertEdge(G,1,3)
    g.insertEdge(G,3,1)
    g.insertEdge(G,2,3)
    g.insertEdge(G,3,2)
    g.insertEdge(G,4,0)
    print(cliqueProblem(G))



main()