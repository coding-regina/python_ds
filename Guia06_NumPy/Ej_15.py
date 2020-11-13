# 15. Crear una matriz que contenga información en distintos formatos, imprimir la info
# de cada formato a través del atributo.
import numpy as np
array15 = ([['Juan', 20, 50.43],
            ['Felicia', 34, 44.24],
            ['Jorge', 42, 43.55],
            ['Laura', 39, 67.33]])

for fila in array15:
    for item in fila:
        print(type(item))
ar = np.array(array15)
print(ar.shape)
print(ar.size)
