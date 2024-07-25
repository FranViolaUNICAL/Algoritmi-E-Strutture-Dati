def knapSack0n(b, Ws, Vs): #b Capacità, Ws Pesi degli oggetti, Vs valori degli oggetti
    # Numero di tipi di oggetti
    n = len(Vs) + 1

    # Inizializzazione della matrice M (n x (b+1)) per memorizzare i valori massimi
    # M[i][j] rappresenta il massimo valore ottenibile con i primi i oggetti e capacità massima j
    M = [[0 for _ in range(b + 1)] for _ in range(n)]

    # Riempimento della matrice M usando programmazione dinamica
    for i in range(1, n):
        for j in range(1, b + 1):
            if Ws[i - 1] <= j:
                # Se possiamo includere l'oggetto i-1 nello zaino (dato il peso Ws[i-1])
                # max tra non prendere l'oggetto e prenderlo almeno una volta
                M[i][j] = max(M[i - 1][j], M[i][j - Ws[i - 1]] + Vs[i - 1])
            else:
                # Non possiamo includere l'oggetto i-1 perché troppo pesante
                M[i][j] = M[i - 1][j]
        # Stampa dello stato della matrice dopo aver considerato l'oggetto i
        print(i, M[i])

    # Chiamata alla funzione Selected per determinare quali oggetti sono stati presi
    # Restituisce il peso totale, il valore massimo e la lista degli oggetti presi
    return [M[-1][-1], M[-1][-1], Selected(b, Ws, Vs, M)]

def Selected(b, Ws, Vs, M):
    # Lista per memorizzare il numero di unità di ciascun oggetto prese
    Sel = [0] * len(Ws)

    # Partiamo dall'ultimo oggetto e dall'ultima capacità
    i, j = len(Ws), b

    # Risalita della matrice per determinare gli oggetti selezionati
    while i > 0:
        if M[i][j] != M[i - 1][j]:
            # L'oggetto i-1 è stato preso
            Sel[i - 1] += 1
            # Aggiornamento della capacità residua
            j -= Ws[i - 1]
        else:
            # L'oggetto i-1 non è stato preso, passa al precedente
            i -= 1

    # Restituisce la lista degli oggetti presi e le rispettive quantità
    print("Peso totale nello zaino:", sum([Sel[i] * Ws[i] for i in range(len(Sel))]))
    print(Sel)
    return Sel

# Esempio di utilizzo
b = 10  # Capacità massima dello zaino
Ws = [2, 3, 4, 5]  # Pesi degli oggetti
Vs = [3, 4, 5, 6]  # Valori degli oggetti

result = knapSack0n(b, Ws, Vs)
print("Valore totale massimo:", result[1])
print("Oggetti selezionati:", result[2])
