def contarNumerosPerfectos():

    # Función para calcular si es un número perfecto
    def calcularNumeroPerfecto(num):
        suma_divisores = 0
        for i in range(1, num):
            if num % i == 0:
                suma_divisores += i
        return suma_divisores == num

    
    # Ingresar n números a la lista
    def ingresarNumeros():
        limite = int(input("Ingrese un límite de números: "))
        for i in range(limite):
            numero = int(input("Ingrese un número: "))
            numeros.append(numero)

    numeros = []
    ingresarNumeros()

    # Contar cuántos números son perfectos
    contador_perfectos = 0
    for num in numeros:
        if calcularNumeroPerfecto(num):
            contador_perfectos += 1

    print(f"La cantidad de números perfectos: {contador_perfectos}")


contarNumerosPerfectos()


# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     elem1 = elem2 = 1
#     sum = 0
#     for i in range(3, n + 1):
#         sum = elem1 + elem2
#         elem1, elem2 = elem2, sum
#     return sum    

# print("Ingrese el límite de la secuencia: ")

# Num = int(input())
# for nx in range(1, Num+1):
#     print("Valor: ", nx, "->", fib(nx))



































