# Ejercicio 25:
# Crear un programa que, a partir de una lista con todas las letras del abecedario, haga
# un copia y borre de esta última todas las vocales. Luego imprimir por pantalla ambas
# listas, la completa y la sin vocales.
# Para crear la lista del abecedario se puede importar la variable ascii_lowercase del
# módulo string:
# Hay un método para eliminar elementos particulares de una lista y es remove(). Se utiliza así:

# import string library function
import string

def crea_lista(cadena):
    return list(cadena);

def desvocaliza(lista_entrada, eliminar):
    for letra in eliminar:
        lista_entrada.remove(letra)
    return lista_entrada

def imprime(algo):
	print(algo)

vocales = crea_lista('aeiou')
abc = crea_lista(string.ascii_lowercase)
imprime(abc)
imprime(desvocaliza(crea_lista(string.ascii_lowercase), vocales))