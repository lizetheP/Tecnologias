num = int(input("Introduce un número entre 1 y 31: "))
if num < 0 or num > 31:
    print("ERROR NÚMERO NO VALIDO")
else:
    dia = num % 7
    if dia == 0:
        print("El dia %i es %s" % (num, "DOMINGO"))
    elif dia == 1:
        print("El dia %i es %s" % (num, "LUNES"))
    elif dia == 2:
        print("El dia %i es %s" % (num, "MARTES"))
    elif dia == 3:
        print("El dia %i es %s" % (num, "MIERCOLES"))
    elif dia == 4:
        print("El dia %i es %s" % (num, "JUEVES"))
    elif dia == 5:
        print("El dia %i es %s" % (num, "VIERNES"))
    elif dia == 6:
        print("El dia %i es %s" % (num, "SABADO"))
        
        
        