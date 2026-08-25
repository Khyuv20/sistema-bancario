import tkinter as tk
from banco import Banco, Cliente
from cuentas import CuentaAhorro, CuentaCorriente

banco = Banco("Banco")

def depositar():
    try:
        numero_cuenta = int(entrada_numero_cuenta.get())
        cantidad = float(entrada_cantidad.get())

        banco.depositar(numero_cuenta, cantidad)

        cuenta = banco.buscar_cuenta(numero_cuenta)

        mensaje.config(
            text = f"Deposito realizado. Saldo actual: {cuenta.consultar_saldo()}"
        )

        entrada_cantidad.delete(0, tk.END)
        entrada_numero_cuenta.delete(0, tk.END)

    except ValueError as error:
        mensaje.config(text = str(error))

def retirar():
    try:
        numero_cuenta = int(entrada_numero_retiro.get())
        cantidad = float(entrada_cantidad_retiro.get())
        
        banco.retirar(numero_cuenta, cantidad)
        
        cuenta = banco.buscar_cuenta(numero_cuenta)
        
        mensaje_retiro.config(
            text = f"Retiro realizado. Saldo actual: {cuenta.consultar_saldo()}"
            )
        
        entrada_numero_retiro.delete(0, tk.END)
        entrada_cantidad_retiro.delete(0, tk.END)
        
    except ValueError as error:
        mensaje_retiro.config(text = str(error))

def transferir():
    try:
        cuenta_origen = int(entrada_cuenta_origen.get())
        cuenta_destino = int(entrada_cuenta_destino.get())
        cantidad = float(entrada_cantidad_transferencia.get())

        banco.transferir(cuenta_origen, cuenta_destino, cantidad)

        cuenta = banco.buscar_cuenta(cuenta_origen)

        mensaje_transferir.config(
            text = f"Transferencia realizada con éxito. Saldo actual: {cuenta.consultar_saldo()}"
        )
        entrada_cuenta_origen.delete(0, tk.END)
        entrada_cuenta_destino.delete(0, tk.END)
        entrada_cantidad_transferencia.delete(0, tk.END)

    except ValueError as error:
        mensaje_transferir.config(text = str(error))

def historial():
    try:
        numero_cuenta = int(entrada_cuenta_historial.get())

        historial_cuenta = banco.consultar_historial(numero_cuenta)

        texto_historial.delete("1.0", tk.END)

        for movimiento in historial_cuenta:
            texto_historial.insert(tk.END, movimiento + "\n")

        entrada_cuenta_historial.delete(0, tk.END)

    except ValueError as error:
        texto_historial.delete("1.0", tk.END)
        texto_historial.insert(tk.END, str(error))

def interes():
    try:
        numero_cuenta = int(entrada_cuenta_interes.get())
        
        banco.aplicar_interes(numero_cuenta)
        
        cuenta = banco.buscar_cuenta(numero_cuenta)
        
        mensaje_interes.config(
            text = f"Intereses aplicados. Saldo acutal: {cuenta.consultar_saldo()}"
        )

    except ValueError as error:
        mensaje_interes.config(text = str(error))

def crear_cliente():
    try:
        identificador = int(entrada_identificador.get())
        nombre = entrada_nombre.get()

        cliente = Cliente(identificador, nombre)

        banco.agregar_cliente(cliente)

        mensaje_cliente.config(text="Cliente creado exitosamente")

        entrada_identificador.delete(0, tk.END)
        entrada_nombre.delete(0, tk.END)

    except ValueError as error:
        mensaje_cliente.config(text=str(error))

def crear_cuenta():
    try:
        identificador = int(entrada_cliente_cuenta.get())
        saldo_inicial = float(entrada_saldo_inicial.get())
        tipo = tipo_cuenta.get()

        if tipo == "":
            raise ValueError("Seleccione un tipo de cuenta")

        cliente = banco.buscar_cliente(identificador)

        if cliente is None:
            raise ValueError("Cliente no encontrado")

        if tipo == "ahorro":
            tasa = float(entrada_tasa.get())
            cuenta = CuentaAhorro(cliente.nombre, saldo_inicial, tasa)
            cliente.agregar_cuenta(cuenta)

        if tipo == "corriente":
            cuenta = CuentaCorriente(cliente.nombre, saldo_inicial)
            cliente.agregar_cuenta(cuenta)

        mensaje_cuenta.config(
            text=f"Cuenta creada exitosamente. Número: {cuenta.numero_cuenta}"
        )

        entrada_tasa.delete(0, tk.END)
        entrada_saldo_inicial.delete(0, tk.END)
        entrada_cliente_cuenta.delete(0, tk.END)

        tipo_cuenta.set("")
        actualizar_tipo_cuenta()

    except ValueError as error:
        mensaje_cuenta.config(text=str(error))

def actualizar_tipo_cuenta():
    if tipo_cuenta.get() == "ahorro":
        label_tasa.grid(row = 2, column = 0)
        entrada_tasa.grid(row = 2, column = 1)

    else:
        label_tasa.grid_remove()
        entrada_tasa.grid_remove()

