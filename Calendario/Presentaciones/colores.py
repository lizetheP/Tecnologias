import colorama

colorama.init()
print(colorama.Fore.RED+"Texto color rojo")
print(colorama.Back.YELLOW+"Texto color rojo sobre fondo amarillo")
print(colorama.Style.BRIGHT+"Texto en negrita sobre fondo amarillo" + colorama.Back.RESET)
print("Texto en negrita")
print(colorama.Style.RESET_ALL + "Texto con valores originales")
print(colorama.Fore.WHITE + colorama.Back.BLUE+"Texto blanco sobre azul"+colorama.Back.RESET)
print(colorama.Fore.GREEN + "Texto verde")





