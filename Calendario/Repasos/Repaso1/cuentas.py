import colorama

colorama.init()
print(colorama.Style.BRIGHT)
print("MENU PRINCIPAL \n")
print("a. Muestra los tipos de cuenta de ahorro")
print("b. Calcular el saldo después de intereses o comisiones")
print("s. Salir")
print(colorama.Fore.RESET)
print(colorama.Style.NORMAL)
opcion = str(input("Introduce una opcion: "))
if opcion == 'a' or opcion == 'A':
    print(colorama.Back.WHITE + colorama.Fore.RED + colorama.Style.BRIGHT)
    print("Banco \t \t Nombre de  \t \t Tasa de    \t Saldo     Cuota por ")
    print("            \t cuenta            \t interes         minimo    manejo")
    print("                                      \t mensual                   de cuenta")
    print("----------------------------------------------------------------------------------------")
    print("Bancomer \t Libreton     \t \t 1.05% \t\t $750.00    $75.00 ")
    print("Banorte  \t Banorte Facil  \t 1.35% \t\t $1000.00   $75.00 ")
    print("Scotiabank \t Ahorro Scotiabank  \t 0.9% \t\t $2000.00   $60.00 ")
    print(colorama.Style.RESET_ALL)
elif opcion == 'b' or opcion == 'B':
    saldo = float(input("Dame el saldo inicial: "))
    print(colorama.Style.BRIGHT)
    print("TIPO DE CUENTA");
    print("a. Libreton ")
    print("b. Banorte facil")
    print("c. Ahorro Scotiabank")
    opcion2 = str(input("Introduce una opcion: "))
    print(colorama.Style.NORMAL)
    if opcion2 == 'a' or opcion == 'A':
        if saldo < 750:
            saldof = saldo - 75
        else:
            interes = saldo * 1.05/100
            saldof = saldo + interes
        print("El saldo final es %f" % saldof)
    elif opcion2 == 'b' or opcion == 'B':
        if saldo < 1000:
            saldof = saldo - 75
        else:
            interes = saldo * 1.35/100
            saldof = saldo + interes
        print("El saldo final es: " +colorama.Style.BRIGHT +"%.2f" % saldof)
        print(colorama.Style.NORMAL)
    elif opcion2 == 'b' or opcion == 'B':
        if saldo < 2000:
            saldof = saldo - 60
        else:
            interes = saldo * .9/100
            saldof = saldo + interes
        print("El saldo final es %f" % saldof)
    else:
        print("ERROR opcion invalida")
elif opcion == 's' or opcion == 'S':
    print("ADIOS")
    exit()
else:
    print("ERROR Opcion invalida")