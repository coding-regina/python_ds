import numpy as np
# 12. Crear una matriz de 4x4 de valores aleatorios entre 1 y 10, y luego agregarle
# una fila de 0s al final.
array12a = np.random.randint(0, 11, (4, 4))
array12b = np.append(array12a, [[0, 0, 0, 0]], axis=0)
print(array12a)
print('')
print(array12b)
