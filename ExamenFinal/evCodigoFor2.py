for m in range(1, 5):
    for n in range(4, 0, -1):
        if n == 1 or n == 4 or m == 1 or m == 4:
            print("*", end="")
        else:
            print("#", end="")
    print() # Salto de línea
    
