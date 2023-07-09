def calcularTrianguloPascal(filas):
    tri_pascal = []

    #completar filas estructura
    for fila in range(filas):
        fila_actual = [1] * (fila + 1)

        #Calcular los valores de la fila
        if fila > 1:
            for i in range(1, fila):
                fila_actual[i] = tri_pascal[fila - 1][i - 1] + tri_pascal[fila - 1][i]

        tri_pascal.append(fila_actual)

    #Separador
    for fila in tri_pascal:
        for valor in fila:
            print(valor, end=" ")
        print()


n = int(input("Ingrese el número de filas: "))
print("*********************Triangulo de Pascal***********************************")
calcularTrianguloPascal(n)












