def calcula_precio(diccionario, fruta, kilos):
    valor = diccionario[fruta]
    precio = valor * kilos
    return precio

def main():
    tabla = {"Plátano" : 22.1, "Manzana" : 39.9, "Pera" : 18.2, "Naranja" : 15.5}
    fruta = str(input("Introduce el nombre de la fruta: "))
    kg = int(input("Introduce los kilos: "))
    if fruta in tabla:
        precio = calcula_precio(tabla, fruta, kg)
        print(kg, "kilos de", fruta, "cuestan", precio, "pesos")
    else:
        print("Lo siento, esta fruta no está disponible.")
main()