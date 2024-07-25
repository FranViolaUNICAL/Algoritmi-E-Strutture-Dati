def knapSack01Rec(b,Ws,Vs,n):
    if n < 0 or b == 0:
        return 0
    if (Ws[n] > b):
        return knapSack01Rec(b,Ws,Vs,n-1)
    else:
        return max(Vs[n] + knapSack01Rec(b-Ws[n],Ws,Vs,n-1))
    knapSack01Rec(b,Ws,Vs,n-1)

def Selected(b,Ws,Vs,Value):
    Sel = [0 for j in range(len(Ws))]
    j = b
    i = len(Ws)-1
    while i >= 0:
        while (j-Ws[i] >= 0) and (Value[j] - Value[j-Ws[i]] == Vs[i]):
            Sel[i] += 1
            j = j - Ws[i]
        i -= 1
    return Sel

def knapSack01(b,Ws,Vs):
    n = len(Vs) + 1
    M = [ [0 for j in range(b+1)] for i in range(n+1) ]
    for i in range(1,n):
        for j in range(1,Ws[i-1]):
            M[i][j] = M[i-1][j]
        for j in range(b,Ws[i-1]-1,-1):
            M[i][j] = max(M[i-1][j],M[i-1][j-Ws[i-1]]+Vs[i-1])
        print(i,M[i])
    return [ M[n-1][b], Selected(b,Ws,Vs,M[n-1]) ]