# 13. Crear dos arreglos de 6 elementos de valores aleatorios entre 0 y 1 y luego
# realizar las operaciones lógicas and y or con los métodos de NumPy.
import numpy as np
array13a = np.random.randint(0, 2, (1,6))
array13b = np.random.randint(0, 2, (1,6))
array13c = np.logical_and(array13a, array13b)
array13d = np.logical_or(array13a, array13b)
print(array13a)
print(array13b)
print('AND: ', array13c)
print('OR : ', array13d)