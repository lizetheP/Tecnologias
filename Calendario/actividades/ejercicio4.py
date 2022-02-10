def llena_datos():
    persona = {}
    continuar = True
    while continuar == True:
        clave = str(input("¿Qué dato quieres introducir? "))
        valor = input(clave + ": ")
        persona[clave] = valor
        print(persona)
        continuar = str(input("¿Quieres agregar más información (Si/No)? ")) == "Si"

def main():
    llena_datos()
    
main()