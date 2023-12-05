def min_caramelos(valor_hambre):
    n = len(valor_hambre)
    caramelos = [1]*n  # en un principio, cada niño tiene un caramelo

    # Asignamos caramelos de izquierda a derecha
    for i in range(1, n):
        if valor_hambre[i] > valor_hambre[i - 1]:
            caramelos[i] = caramelos[i - 1] + 1

    # Asignamos caramelos de derecha a izquierda
    for i in range(n - 2, -1, -1):
        if valor_hambre[i] > valor_hambre[i + 1] and caramelos[i] <= caramelos[i + 1]:
            caramelos[i] = caramelos[i + 1] + 1

    return sum(caramelos)


if __name__ == '__main__':
    entrada = list(map(int, input().split()))
    print(min_caramelos(entrada))

