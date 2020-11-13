import numpy as np

# 3. Crear una matriz de 3x3 con los valores de 0 a 8.
array2 = np.arange(0, 9).reshape(3, 3)
print('')
print(array2)

# 6. Encontrar los índices de los valores mínimos y máximos de la matriz creada en
# el ejercicio 3.
min = np.where(array2 == array2.min())
max = np.where(array2 == array2.max())
coordMin= list(zip(min[0], min[1]))
for cord in coordMin:
    print(cord)
coordMax= list(zip(max[0], max[1]))
for cord in coordMax:
    print(cord)


