def lista_compras():
    lista = {}
    continuar = True
    while continuar == True:
        clave = str(input("Introduce el nombre del artículo: "))
        valor = float(input("Introduce su precio: "))
        lista[clave] = valor
        print(lista)
        continuar = str(input("¿Quieres agregar otro artículo (Si/No)? ")) == "Si"
    return lista

def imprime_compras(diccionario):
    print("\nLista de compras")
    suma = 0
    for key in diccionario:
        print(key, "\t", diccionario[key])
        suma = suma + diccionario[key]
    print("Total \t", suma)
    
def main():
    diccionario = lista_compras()
    imprime_compras(diccionario)
    
main()