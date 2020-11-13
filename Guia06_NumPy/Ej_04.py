import numpy as np

# 4. Encontrar los índices que no son ceros del arreglo
array3 = np.array([1, 2, 4, 2, 4, 0, 1, 0, 0, 0, 12, 4, 5, 6, 7, 0])
onde = np.where(array3 != 0)
print('No hay ceros en: ', onde)
onde = np.where(array3 == 0)
print('Hay ceros en: ', onde)
