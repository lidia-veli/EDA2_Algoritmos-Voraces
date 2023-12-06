def puede_llegar_final(array):
    n = len(array)
    posicion = 0
    valor = array[posicion]

    while posicion < n and valor != 0:
        posicion += valor

        if posicion == n - 1:
            return True
    
    return False


if __name__ == '__main__':
    entrada = list(map(int, input().split()))
    print(puede_llegar_final(entrada))  
