def llena_datos():
    persona = {}
    continuar = "s"
    while continuar.lower() == 's' or continuar.lower() == 'si':
        clave = str(input("¿Qué dato quieres introducir? "))
        valor = input(clave + ": ")
        persona[clave] = valor
        print(persona)
        continuar = input("¿Quieres agregar más información (S/N)? ")
    return persona

def imprime_y_cuenta(diccionario):
    print("\nLista de datos")
    cont = 0
    for key in diccionario:
        #print(key, " : ", diccionario[key])
        print(str(key) + "\t" + str(diccionario[key]))
        cont = cont + 1
    print("Total datos:", cont)
    
def main():
    diccionario = llena_datos()
    imprime_y_cuenta(diccionario)
main()