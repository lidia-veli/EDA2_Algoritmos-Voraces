def min_intercambios(row):
    n = len(row)
    num_interc = 0

    for i in range(0, n, 2):
        if row[i] % 2 == 0:  # si es par
            pareja = row[i] + 1
        
        else:  # si es impar
            pareja = row[i] - 1
        
        if row[i+1] != pareja:  # si no es su pareja
            num_interc += 1
            indice = row.index(pareja)  # buscamos su pareja
            # y la intercambiamos para que esté a su lado
            row[i+1], row[indice] = row[indice], row[i+1]

    return num_interc

if __name__ == '__main__':
    entrada = list(map(int, input().split()))
    print(min_intercambios(entrada))
