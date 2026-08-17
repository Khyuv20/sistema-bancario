from cuentas import CuentaAhorro

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def agregar_cliente(self, cliente):
        cliente_existente = self.buscar_cliente(cliente.identificador)
        if cliente_existente is not None:
            raise ValueError ("Ya existe un cliente con este identificador")
        self.clientes.append(cliente)

    def agregar_cuenta(self, identificador, cuenta):
        cliente = self.buscar_cliente(identificador)
        if cliente is None:
            raise ValueError("Cliente no encontrado.")
        cuenta_existente = self.buscar_cuenta(cuenta.numero_cuenta)
        if cuenta_existente is not None:
            raise ValueError ("La cuenta ya esta regsitrada")
        cliente.agregar_cuenta(cuenta)
        
    def buscar_cliente(self, identificador):
        for cliente in self.clientes:
            if cliente.identificador == identificador:
                return cliente
        return None

    def buscar_cuenta(self, numero_cuenta):
        # Recorre todos los clientes y sus cuentas
        # hasta encontrar el número de cuenta solicitado.
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
    
    def consultar_historial(self, numero_cuenta):
        cuenta = self.buscar_cuenta(numero_cuenta)
        
        if cuenta is None:
            raise ValueError("Cuenta no encontrada")
        
        return cuenta.consultar_historial()
        
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

    
    def transferir(self, numero_origen, numero_destino, cantidad):
        cuenta_origen = self.buscar_cuenta(numero_origen)
        cuenta_destino = self.buscar_cuenta(numero_destino)
        
        if cuenta_origen is None or cuenta_destino is None:
            raise ValueError("Una o ambas cuentas no fueron encontradas.")
        
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        if cuenta_origen == cuenta_destino:
            raise ValueError("No se puede transferir a la misma cuenta.")
        
        total_descontado = cuenta_origen.retirar(cantidad, False)
        
        try:
            cuenta_destino.depositar(cantidad, False)
        except ValueError:
            cuenta_origen.depositar(total_descontado, False)
            raise
        
        cuenta_origen.historial.append(f"Transferencia enviada: {cantidad} → Cuenta {numero_destino}")
        cuenta_destino.historial.append(f"Transferencia recibida: {cantidad} ← Cuenta {numero_origen}")

class Cliente:
    def __init__(self, identificador, nombre):
        if not isinstance (identificador, int):
            raise ValueError ("El identificador debe ser un número")
        if identificador <= 0:
            raise ValueError ("El identificadro debe ser mayor a 0")
        
        if nombre.strip() == "":
            raise ValueError ("El nombre no puede estar vacío")
        self.identificador = identificador
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        for cuenta_existente in self.cuentas:
            if cuenta_existente.numero_cuenta ==  cuenta.numero_cuenta:
                raise ValueError ("La cuenta ya esta asociada a este cliente")
        self.cuentas.append(cuenta)

    def mostrar_cuentas(self):
        # Si el cliente no tiene cuentas, termina el método.
        if not self.cuentas:
            print("El cliente no tiene cuentas registradas.")
            return

        # Recorre y muestra cada cuenta asociada al cliente.
        for cuenta in self.cuentas:
            print(cuenta)