class TarjetaDebito:
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def abonar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Abonado ${cantidad} a la cuenta")
        else:
            print("Se debe ingresar una cantidad mayor a 0")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("No tienes suficientes fondos")
        elif cantidad <= 0:
            print("El retiro debe ser mayor a 0")
        else:
            self.__saldo -= cantidad
            print(f"Usted a retirado {cantidad}")

    def obtenerSaldo(self):
        return self.__saldo