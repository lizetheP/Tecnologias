def escribe_cadena(cadena, ruta):
    file = open (ruta, "w")
    for i in range(0, len(cadena)):
        print("%c" % cadena[i], end="")
        file.write(cadena[i].upper())
    file.close()

def main():
    frase = str(input("Introduce una frase: "))
    ruta = str(input("Introduce la ruta del archivo de texto: "))
    escribe_cadena(frase, ruta)

main()
