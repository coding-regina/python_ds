import pandas as pd
import numpy as np
df = pd.read_csv('../Guia_Pandas/titanic3.csv')


print('Devuelve el valor máximo de cada col')
print(df.max())