def KnapsackF(Wmax, Ws, Vs, Cs):
    n = len(Ws)
    D = []
    for i in range(n):
        D.append([Vs[i]/Ws[i], i])
    D.sort()
    D.reverse()
    print(">",D)
    weight = 0
    value = 0
    i = 0
    sack = []
    while weight < Wmax and i < n:
        j = D[i][1]
        k = min((Wmax-weight)/Ws[j], Cs[j])
        weight += k * Ws[j]
        value += k * Vs[j]
        sack.append([j,k])
        i += 1
    return [weight, value, sack]