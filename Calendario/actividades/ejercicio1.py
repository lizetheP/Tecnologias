def encuentra_simbolo(diccionario, divisa):
    simbolo = diccionario.get(divisa)
    simbolo2 = diccionario[divisa]
    return simbolo, simbolo2

def main():
    monedas = {"Euro":'€', "Yen":'¥', "Peso": '$', "Libra esterlina": '£' }
    divisa = str(input("Introduce una divisa: "))
    simbolo, simbolo2 = encuentra_simbolo(monedas, divisa)
    print("Símbolo:", simbolo)
    print("Símbolo2:", simbolo2)
    
main()