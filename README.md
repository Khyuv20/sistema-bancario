# 🏦 Sistema Bancario en Python

Sistema bancario desarrollado en **Python** como proyecto de aprendizaje para practicar y aplicar conceptos de programación, Programación Orientada a Objetos (POO), manejo de errores, modularización, Git e interfaces gráficas con Tkinter.

El proyecto comenzó como un sistema bancario sencillo ejecutado desde la terminal y fue evolucionando progresivamente hasta contar con una **interfaz gráfica completa**.

La versión final del proyecto es **Banco 5.0**.

---

## ✨ Características

El sistema permite:

- Crear clientes.
- Crear cuentas bancarias asociadas a clientes.
- Crear cuentas de ahorro.
- Crear cuentas corrientes.
- Consultar saldos.
- Realizar depósitos.
- Realizar retiros.
- Realizar transferencias entre cuentas.
- Consultar el historial de movimientos.
- Aplicar intereses a cuentas de ahorro.
- Validar datos y operaciones incorrectas.
- Manejar errores sin cerrar el programa.
- Utilizar el sistema mediante una interfaz gráfica desarrollada con Tkinter.

---

## 🏦 Tipos de cuenta

### Cuenta de ahorro

Las cuentas de ahorro incluyen una tasa de interés.

El sistema permite aplicar el interés correspondiente sobre el saldo de la cuenta.

### Cuenta corriente

Las cuentas corrientes cuentan con características propias como:

- Comisión por retiro.
- Límite de sobregiro.

---

## 💸 Operaciones bancarias

### Depósitos

Permite depositar dinero utilizando el número de cuenta.

El sistema valida que la cantidad ingresada sea válida.

### Retiros

Permite retirar dinero de una cuenta.

Se realizan validaciones para evitar operaciones inválidas o retiros que no estén permitidos según las reglas de la cuenta.

### Transferencias

Permite transferir dinero entre dos cuentas utilizando:

- Número de cuenta de origen.
- Número de cuenta de destino.
- Cantidad a transferir.

El sistema valida, entre otras cosas:

- Que ambas cuentas existan.
- Que la cantidad sea válida.
- Que la cuenta de origen y destino no sean la misma.
- Que la operación pueda realizarse correctamente.

Las transferencias también quedan registradas en el historial de ambas cuentas.

### Historial

Cada cuenta mantiene un historial de sus movimientos.

Puede incluir operaciones como:

- Depósitos.
- Retiros.
- Transferencias enviadas.
- Transferencias recibidas.
- Intereses aplicados.

El historial puede consultarse desde la interfaz gráfica utilizando el número de cuenta.

---

## 🖥️ Interfaz gráfica

Banco 5.0 incorpora una interfaz gráfica desarrollada con **Tkinter**.

La interfaz permite realizar las principales operaciones del sistema sin utilizar directamente la terminal.

Las operaciones disponibles incluyen:

- Crear cliente.
- Crear cuenta.
- Depositar.
- Retirar.
- Transferir.
- Consultar historial.
- Aplicar intereses.

La interfaz utiliza distintos widgets de Tkinter, entre ellos:

- `Frame`
- `Label`
- `Entry`
- `Button`
- `Radiobutton`
- `StringVar`
- `Text`

También se utilizan los gestores de geometría:

- `pack()`
- `grid()`

Los diferentes formularios de operaciones se muestran u ocultan dependiendo de la opción seleccionada por el usuario.

---

## 🧠 Conceptos aplicados

Durante el desarrollo del proyecto se utilizaron conceptos como:

### Python

- Variables
- Condicionales
- Bucles
- Funciones
- Listas
- Manejo de excepciones
- Módulos
- Imports

### Programación Orientada a Objetos

- Clases
- Objetos
- Atributos
- Métodos
- Encapsulamiento
- Herencia
- Composición
- Métodos protegidos
- Representación de objetos con `__str__`

### Manejo de errores

Se utiliza `try / except` y excepciones como `ValueError` para controlar situaciones como:

- Datos numéricos inválidos.
- Cantidades incorrectas.
- Clientes inexistentes.
- Cuentas inexistentes.
- Clientes duplicados.
- Operaciones bancarias no permitidas.

### Interfaces gráficas

