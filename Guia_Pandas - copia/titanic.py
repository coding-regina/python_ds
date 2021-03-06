import pandas as pd
import numpy as np
df = pd.read_csv('titanic3.csv')
# print(df, '\n')
# print()
# print(df.head(1))
# print()
# print(df.isnull())
# print()
# print(df.describe())
# print('\nCuenta la cantidad de datos nulos por columna')
# print(df.isnull().sum())
# print()
# print('Imprime la columna de sexo asociado al ID')
# print(df.sex) #
# print()
# print('valor booleano')
# print(df.sex == 'female')
# print()
# print('últimas 5 filas')
# print(df.tail())
# print()
# print('dimension')
# print(df.shape)
# print()
# print('labels de cada columna')
# print(df.columns.values)
# print()
# print('discrimina los valores de cada columna')
# print(df.dtypes)
# print()
# print('ordena según el nro de ticket')
# print(df.sort_values('ticket'))
print('\nVALORES FALTANTES')
print('Chequea los valores faltantes de la columna con label body')
print(pd.isnull(df.body))
print('\nChequea los valores presentes de la columna con label body')
print(pd.notnull(df.body))
print('\nArreglo con los valores faltantes de la columna label body')
print(pd.isnull(df.body).values)
print('\nCantidad de valores faltantes')
print(pd.isnull(df.body).values.sum())