def encuentra_simbolo(diccionario, divisa):
    simbolo = diccionario.get(divisa)
    return simbolo

def main():
    monedas = {"Euro":'€', "Yen":'¥', "Peso": '$', "Libra esterlina": '£' }
    divisa = str(input("Introduce una divisa: "))
    simbolo = encuentra_simbolo(monedas, divisa)
    print("Símbolo:", simbolo)
    
main()