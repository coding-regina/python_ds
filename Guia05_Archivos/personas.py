# Ejercicio 1
# Crear un script llamado personas.py que lea los datos de un fichero de texto, que
# transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego
# recorre las personas de la lista y para cada una muestra de forma amigable todos sus
# campos.
# El fichero de texto se denominará personas.txt tendrá el siguiente contenido en texto
# plano (créalo previamente):
# 1;Carlos;Pérez;05/01/1989
# 2;Manuel;Heredia;26/12/1973
# 3;Rosa;Campos;12/06/1961
# 4;David;García;25/07/2006
#
# Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.
lista = []
with open('personas.txt', 'r') as dato:
    dato.seek(0)  # posiciona al inicio del archivo
    entrada = dato.read().replace('\xa0', ';').replace(' ', '').replace('\n', '')
    raw = entrada.split(';')
    dato.close()
i = 0
while i < len(raw):
    dictio = {'id': raw.__getitem__(i), 'nombre': raw.__getitem__(i + 1), 'apellido': raw.__getitem__(i + 2), 'nacimiento': raw.__getitem__(i + 3)}
    lista.append(dictio)
    i += 4

claves = dictio.keys()
nombres = dictio.values()

for elemento in lista:
    print('Nro.        : ', elemento.__getitem__('id'))
    print('Nombre      : ', elemento.__getitem__('apellido'), ',', elemento.__getitem__('nombre'))
    print('Fecha nacim.: ', elemento.__getitem__('nacimiento'))
    print('----------------------------------')

# personas.txt
# 1;Carlos;Pérez;05/01/1989
# 2;Manuel;Heredia;26/12/1973
# 3;Rosa;Campos;12/06/1961
# 4;David;García;25/07/2006
