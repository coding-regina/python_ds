# Ejercicio 2
# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad
# (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construir los siguientes
# métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# ● mostrar(): Muestra los datos de la cuenta.
# ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# ● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    def saldo(self):
        print('Su saldo es de $ {:,.2f}'.format(self.__cantidad).replace(',', '@').replace('.', ',').replace('@',
                                                                                                              '.'))
    def mostrar(self):
        print(f"Titular: {self.titular}")
        self.saldo()

    def ingresar(self):
        monto = float(input('Ingrese importe a depositar: $ '))
        if monto > 0:
            self.__cantidad += monto
        self.saldo()

    def retirar(self):
        self.__cantidad -= float(input('Ingrese importe a extraer: $ '))
        self.saldo()



k001 = Cuenta("Juan Pérez")
k002 = Cuenta("Ana García", 100500.34)

k001.mostrar()
k001.ingresar()
k001.retirar()
k002.mostrar()