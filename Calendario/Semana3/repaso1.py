"""Algoritmo: Cuentas bancarias
var
   caracter : opcion1, opcion2
   real : saldo, saldof, interes
inicio
   escribir("MENU
                a. Mostrar tabla
                b. Calcular saldo
                s. Salir   ")
   Pedir opcion1
   si opcion1 = 'a' o opcion1 ='A'
           escribir("Mostrar tabla...")
   sino si opcion1 = 'b' o opcion1 = 'B'
           Pedir el saldo
           escribir ("MENU 2
                TIPO DE CUENTA
                a. Libreton
                b. Banorte Fácil
                c. Ahorro Scotiabank ")
           Pedir opcion2
           si opcion2 = 'a' o opcion2 ='A'
                  si saldo < 750
                      saldof = saldo - 75
                  sino
                      interes = saldo*1.05/100
                      saldof = saldo + interes
                  escribir("saldof")
           sino si opcion2 = 'b' o opcion2 ='B'
                  si (saldo < 1000)
                      saldof = saldo - 75
                  si_no
                      interes = saldo*1.35/100
                      saldof = saldo + interes
                  escribir("saldof")
            sino si opcion2 = 'c' o opcion2 ='C'
                  si (saldo < 2000)
                      saldof = saldo - 60
                  si_no
                      interes = saldo*0.9/100
                      saldof = saldo + interes
                  escribir("saldof")
            sino
                  esciribr("Opción invalida")
   sino si opcion1 = 's' o opcion1 = 'S'
        salir del programa
   sino
           escribir ("Opción invalida")"""
    

print("MENU PRINCIPAL")
print("a. Muestra los tipos de cuenta de ahorro")
print("b. Calcular el saldo después de intereses o comisiones")
print("s. Salir")
opcion1 = str(input("Introduce una opcion: "))
if opcion1 == 'a' or opcion1 == 'A':
    print("Banco \t \t Nombre de  \t \t Tasa de    \t Saldo     Cuota por ")
    print("            \t cuenta            \t interes         minimo    manejo")
    print("                                      \t mensual                   de cuenta")
    print("----------------------------------------------------------------------------------------")
    print("Bancomer \t Libreton     \t \t 1.05% \t\t $750.00    $75.00 ")
    print("Banorte  \t Banorte Facil  \t 1.35% \t\t $1000.00   $75.00 ")
    print("Scotiabank \t Ahorro Scotiabank  \t 0.9% \t\t $2000.00   $60.00 ")
elif opcion1 == 'b' or opcion1 == 'B':
    saldo = float(input("Introduce el saldo: "))
    print("\nTIPO DE CUENTA")
    print("a. Libreton ")
    print("b. Banorte facil")
    print("c. Ahorro Scotiabank")
    opcion2 = str(input("Introduce una opcion: "))
    if opcion2 == 'a' or opcion2 == 'A':
        if saldo < 750:
            saldof = saldo - 75
        else:
            interes = saldo * 1.05/100
            saldof = saldo + interes
            print("El saldo final es %f" % saldof)
    elif opcion2 == 'b' or opcion2 == 'B':
        if saldo < 1000:
            saldof = saldo - 75
        else:
            interes = saldo * 1.35/100
            saldof = saldo + interes
            print("El saldo final es %f" % saldof)
    elif opcion2 == 'c' or opcion2 == 'C':
        if saldo < 2000:
            saldof = saldo - 60
        else:
            interes = saldo * .9/100
            saldof = saldo + interes
            print("El saldo final es %f" % saldof)
    else:
        print("ERROR opcion invalida")
elif opcion1 == 'S' or opcion1 == 's':        
        print("ADIOS");
        exit()
else:
        print("ERROR Opcion invalida")
