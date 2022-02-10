a = 10
b = 3
bandera = 1
while bandera == 1:
    c = a % b 
    a = b
    b = c  
    if c == 0:
        bandera = 0
print("a: ", a)
print("b: ", b)
print("c: ", c)


