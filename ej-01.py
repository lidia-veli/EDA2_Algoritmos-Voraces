def max_area(height):
    n = len(height)
    max_agua = 0
    izda, dcha = 0, n - 1

    while izda < dcha:
        h = min(height[izda], height[dcha])
        anchura = dcha - izda
        max_agua = max(max_agua, h * anchura)

        if height[izda] < height[dcha]:
            izda += 1
        else:
            dcha -= 1

    return max_agua

if __name__ == '__main__':

    entrada = list(map(int, input().split()))
    print(max_area(entrada))

    #print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    #print(max_area([1, 1]))
