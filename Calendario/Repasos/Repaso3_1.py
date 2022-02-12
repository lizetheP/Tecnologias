import random

def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            matriz[i].insert(j, '-')
    return matriz

def imprime_matriz_letras(matriz):
    for i in range(len(matriz)):  # Número de renglones o listas
        for j in range(len(matriz[i])): # Número de columnas o elementos de la lista
            print("%c "% matriz[i][j], end="")
        print()

def llena_matriz_letras(matriz):
    num = 65
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = num
            num = num + 1

def imprime_matriz_numeros(matriz):
    for i in range(len(matriz)):  # Número de renglones o listas
        for j in range(len(matriz[i])): # Número de columnas o elementos de la lista
            print("%i "% matriz[i][j], end="")
        print()

def llena_matriz_numeros(matriz):
    num = 1
    for i in range(len(matriz)-1, -1, -1):
        for j in range(len(matriz[i])-1, -1, -1):
            matriz[i][j] = num
            num = num + 1

def menu():
    print()
    print("1. Llena matriz letras")
    print("2. Llena matriz números")
    print("3. Salir")
    
def main():
    continua = True
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    while continua == True:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            llena_matriz_letras(matriz)
            imprime_matriz_letras(matriz)
        elif opcion == 2:
            llena_matriz_numeros(matriz)
            imprime_matriz_numeros(matriz)
        elif opcion == 3:
            print("Adios")
            continua = False
        else:
            print("Error opción inválida")
        
main()