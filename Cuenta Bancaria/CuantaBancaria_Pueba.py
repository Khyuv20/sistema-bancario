class Cuenta:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            raise ValueError("La cantidad debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente.")

        self.__saldo -= cantidad

class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo = 0, tasa_interes = 0):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
    def aplicar_interes(self):
        interes = self.consultar_saldo() * self.tasa_interes
        if interes > 0:
            self.depositar(interes)
        else:
            raise ValueError(
            "No se puede aplicar interés con saldo o tasa igual a cero."
        )
    
class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo = 0):
        super().__init__(titular, saldo)
        self.comision = 5

    def retirar(self,cantidad):
        super().retirar(cantidad + self.comision)

cuenta = None

while True:
    print("\n--- MENÚ BANCARIO ---")
    print("1. Crear cuenta de ahorro")
    print("2. Crear cuenta corriente")
    print("3. Consultar saldo")
    print("4. Depositar")
    print("5. Retirar")
    print("6. Aplicar interés")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion =="1":
        titular = input("Ingrese el nombre del titular: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        tasa_interes = float(input( "Ingrese la tasa de interés (ejemplo: 0.10 para 10%): "))
        cuenta = CuentaAhorro(titular, saldo_inicial, tasa_interes)
        print(f"Cuenta de ahorro creada para {titular} con saldo inicial de {saldo_inicial} y tasa de interés de {tasa_interes*100}%.")
    elif opcion == "2":
        titular = input("Ingrese el nombre del titular: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        cuenta = CuentaCorriente(titular, saldo_inicial)
        print(f"Cuenta corriente creada para {titular} con saldo inicial de {saldo_inicial}.")
    elif opcion == "3":
        if cuenta is None:
            print("No hay ninguna cuenta creada.")
        else:
            print(f"Saldo: {cuenta.consultar_saldo()}")
    elif opcion == "4":
        if cuenta is None:
            print("No hay ninguna cuenta creada.")
        else:
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
                print(f"Se ha depositado {cantidad}. Nuevo saldo: {cuenta.consultar_saldo()}")
            except ValueError as error:
                print(error)
    elif opcion == "5":
        if cuenta is None:
            print("No hay ninguna cuenta creada.")
        else:
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
                print(f"Se han retirado {cantidad}. Nuevo saldo: {cuenta.consultar_saldo()}")
            except ValueError as error:
                print(error)
    elif opcion == "6":
        if cuenta is None:
            print("No hay ninguna cuenta creada.")
        elif isinstance(cuenta, CuentaAhorro):
            try:
                cuenta.aplicar_interes()
                print("Interés aplicado.")
            except ValueError as error:
                print(error)
        else:
            print(
            "La opción de aplicar interés solo está disponible "
            "para cuentas de ahorro."
        )
    elif opcion == "7":
        break
    else:
        print("Opción no válida.")