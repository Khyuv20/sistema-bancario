
# ==== CLASES ===

class Cuenta:
# Contador compartido por todas las cuentas para generar
# números de cuenta únicos automáticamente.
    siguiente_numero = 1000

    def __init__(self, titular, saldo = 0):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        
        self.titular = titular
        # El saldo es privado para evitar modificarlo directamente
        # desde fuera de la clase.
        self.__saldo = saldo
        
        # Cada cuenta recibe el número actual y después
        # el contador aumenta para la siguiente cuenta.
        self.numero_cuenta = Cuenta.siguiente_numero
        Cuenta.siguiente_numero += 1

    def consultar_saldo(self):
        return self.__saldo
    
    # Método protegido pensado para que las clases hijas
    # puedan descontar saldo sin acceder directamente a __saldo.
    def _descontar_saldo(self, cantidad):
        self.__saldo -= cantidad
    
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

    # Permite mostrar la información de una cuenta con print(cuenta).
    def __str__(self):
        return (
        f"Titular: {self.titular},"
        f"Cuenta: {type(self).__name__},"
        f"Saldo: {self.consultar_saldo()},"
        f"Número de cuenta: {self.numero_cuenta}"
        )

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente(self, identificador):
        for cliente in self.clientes:
            if cliente.identificador == identificador:
                return cliente
        return None

    def buscar_cuenta(self, numero_cuenta):
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    return cuenta
        return None

    def depositar(self,numero_cuenta, cantidad):
        cuenta = self.buscar_cuenta(numero_cuenta)
        if cuenta is None:
            raise ValueError("Cuenta no encontrada.")
        cuenta.depositar(cantidad)

    def retirar(self, numero_cuenta, cantidad):
        cuenta = self.buscar_cuenta(numero_cuenta)
        if cuenta is None:
            raise ValueError("Cuenta no encontrada.")
        cuenta.retirar(cantidad)

    def consultar_saldo(self, numero_cuenta):
        cuenta = self.buscar_cuenta(numero_cuenta)
        if cuenta is None:
            raise ValueError("Cuenta no encontrada.")
        return cuenta.consultar_saldo()
    
    def aplicar_interes(self, numero_cuenta):
        cuenta = self.buscar_cuenta(numero_cuenta)
        if cuenta is None:
            raise ValueError("Cuenta no encontrada.")
        if isinstance(cuenta, CuentaAhorro):
            cuenta.aplicar_interes()
        else:
            raise ValueError(
            "La opción de aplicar interés solo está disponible "
            "para cuentas de ahorro."
            )

    def agregar_cuenta(self, identificador, cuenta):
        cliente = self.buscar_cliente(identificador)
        if cliente is None:
            raise ValueError("Cliente no encontrado.")
        cliente.agregar_cuenta(cuenta)

class Cliente:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_cuentas(self):
        if not self.cuentas:
            print("El cliente no tiene cuentas registradas.")
            return

        for cuenta in self.cuentas:
            print(cuenta)

class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo = 0, tasa_interes = 0):
        super().__init__(titular, saldo)
        
        if tasa_interes < 0:
            raise ValueError("La tasa de interés no puede ser negativa.")

        self.tasa_interes = tasa_interes
        
    def aplicar_interes(self):
        interes = self.consultar_saldo() * self.tasa_interes
        if interes <= 0:
            raise ValueError(
            "No se puede aplicar interés con saldo o tasa igual a cero."
            )
        self.depositar(interes)

class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo = 0, comision = 5, limite_sobregiro = 500):
        super().__init__(titular, saldo)
        
        if limite_sobregiro < 0:
            raise ValueError("El límite de sobregiro no puede ser negativo.")
        
        if comision < 0:
            raise ValueError("La comisión no puede ser negativa.")
        
        self.__limite_sobregiro = limite_sobregiro
        self.comision = comision

    def retirar(self,cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        total_retiro = cantidad + self.comision
        saldo_final = self.consultar_saldo() - total_retiro

        if saldo_final < -self.__limite_sobregiro:
            raise ValueError("Se ha excedido el límite de sobregiro.")

        self._descontar_saldo(total_retiro)

#  === MENU ===
banco = Banco("Mi Banco")

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

    if opcion == "1":
        try:
            identificador = int(input("Ingrese el ID del cliente: "))
            cliente = banco.buscar_cliente(identificador)

            cliente_nuevo = False

            if cliente is None:
                nombre = input("Ingrese el nombre del cliente: ")
                cliente = Cliente(identificador, nombre)
                cliente_nuevo = True

            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            tasa_interes = float(input("Ingrese la tasa de interés: "))

            cuenta = CuentaAhorro(
                cliente.nombre,
                saldo_inicial,
                tasa_interes
            )

            cliente.agregar_cuenta(cuenta)

            if cliente_nuevo:
                banco.agregar_cliente(cliente)

            print(
                f"Cuenta de ahorro creada para {cliente.nombre}. "
                f"Número de cuenta: {cuenta.numero_cuenta}"
            )

        except ValueError as error:
            print(f"Error: {error}")

    elif opcion == "2":
        try:
            identificador = int(input("Ingrese el ID del cliente: "))
            cliente = banco.buscar_cliente(identificador)

            cliente_nuevo = False

            if cliente is None:
                nombre = input("Ingrese el nombre del cliente: ")
                cliente = Cliente(identificador, nombre)
                cliente_nuevo = True

            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            comision = float(input("Ingrese la comisión: "))
            limite_sobregiro = float(
                input("Ingrese el límite de sobregiro: ")
            )

            cuenta = CuentaCorriente(
                cliente.nombre,
                saldo_inicial,
                comision,
                limite_sobregiro
            )

            cliente.agregar_cuenta(cuenta)

            if cliente_nuevo:
                banco.agregar_cliente(cliente)

            print(
                f"Cuenta corriente creada para {cliente.nombre}. "
                f"Número de cuenta: {cuenta.numero_cuenta}"
            )

        except ValueError as error:
            print(f"Error: {error}")
        
    elif opcion == "3":
        try:
            cuenta_numero = int(input("Ingrese el número de cuenta: "))
            saldo = banco.consultar_saldo(cuenta_numero)
            print(f"Saldo de la cuenta {cuenta_numero}: {saldo}")
        except ValueError as error:
            print(error)
            
    elif opcion == "4":
        
        try:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            banco.depositar(numero_cuenta, cantidad)
            print(f"Se han depositado {cantidad} en la cuenta {numero_cuenta}.")
        except ValueError as error:
            print(error)
    
    elif opcion == "5":
        try:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            banco.retirar(numero_cuenta, cantidad)
            print(f"Se han retirado {cantidad} de la cuenta {numero_cuenta}.")
        except ValueError as error:
            print(error)

    elif opcion == "6":
        try:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            banco.aplicar_interes(numero_cuenta)
            print(f"Se ha aplicado el interés a la cuenta {numero_cuenta}.")
        except ValueError as error:
            print(error)
    
    elif opcion == "7":
        break
    else:
        print("Opción no válida.")

print(cuenta)