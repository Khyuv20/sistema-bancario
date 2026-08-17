# Sistema Bancario en Python

Sistema bancario desarrollado en Python como proyecto de aprendizaje para practicar programación orientada a objetos, validación de datos, manejo de excepciones, modularización y organización de proyectos.

Actualmente, el sistema permite gestionar clientes y diferentes tipos de cuentas bancarias, realizar operaciones entre ellas, consultar historiales de movimientos y controlar operaciones incorrectas mediante excepciones.

## Funcionalidades

- Crear cuentas de ahorro y cuentas corrientes.
- Generar números de cuenta automáticamente.
- Registrar clientes mediante un identificador.
- Asociar múltiples cuentas a un mismo cliente.
- Buscar clientes mediante su identificador.
- Buscar y gestionar cuentas mediante su número de cuenta.
- Consultar el saldo de una cuenta.
- Depositar dinero.
- Retirar dinero.
- Realizar transferencias entre cuentas.
- Consultar el historial de movimientos de una cuenta.
- Aplicar intereses a cuentas de ahorro.
- Cobrar comisión al retirar dinero de cuentas corrientes.
- Permitir sobregiro en cuentas corrientes hasta un límite establecido.
- Utilizar un menú interactivo desde la terminal.

## Transferencias

El sistema permite realizar transferencias entre dos cuentas registradas en el banco.

Antes de realizar una transferencia se valida que:

- La cuenta de origen exista.
- La cuenta de destino exista.
- La cantidad sea mayor que cero.
- La cuenta de origen y destino sean diferentes.
- La cuenta de origen pueda realizar el retiro.

Si la transferencia no puede completarse después de retirar el dinero de la cuenta de origen, el sistema devuelve el dinero descontado para evitar dejar la operación incompleta.

## Historial de movimientos

Cada cuenta mantiene un historial de sus operaciones.

Actualmente pueden registrarse movimientos como:

- Depósitos.
- Retiros.
- Transferencias enviadas.
- Transferencias recibidas.

En las cuentas corrientes, los retiros también pueden registrar información sobre la comisión y el total descontado.

Las transferencias se registran directamente como transferencias para evitar mostrar movimientos duplicados como retiro y depósito.

## Validaciones

El sistema incluye diferentes validaciones para evitar estados y operaciones incorrectas.

Entre ellas:

- El saldo inicial no puede ser negativo.
- Los depósitos deben ser mayores que cero.
- Los retiros deben ser mayores que cero.
- No se puede retirar más dinero del permitido.
- Las cuentas corrientes respetan su límite de sobregiro.
- La comisión de una cuenta corriente no puede ser negativa.
- El límite de sobregiro no puede ser negativo.
- La tasa de interés no puede ser negativa.
- El titular de una cuenta debe ser texto y no puede estar vacío.
- El identificador de un cliente debe ser un número entero mayor que cero.
- El nombre de un cliente no puede estar vacío.
- No pueden existir dos clientes con el mismo identificador.
- Una misma cuenta no puede registrarse varias veces.
- No se puede transferir dinero a la misma cuenta.
- Las operaciones sobre cuentas inexistentes generan un error controlado.

## Estructura del proyecto

A partir de la versión 4.0, el proyecto está dividido en diferentes módulos para separar responsabilidades y facilitar su mantenimiento.

```text
Cuenta Bancaria/
├── main.py
├── banco.py
└── cuentas.py
```

### `cuentas.py`

Contiene las clases relacionadas con los diferentes tipos de cuenta.

#### `Cuenta`

Clase base que contiene el comportamiento común de las cuentas bancarias.

Entre sus responsabilidades se encuentran:

- Administrar el saldo.
- Generar números de cuenta.
- Realizar depósitos.
- Realizar retiros.
- Mantener el historial de movimientos.

#### `CuentaAhorro`

Hereda de `Cuenta` y añade una tasa de interés que puede aplicarse al saldo.

#### `CuentaCorriente`

Hereda de `Cuenta` y modifica el comportamiento de los retiros para:

- Cobrar una comisión.
- Permitir sobregiro hasta un límite establecido.

### `banco.py`

Contiene las clases relacionadas con la administración del banco.

#### `Cliente`

Representa a un cliente mediante un identificador y un nombre.

Cada cliente puede tener múltiples cuentas asociadas.

#### `Banco`

Gestiona los clientes y las cuentas del sistema.

Entre sus responsabilidades se encuentran:

- Registrar clientes.
- Buscar clientes.
- Asociar cuentas.
- Buscar cuentas.
- Consultar saldos.
- Realizar depósitos.
- Realizar retiros.
- Aplicar intereses.
- Realizar transferencias.
- Consultar historiales.

### `main.py`

Es el punto de entrada del programa.

Contiene el menú interactivo desde el cual el usuario puede utilizar las diferentes funcionalidades del sistema.

El programa se inicia mediante:

```python
if __name__ == "__main__":
    main()
```

Esto permite separar la ejecución principal de los módulos que contienen la lógica del sistema.

## Conceptos utilizados

Durante el desarrollo del proyecto se han aplicado conceptos de Python como:

- Variables y tipos de datos.
- Condicionales.
- Bucles.
- Funciones.
- Listas.
- Manejo de excepciones con `try`, `except` y `raise`.
- Programación orientada a objetos.
- Clases y objetos.
- Encapsulamiento.
- Atributos privados y protegidos.
- Herencia.
- Sobrescritura de métodos.
- Uso de `super()`.
- Uso de `isinstance()`.
- Métodos especiales como `__init__()` y `__str__()`.
- Módulos.
- Imports.
- Separación de responsabilidades.
- Uso de `if __name__ == "__main__"`.

## Ejecución

Para ejecutar el programa, situarse en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

Después se mostrará el menú bancario en la terminal.

## Versión

Versión actual:

`v4.0`

### Banco 4.0

Esta versión incorpora principalmente:

- Transferencias entre cuentas.
- Historial de movimientos.
- Nuevas validaciones.
- Mejoras en la lógica de las operaciones.
- Prevención de transferencias incompletas.
- Separación del proyecto en múltiples archivos.
- Uso de módulos e imports.
- Nuevo punto de entrada mediante `main.py`.
- Integración de transferencias e historial en el menú.

## Próxima versión

La próxima etapa del proyecto será:

`v5.0`

El objetivo principal de Banco 5.0 será desarrollar una **interfaz gráfica** para dejar de depender exclusivamente de la terminal.

La lógica bancaria desarrollada hasta la versión 4.0 se mantendrá separada de la interfaz, permitiendo reutilizar las clases y módulos existentes sin tener que reescribir el funcionamiento interno del banco.

## Objetivo del proyecto

Este proyecto tiene como objetivo principal aprender Python mediante la construcción progresiva de una aplicación real.

Cada versión amplía el sistema e introduce nuevos conceptos, buscando mejorar tanto las funcionalidades como la estructura y calidad del código.