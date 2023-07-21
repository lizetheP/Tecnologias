def calcula_precio(diccionario, fruta, kilos):
    valor = diccionario[fruta]
    precio = valor * kilos
    return precio

def main():
    tabla = {"Plátano" : 22.1, "Manzana" : 39.9, "Pera" : 18.2, "Naranja" : 15.5}
    fruta = str(input("Introduce el nombre de la fruta: "))
    kg = float(input("Introduce los kilos: "))
    #if fruta in tabla:
    if tabla.get(fruta) != None:
        precio = calcula_precio(tabla, fruta, kg)
        print(kg, "kilos de", fruta, "cuestan", precio, "pesos")
        print("%.1f kilos de %s cuestan %.2f pesos" % (kg, fruta, precio))
    else:
        print("Lo siento, esta fruta no está disponible.")
main()