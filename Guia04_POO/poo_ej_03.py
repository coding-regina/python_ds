# Ejercicio 3
# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del
# titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por
# ciento. Construir los siguientes métodos para la clase:
# ● Un constructor.
# ● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
# edad., por lo tanto hay que crear un método esTitularValido() que devuelve
# verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
# contrario.
# ● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# ● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la # bonificación de la cuenta.
# ● Pensar los métodos heredados de la clase madre que hay que reescribir.

from datetime import date
from datetime import datetime

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def saldo(self):
        print('Saldo: $ {:,.2f}'.format(self.cantidad).replace(',', '@').replace('.', ',').replace('@',
                                                                                                              '.'))
    def mostrar(self):
        print(f"Titular: {self.titular}")
        self.saldo()

    def ingresar(self):
        monto = float(input('Ingrese importe a depositar: $ '))
        if monto > 0:
            self.cantidad += monto
        self.saldo()

    def retirar(self):
        self.cantidad -= float(input('Ingrese importe a extraer: $ '))
        self.saldo()

class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,agno_nac,bonif):
        super().__init__(titular, cantidad)
        self.__agno_nac = agno_nac
        self.bonif = bonif

    def esTitularValido(self):
        now = datetime.now()
        edad = now.year - self.__agno_nac
        esValido = False
        if edad >= 18 and edad <= 25:
            esValido = True
        return esValido

    def retirar(self):
        if self.esTitularValido():
            self.cantidad -= float(input('Ingrese importe a extraer: $ '))
            self.saldo()
        else:
            print('Su cuenta no permite extracciones.')

    def mostrar(self):
        print('Cuenta Joven')
        super().mostrar()
        print(f'Bonificación: {self.bonif}%\n---------------------------------')


ana = CuentaJoven('Ana López', 1000,1990, 10)
juan = CuentaJoven('Juan Gutiérrez', 5000, 1997,20)
ana.retirar()
ana.mostrar()

juan.mostrar()
juan.ingresar()