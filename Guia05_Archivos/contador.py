# Ejercicio 2
# Crear un script llamado counter.py que realice varias tareas sobre un fichero llamado
# contador.txt que almacenará un counter de visitas (será un número):
# ● Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe
#   o está vacío lo crearemos con el número 0. Si existe simplemente leeremos
#   el valor del counter.
# ● Luego a partir de un argumento:
# ● Si se envía el argumento inc, se incrementará el counter en uno
#   y se mostrará por pantalla.
# ● Si se envía el argumento dec, se decrementará el counter en uno
#   y se mostrará por pantalla.
# ● Si no se envía ningún argumento (o algo que no sea inc o dec), se
#   mostrará el valor del counter por pantalla.
# ● Finalmente guardará de nuevo el valor del counter de nuevo en el fichero.
# ● Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje:
#   Error: Fichero corrupto.

import os


def check_file_existance(file_path):  # chequea si existe el archivo
    try:
        with open(file_path, 'r+') as f:
            if os.path.getsize(file_path) == 0:  # si el archivo está vacío
                f.write('0')
                f.close()
            else:  # si el archivo no está vacío
                inner_counter = int(f.read()) + ask()
                f.seek(0)
                f.write(str(inner_counter))
                print('Contador en',inner_counter)
                f.close()
            return True
    except FileNotFoundError as e:
        print('ERROR: El archivo no existe.\nEl Archivo \'contador.txt\' ha sido creado e inicializado.')
        with open(file_path, 'w+') as f:
           f.write('0')
           f.close()
        return False
    except IOError as e:
        print('ERROR: El archivo está dañado.\n', e)
        return False


def ask():
    option1 = (input('[C]reciente, [D]ecreciente, [M]ostrar? ')).lower()
    if option1 == 'c':
        increment = 1
    elif option1 == 'd':
        increment = -1
    else:
        increment = 0
    return increment


file = 'contador.txt'
check_file_existance(file)
