# Ejercicio 8:
# Crear un programa que pregunte al usuario una cantidad a invertir , el interés anual y el
# número de años, y muestre por pantalla el capital obtenido en la inversión.

def inicia():
    inversion = float(pide_data('Ingrese capital a invertir: '))
    interes_anual = float(pide_data('Ingrese % de interés anual: '))
    agnos = int(pide_data('Ingrese cantidad de años: '))
    calcula(inversion, interes_anual, agnos)

def pide_data(alguna):
    return input(alguna)

def calcula(inversion, interes_anual, agnos):
    ganancia = inversion * (interes_anual / 100) * agnos
    capital_final = inversion + ganancia
    imprime('El capital final al cabo de ' + str(agnos) + ' año/s, será de ' + str(capital_final))

def imprime(algo):
    print(algo)

inicia()