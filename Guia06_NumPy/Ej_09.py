import numpy as np

# 9. Crear dos arreglos al azar A y B, verificar si son iguales.
a = np.random.randint(0, 55, (6,6))
b = np.random.randint(0, 55, (6,6))
print('')
print(a)
print('')
print(b)
print('')
print((a == b).all())
print('')
print(a == b)
print('')