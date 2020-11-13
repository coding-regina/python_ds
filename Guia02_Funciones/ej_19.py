# Ejercicio 19:
# Crear un programa en el que se pregunte al usuario por una frase y una letra, y
# muestre por pantalla el número de veces que aparece la letra en la frase.
async
def dame(algo):
    return (input(algo))

def ocurrencias(frase, letra):
    return frase.count(letra)

def imprime(algo):
    print(algo)

imprime('Aparece ' + str(ocurrencias(dame('Ingrese una frase: '), dame('Ingrese una letra: '))) + ' veces')