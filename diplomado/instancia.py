from diplomado.tarjeta import TarjetaDebito

tarjeta_osmar = TarjetaDebito("Osmar", 1000)

tarjeta_osmar.abonar(1000)
tarjeta_osmar.retirar(500)
saldo_actual = tarjeta_osmar.obtenerSaldo()

print(f"Hola Osmar, este es su saldo actual {saldo_actual}")
