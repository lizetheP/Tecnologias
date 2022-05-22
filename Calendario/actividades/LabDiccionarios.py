def encuentra_simbolo(diccionario, divisa):
    for key in diccionario:
        if key == divisa:
            return diccionario[key]
    return "La divisa no está"

def encuentra_simbolo2(diccionario, divisa):
    simbolo = diccionario.get(divisa)
    return simbolo

def guarda_datos(nombre, edad, direccion, telefono):
    diccionario = {"Nombre": nombre, "Edad": edad, "Dirección": direccion, "Teléfono": telefono}
    return diccionario

def calcula_costo (diccionario, fruta, kilos):
    for key in diccionario:
        print("Key: ", key)
        print("Fruta: ", fruta)
        if key == fruta:
            #costo = diccionario[key] * kilos
            costo = diccionario.get(fruta) * kilos
            mensaje = str(kilos) + " kilos de " + fruta + " cuestan " + str(costo) + " pesos"
            return mensaje
    return "Lo siento, esta fruta no está disponible"

def llena_datos():
    diccionario = {}
    respuesta = 'si'
    while respuesta.lower() == 'si':
        dato = input("Dato a introducir: ")
        valor = input(dato + " : ")
        #diccionario.setdefault(dato, valor)
        diccionario[dato] = valor
        print(diccionario)
        respuesta = input("Deseas continuar (si/no): ")

def lista_compras():
    diccionario = {}
    respuesta = 'si'
    while respuesta.lower() == 'si':
        dato = input("Introduce el nombre del artículo: ")
        valor = float(input("Introduce su precio: "))
        diccionario.setdefault(dato, valor)
        #diccionario[dato] = valor
        print(diccionario)
        respuesta = input("Deseas continuar (si/no): ")
    return diccionario

def imprime_compras(diccionario):
    print("Lista de compras")
    total = 0
    for key in diccionario:
        print(key, "\t", diccionario[key])
        total = total + diccionario[key]
    print("TOTAL:\t" + str(total))
    
def menu():
    print()
    print("1. Encuentra símbolo")
    print("2. Guarda datos")
    print("3. Calcula precio")
    print("4. Llena datos")
    print("5. Lista de compras")
    print("6. Imprime compras")
    print("7. Salir")
    
def main():
    diccionario = {"Euro":'€', "Yen":'¥', "Peso": '$', "Libra esterlina": '£' }
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            divisa = input("Introduce la divisa: ")
            res = encuentra_simbolo(diccionario, divisa)
            print(res)
        elif opcion == 2:
            nombre = input("Introduce tu nombre: ")
            edad = int(input("Introduce tu edad: "))
            direccion = input("Introduce tu dirección: ")
            tel = input("Introduce tu teléfono: ")
            diccionario = guarda_datos(nombre, edad, direccion, tel)
            name = diccionario.get("Nombre")
            edge = diccionario.get("Edad")
            direc = diccionario.get("Dirección")
            tel = diccionario.get("Teléfono")
            print("%s tiene %i años, vive en %s y su número de teléfono es %s" % (name, edge, direc, tel))
        elif opcion == 3:
            tabla = {"Plátano" : 22.1, "Manzana" : 39.9, "Pera" : 18.2, "Naranja" : 15.5}
            fruta = str(input("Introduce el nombre de la fruta: "))
            kg = int(input("Introduce los kilos: "))
            res = calcula_costo (tabla, fruta, kg)
            print(res)
        elif opcion == 4:
            llena_datos()
        elif opcion == 5:
            compras = lista_compras()
            print(compras)
        elif opcion == 6:
            compras = lista_compras()
            imprime_compras(compras)
        elif opcion == 6:
            print("Adiós")
            continua = False
        else:
            print("OPCIÓN INVÁLIDA")
        
main()