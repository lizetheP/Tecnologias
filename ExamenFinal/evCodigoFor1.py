a = 1
b = 5
for m in range (1, 5):
    for n in range (1, b):
        print("*", end = "")
    for n in range (1, a):
        print("#", end = "")
    b = b - 1
    a = a + 1
    print() # Salto de línea
    
