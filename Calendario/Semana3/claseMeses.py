mm = int(input("Introduce el mes (##): "))
aa = int(input("Introduce el año (####): "))

if mm == 1 or mm == 3 or mm == 5 or mm == 7 or \
   mm == 8 or mm == 10 or mm == 12:
    dd = 31
elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    dd = 30
elif mm == 2:
    if ((aa % 4 == 0 and aa % 100 != 0) or aa % 400 == 0):
        dd = 29
    else:
        dd = 28
else:
    print("El mes %i no es válido" % mm)

if mm >= 1 and mm <= 12:
    print("El mes %i del año %i tiene %i días" % (mm, aa, dd))
    
    
    
    