Se utilizó Tkinter para aprender conceptos como:

- Creación de ventanas.
- Organización mediante Frames.
- Entrada de datos.
- Botones y eventos.
- Radiobuttons.
- Variables de Tkinter.
- Mostrar y ocultar elementos.
- Distribución mediante `pack()` y `grid()`.
- Visualización de contenido multilínea mediante `Text`.

## 📁 Estructura del proyecto

```text
Cuenta Bancaria/
│
├── banco.py
├── cuentas.py
├── gui.py
└── main.py
```

### `cuentas.py`

Contiene las clases relacionadas con las cuentas bancarias:

- `Cuenta`
- `CuentaAhorro`
- `CuentaCorriente`

Aquí se encuentra gran parte de la lógica relacionada con:

- Saldo.
- Depósitos.
- Retiros.
- Intereses.
- Historial.
- Comisiones.
- Sobregiro.

### `banco.py`

Contiene la lógica relacionada con el banco y los clientes.

Incluye clases como:

- `Banco`
- `Cliente`

Se encarga de operaciones como:

- Gestionar clientes.
- Buscar clientes.
- Buscar cuentas.
- Realizar operaciones utilizando números de cuenta.
- Transferencias.
- Consulta de historial.
- Aplicación de intereses.

### `main.py`

Contiene la versión del sistema utilizada desde la terminal.

### `gui.py`

Contiene la interfaz gráfica de **Banco 5.0**, desarrollada con Tkinter.

---

## 🚀 Ejecución

Para ejecutar la interfaz gráfica:

```bash
python gui.py
```

Dependiendo de la instalación de Python, también puede utilizarse:

```bash
python3 gui.py
```

Para ejecutar la versión de terminal:

```bash
python main.py
```

o:

```bash
python3 main.py
```

---

## 📈 Evolución del proyecto

El sistema fue desarrollado de manera incremental.

### Banco 1.x

Primera implementación de una cuenta bancaria.

Se introdujeron conceptos básicos como:

- Clase `Cuenta`.
- Titular.
- Saldo.
- Depósitos.
- Retiros.

### Banco 2.0

El proyecto comenzó a incorporar más conceptos de Programación Orientada a Objetos.

Se añadieron distintos tipos de cuenta y se trabajó con herencia.

### Banco 3.0

Se incorporaron conceptos como:

- Clientes.
- Banco.
- Múltiples cuentas.
- Búsqueda mediante número de cuenta.
- Gestión centralizada de operaciones.

### Banco 4.0

Se amplió considerablemente la lógica del sistema.

Se añadieron:

- Transferencias.
- Historial de movimientos.
- Más validaciones.
- Manejo de errores.
- Separación del proyecto en diferentes archivos.
- Uso de módulos e imports.

### Banco 5.0

Se desarrolló una interfaz gráfica utilizando **Tkinter**.

La lógica bancaria desarrollada anteriormente fue reutilizada desde la GUI, manteniendo separadas la lógica del sistema y la interfaz.

Banco 5.0 representa la versión final de este proyecto.

---

## 🎯 Objetivo del proyecto

El objetivo principal de este proyecto no es representar un sistema bancario real listo para producción.

Fue desarrollado como proyecto práctico para aprender programación progresivamente y aplicar los conceptos aprendidos en un sistema cada vez más completo.

El desarrollo permitió pasar de ejercicios individuales a trabajar con un programa compuesto por múltiples clases, archivos y responsabilidades.

---

## ⚠️ Limitaciones

Esta aplicación es un proyecto educativo.

Actualmente:

- Los datos se almacenan en memoria.
- Los datos se pierden al cerrar el programa.
- No utiliza una base de datos.
- No implementa autenticación real.
- No utiliza cifrado ni mecanismos de seguridad propios de un sistema bancario real.
- No está diseñado para manejar dinero real.

Una posible evolución futura sería implementar persistencia mediante una base de datos.

---

## 🔮 Posible continuación

Aunque Banco 5.0 representa el cierre del proyecto actual, una posible versión futura podría incorporar:

- SQLite.
- SQL.
- Persistencia de clientes.
- Persistencia de cuentas.
- Persistencia del historial de movimientos.

Esto permitiría conservar la información incluso después de cerrar la aplicación.

---

