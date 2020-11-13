# Ejercicio 9:
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
# hacer venta por correo y la empresa de logística les cobra por el peso de cada paquete
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete
# a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea
# el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
# del paquete que será enviado. Mostrar el resultado por pantalla.

def peso_unit(que):
    return 112 if que == 'payaso' else 75

def pide_ventas(que):
    unidades = input('Unidades de ' + que + ' vendidas: ')
    return int(unidades)

def imprime(algo):
    print(algo)

def peso_total():
    peso_total = ((peso_unit('payaso') * pide_ventas('payaso')) + (peso_unit('muñeca') * pide_ventas('muñeca'))) / 1000
    imprime('El despacho tiene un peso de ' + str(peso_total) + ' kg')

peso_total()