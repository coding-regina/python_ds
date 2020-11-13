# Ejercicio 23:
# Crear un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
# de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
# mensaje informando de ello.
# Fruta Precio (kg)
# Banana 80
# Manzana 100
# Pera 50
# Naranja 70

def crea_dic():
    lista_precios = {'Banana': 80, 'Manzana': 100, 'Pera': 50, 'Naranja': 70}
    return lista_precios

def pregunta(algo):
    return input(algo)

def imprime(algo):
    print(algo)

def busca(algo, donde): #algo = key // donde = dict
    if algo in donde:
        cantidad = int(pregunta('¿Cuántos kilos precisa? '))
        imprime(str(cantidad) + ' kilos de ' + algo + ' le costarán $ ' + str((donde[algo] * cantidad)))
    else:
        imprime('No tenemos ese artículo.')

busca(pregunta('¿Qué necesita? [Banana/Manzana/Pera/Naranja]: ').capitalize(), crea_dic())