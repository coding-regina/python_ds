# Ejercicio 14:
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los
# puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
# aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
# los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las
# cifras mencionadas.  A continuación se muestra una tabla con los niveles
# correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel
# es de 100000 multiplicada por la puntuación del nivel.
# Nivel Puntuación
# Inaceptable 0.0
# Aceptable 0.4
# Meritorio 0.6 o más
# Crear un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
# así como la cantidad de dinero que recibirá el usuario.

def puntua():
    puntuacion = float(input('Ingrese puntuación del empleado: '))
    if puntuacion < 0.4 :
        nivel = 'Inaceptable'
        multiplicador = 0
    elif puntuacion < 0.6 :
        nivel = 'Aceptable'
        multiplicador = 0.4
    else:
        nivel = 'Meritorio'
        multiplicador = 0.6
    bonificacion = multiplicador * 100000
    print('El nivel del empleado es ' + nivel + '\nBonificación obtenida: $ {:,.2f}'.format(bonificacion).replace(",", "@").replace(".", ",").replace("@", "."))

puntua()