def actualizar_operacion():
    if operacion_seleccionada.get() == "depositar":
        frame_deposito.pack()
        frame_retiro.pack_forget()
        frame_transferencia.pack_forget()
        frame_historial.pack_forget()
        frame_interes.pack_forget()
    
    if operacion_seleccionada.get() == "retirar":
        frame_retiro.pack()
        frame_deposito.pack_forget()
        frame_transferencia.pack_forget()
        frame_historial.pack_forget()
        frame_interes.pack_forget()
        
    if operacion_seleccionada.get() == "transferir":
        frame_transferencia.pack()
        frame_deposito.pack_forget()
        frame_retiro.pack_forget()
        frame_historial.pack_forget()
        frame_interes.pack_forget()

    if operacion_seleccionada.get() == "historial":
        frame_historial.pack()
        frame_deposito.pack_forget()
        frame_retiro.pack_forget()
        frame_transferencia.pack_forget()
        frame_interes.pack_forget()

    if operacion_seleccionada.get() == "interes":
        frame_interes.pack()
        frame_historial.pack_forget()
        frame_deposito.pack_forget()
        frame_retiro.pack_forget()
        frame_transferencia.pack_forget()

ventana = tk.Tk()

titulo = tk.Label(
    ventana,
    text = "Banco"
)
titulo.pack()

frame_cliente = tk.Frame(ventana)
frame_cliente.pack()

label_identificador = tk.Label(
    frame_cliente,
    text = "Identificador"
)
label_identificador.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")

entrada_identificador = tk.Entry(frame_cliente)
entrada_identificador.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "w")

label_nombre = tk.Label(
    frame_cliente,
    text = "Nombre"
)
label_nombre.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")

entrada_nombre = tk.Entry(frame_cliente)
entrada_nombre.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")

boton_crear_cliente = tk.Button(
    frame_cliente,
    text = "Crear cliente",
    command=crear_cliente
)
boton_crear_cliente.grid(row = 2, columnspan = 2, pady = 5)

mensaje_cliente = tk.Label(
    frame_cliente,
    text = ""
)
mensaje_cliente.grid(row = 3, columnspan = 2, pady = 5)

frame_cuenta = tk.Frame(ventana)
frame_cuenta.pack()

label_identificador_cliente = tk.Label(
    frame_cuenta,
    text="Identificador del cliente"
)
label_identificador_cliente.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_cliente_cuenta = tk.Entry(frame_cuenta)
entrada_cliente_cuenta.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = "w")

label_saldo_inicial = tk.Label(
    frame_cuenta,
    text = "Saldo inicial"
)
label_saldo_inicial.grid(row = 1, column = 0, pady = 5 , padx = 5, sticky = "w")

entrada_saldo_inicial = tk.Entry(frame_cuenta)
entrada_saldo_inicial.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = "w")

tipo_cuenta = tk.StringVar()

radio_ahorro = tk.Radiobutton(
    frame_cuenta,
    text = "Ahorro",
    value = "ahorro",
    variable = tipo_cuenta,
    command = actualizar_tipo_cuenta
)
radio_ahorro.grid(row = 3, column = 0, pady = 5)

radio_corriente = tk.Radiobutton(
    frame_cuenta,
    text = "Corriente",
    value = "corriente",
    variable = tipo_cuenta,
    command = actualizar_tipo_cuenta
)
radio_corriente.grid(row = 3, column = 1, pady = 5)

label_tasa = tk.Label(
    frame_cuenta,
    text = "Tasa de interés"
)
label_tasa.grid(row = 2, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_tasa = tk.Entry(frame_cuenta)
entrada_tasa.grid(row = 2, column = 1, pady = 5, padx = 5)

boton_crear_cuenta = tk.Button(
    frame_cuenta,
    text = "Crear cuenta",
    command = crear_cuenta
)
boton_crear_cuenta.grid(row = 4, columnspan = 2, pady = 5)

mensaje_cuenta = tk.Label(
    frame_cuenta,
    text = ""
)
mensaje_cuenta.grid(row = 5, columnspan = 2, pady = 5)

frame_operaciones = tk.Frame(ventana)
frame_operaciones.pack()

frame_selector_operaciones = tk.Frame(frame_operaciones)
frame_selector_operaciones.pack()

operacion_seleccionada = tk.StringVar()

radio_depositar = tk.Radiobutton(
    frame_selector_operaciones, 
    text = "Depositar", 
    value = "depositar",
    variable = operacion_seleccionada,
    command = actualizar_operacion
)
radio_depositar.grid(row = 0, column = 0)

radio_retirar = tk.Radiobutton(
    frame_selector_operaciones,
    text = "Retirar",
    value = "retirar",
    variable = operacion_seleccionada,
    command= actualizar_operacion
)
radio_retirar.grid(row = 0, column = 1)

radio_transferir = tk.Radiobutton(
    frame_selector_operaciones,
    text = "Transferir",
    value = "transferir",
    variable = operacion_seleccionada,
    command = actualizar_operacion
)
radio_transferir.grid(row = 0, column = 2)

radio_historial = tk.Radiobutton(
    frame_selector_operaciones,
    text = "Historial",
    value = "historial",
    variable = operacion_seleccionada,
    command = actualizar_operacion
)
radio_historial.grid(row = 1,column = 0)

radio_interes = tk.Radiobutton(
    frame_selector_operaciones,
    text = "Generar intereses",
    value = "interes",
    variable = operacion_seleccionada,
    command = actualizar_operacion
)
radio_interes.grid(row = 1, column = 1)

frame_transferencia = tk.Frame(frame_operaciones)
frame_deposito = tk.Frame(frame_operaciones)
frame_retiro = tk.Frame(frame_operaciones)
frame_historial = tk.Frame(frame_operaciones)
frame_interes = tk.Frame(frame_operaciones)

label_cuenta_interes = tk.Label(
    frame_interes,
    text = "Número de cuenta"
)
label_cuenta_interes.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_cuenta_interes = tk.Entry(frame_interes)
entrada_cuenta_interes.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = "w")

