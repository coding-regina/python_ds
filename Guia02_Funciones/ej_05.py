# Ejercicio 5:
# Crear un programa que pregunte el nombre del usuario y después de que el usuario lo
# introduzca muestre por pantalla <NOMBRE> tiene <n> letras.

def pide_dato(algo):
    dato = input(algo)
    return dato

def cuenta_letras(cadena):
    return str(len(cadena.replace(' ','')))

nombre = pide_dato('Ingrese su nombre: ')
print('Su nombre tiene ', cuenta_letras(nombre), ' letras')