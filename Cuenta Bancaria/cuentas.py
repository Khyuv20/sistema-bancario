
class Cuenta:
# Contador compartido por todas las cuentas para generar
# números de cuenta únicos automáticamente.
    siguiente_numero = 1000

    def __init__(self, titular, saldo = 0):
        if not isinstance (titular, str):
            raise ValueError ("El titular debe ser texto")
        
        if titular.strip() == "":
            raise ValueError ("El titular no debe estar vacío")
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        
        self.historial = []
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
    
    def consultar_historial(self,):
        return self.historial

    def _descontar_saldo(self, cantidad):
        self.__saldo -= cantidad
    
    def depositar(self, cantidad, registrar = True):
        if cantidad > 0:
            self.__saldo += cantidad
            if registrar:
                self.historial.append(f"Depósito: {cantidad}")
        else:
            raise ValueError("La cantidad debe ser mayor que 0.")

    def retirar(self, cantidad, registrar = True):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        

        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente.")

        self.__saldo -= cantidad
        if  registrar:
            self.historial.append(f"Retiro: {cantidad}")
        return cantidad

    # Permite mostrar la información de una cuenta con print(cuenta).
    def __str__(self):
        return (
        f"Titular: {self.titular},"
        f"Cuenta: {type(self).__name__},"
        f"Saldo: {self.consultar_saldo()},"
        f"Número de cuenta: {self.numero_cuenta}"
        )

class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo = 0, tasa_interes = 0):
        super().__init__(titular, saldo)
        
        if tasa_interes < 0:
            raise ValueError("La tasa de interés no puede ser negativa.")

        self.tasa_interes = tasa_interes
        
    def aplicar_interes(self):
        # Calcula el interés utilizando el saldo actual de la cuenta.
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
        # El límite es privado para evitar modificarlo directamente.
        self.__limite_sobregiro = limite_sobregiro
        self.comision = comision
    # Sobrescribe retirar() de Cuenta para incluir
    # comisión y permitir sobregiro hasta el límite establecido.
    def retirar(self,cantidad, registrar = True):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        # La comisión también forma parte del dinero descontado.
        total_retiro = cantidad + self.comision
        saldo_final = self.consultar_saldo() - total_retiro

        if saldo_final < -self.__limite_sobregiro:
            raise ValueError("Se ha excedido el límite de sobregiro.")

        self._descontar_saldo(total_retiro)
        if registrar == True:
            self.historial.append(
            f"Retiro: ${cantidad} | Comisión: ${self.comision} | Total descontado: ${total_retiro}")
        return total_retiro
