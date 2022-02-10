def guarda_datos(nombre, edad, direccion, telefono):
    diccionario = {"nombre" : nombre, "edad" : edad, "direccion" : direccion, "tel" : telefono}
    return diccionario

def main():
    nombre = str(input("Introduce tu nombre: "))
    edad = int(input("Introduce tu edad: "))
    direccion = str(input("Introduce tu dirección: "))
    telefono = str(input("Introduce tu número de teléfono: "))
    diccionario = guarda_datos(nombre, edad, direccion, telefono)
    name = diccionario.get("nombre")
    edge = diccionario.get("edad")
    direc = diccionario.get("direccion")
    tel = diccionario.get("tel")
    print("%s tiene %i años, vive en %s y su número de teléfono es %s" % (name, edge, direc, tel))
    
main()