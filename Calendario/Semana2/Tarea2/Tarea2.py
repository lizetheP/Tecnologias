import math
x = int(input(" Introduce el valor de x: "))
if x <= -1:
    res = math.sqrt(x*x - 1)
elif x > -1 and x < 1:
    res = x
else:
    res = math.sqrt(x - 1)
print(" El resultado es: %.4f" % res)