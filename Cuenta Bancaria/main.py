from cuentas import CuentaAhorro, CuentaCorriente
from banco import Banco, Cliente

def main():
    banco = Banco("Mi Banco")

    while True:
        print("\n--- Banco ---")
        print("1. Crear cuenta de ahorro")
        print("2. Crear cuenta corriente")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Transferir")
        print("6. Aplicar interés")
        print("7. Consultar saldo")
        print("8. Consultar historial")
        print("9. Salir")

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
                numero_cuenta = int(input("Ingrese el número de cuenta: "))
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                banco.depositar(numero_cuenta, cantidad)
                print(f"Se han depositado {cantidad} en la cuenta {numero_cuenta}.")
            except ValueError as error:
                print(f"Error: {error}")
        
        elif opcion == "4":
            try:
                numero_cuenta = int(input("Ingrese el número de cuenta: "))
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                banco.retirar(numero_cuenta, cantidad)
                print(f"Se han retirado {cantidad} de la cuenta {numero_cuenta}.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "5":
            try:
                numero_origen = int(input("Ingrese el número de cuenta de origen: "))
                numero_destino = int(input("Ingrese el número de cuenta del destino: "))
                cantidad = float(input("Ingrese la cantidad a transferir: "))
                
                banco.transferir(numero_origen, numero_destino, cantidad)
                print(f"Se ha transfeirdo {cantidad} a {numero_destino}")
            
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "6":
            try:
                numero_cuenta = int(input("Ingrese el número de cuenta: "))
                banco.aplicar_interes(numero_cuenta)
                print(f"Se ha aplicado el interés a la cuenta {numero_cuenta}.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "7":
            try:
                cuenta_numero = int(input("Ingrese el número de cuenta: "))
                saldo = banco.consultar_saldo(cuenta_numero)
                print(f"Saldo de la cuenta {cuenta_numero}: {saldo}")
            except ValueError as error:
                print(f"Error: {error}")
                
        elif opcion == "8":
            try:
                numero_cuenta = int(input("Ingrese el número de cuenta: "))
                historial = banco.consultar_historial(numero_cuenta)
                
                for moviemiento in historial:
                    print(moviemiento)
                    
            except ValueError as error:
                print(f"Error: {error}")
                
        elif opcion == "9":
            print("Gracias por utilizar el sistema bancario.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()