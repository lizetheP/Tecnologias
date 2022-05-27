def escribe_en_archivo(nombre):
    file = open(nombre, "w")
    for i in range(3):
        frase = str(input("Dame una frase: "))
        file.write(frase)
        file.write('\n')
    file.close()
    
def cuenta_caracteres(nombre):
    file = open(nombre, "r")
    cont = 0
    continua = True
    while continua == True:
        caracter = file.read(1)
        caracter = caracter.lower()
        if not caracter:
            continua = False
        else:
            if caracter != ' ' and caracter != '\n':
                cont = cont + 1
    file.close()
    return cont

def imprime_archivo(nombre):
    file = open(nombre, "r")
    contenido = file.read()
    print(contenido)
    file.close()
    
def menu():
    print()
    print("1. Escribe en archivo")
    print("2. Cuenta caracteres")
    print("3. Imprime archivo")
    print("4. Salir")
        
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            nombre = input("Introduce el nombre del archivo: ")
            escribe_en_archivo(nombre)
        elif opcion == 2:
            nombre = input("Introduce el nombre del archivo de texto: ")
            cont = cuenta_caracteres(nombre)
            print("El archivo tiene %i caracteres" % cont)
        elif opcion == 3:
            nombre = input("Introduce el nombre del archivo: ")
            imprime_archivo(nombre)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("ERROR OPCIÓN INVALIDA")   
    
main()

# Rodrigo
# Rodolfo
# Esmeralda
# Ricardo
# Ricardo
# Isabella