boton_interes = tk.Button(
    frame_interes,
    text = "Aplicar interes",
    command = interes
)
boton_interes.grid(row = 1, columnspan = 2, pady = 5)

mensaje_interes = tk.Label(frame_interes)
mensaje_interes.grid(row = 2, columnspan = 2, pady = 5)

label_cuenta_historial = tk.Label(
    frame_historial,
    text = "Número de cuenta"
)
label_cuenta_historial.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_cuenta_historial = tk.Entry(frame_historial)
entrada_cuenta_historial.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = "w")

texto_historial = tk.Text(
    frame_historial,
    width = 50,
    height = 10
)
texto_historial.grid(row = 1, columnspan = 2, pady= 5)

boton_historial = tk.Button(
    frame_historial,
    text = "Historial",
    command = historial
)
boton_historial.grid(row = 2, columnspan = 2, pady =5 )

label_cuenta_origen = tk.Label(
    frame_transferencia,
    text = "Cuenta de origen"
)
label_cuenta_origen.grid(row = 0, column = 0, pady= 5, padx = 5, sticky = "w")

entrada_cuenta_origen = tk.Entry(frame_transferencia)
entrada_cuenta_origen.grid(row = 0, column = 1, pady = 5, padx = 5, sticky="w")

label_cuenta_destino = tk.Label(
    frame_transferencia,
    text = "Cuenta de destino"
)
label_cuenta_destino.grid(row = 1, column =0, pady = 5, padx = 5, sticky = "w")

entrada_cuenta_destino = tk.Entry(frame_transferencia)
entrada_cuenta_destino.grid(row = 1, column = 1, pady = 5, padx = 5, sticky="w")

label_cantidad_transferencia = tk.Label(
    frame_transferencia,
    text = "Cantidad a transferir"
)
label_cantidad_transferencia.grid(row = 2, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_cantidad_transferencia =tk.Entry(frame_transferencia)
entrada_cantidad_transferencia.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = "w")

boton_transferir = tk.Button(
    frame_transferencia,
    text = "Transferir",
    command = transferir
)
boton_transferir.grid(row = 3, columnspan= 2, pady = 5)

mensaje_transferir = tk.Label(frame_transferencia)
mensaje_transferir.grid(row = 4, columnspan = 2, pady= 5)

label_numero_retiro = tk.Label(
    frame_retiro,
    text = "Número de cuenta"
)
label_numero_retiro.grid(row = 0, column =0 , pady = 5, padx = 5, sticky = "w")

entrada_numero_retiro= tk.Entry(frame_retiro)
entrada_numero_retiro.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = "w")

label_cantidad_retiro = tk.Label(
    frame_retiro,
    text = "Cantidad a retirar"
)
label_cantidad_retiro.grid(row = 1, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_cantidad_retiro = tk.Entry(frame_retiro)
entrada_cantidad_retiro.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = "w")

boton_retirar = tk.Button(
    frame_retiro,
    text = "Retirar",
    command = retirar
)
boton_retirar.grid(row = 2, columnspan = 2, pady = 5)

mensaje_retiro = tk.Label (frame_retiro)
mensaje_retiro.grid(row = 3, columnspan = 2, pady = 5)

label_numero_cuenta = tk.Label(
    frame_deposito,
    text = "Número de cuenta"
)
label_numero_cuenta.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_numero_cuenta = tk.Entry(frame_deposito)
entrada_numero_cuenta.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = "w")

label_cantidad = tk.Label(
    frame_deposito,
    text = "Cantidad a depositar"
)
label_cantidad.grid(row = 1, column = 0, pady = 5, padx = 5, sticky = "w")

entrada_cantidad = tk.Entry(frame_deposito)
entrada_cantidad.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = "w")

boton_depositar = tk.Button(
    frame_deposito,
    text = "Depositar",
    command = depositar
)
boton_depositar.grid(row = 2, columnspan = 2, pady = 5)

mensaje = tk.Label(
    frame_deposito,
    text = ""
)
mensaje.grid(row = 3, columnspan = 2, pady = 5)

ventana.mainloop()