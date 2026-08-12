# Sistema Bancario en Python

Sistema bancario desarrollado en Python como proyecto de aprendizaje para practicar programación orientada a objetos.

Actualmente, el proyecto permite crear clientes y diferentes tipos de cuentas bancarias, realizar operaciones sobre ellas y controlar distintos errores mediante excepciones.

## Funcionalidades

- Crear cuentas de ahorro y cuentas corrientes.
- Depositar y retirar dinero en ambos tipos de cuenta.
- Consultar el saldo mediante el número de cuenta.
- Las cuentas de ahorro permiten aplicar intereses al saldo.
- Las cuentas corrientes cobran una comisión al realizar retiros.
- Las cuentas corrientes permiten sobregiro hasta un límite establecido.
- Registrar clientes mediante un identificador.
- Asociar múltiples cuentas a un mismo cliente.
- Buscar y gestionar cuentas mediante su número de cuenta.
- Validar operaciones incorrectas, como depósitos negativos, retiros inválidos o cuentas inexistentes.

## Conceptos utilizados

Durante el desarrollo de este proyecto se utilizaron diferentes conceptos de Python y programación orientada a objetos:

- Programación orientada a objetos (POO).
- Clases y objetos.
- Herencia.
- Sobrescritura de métodos.
- Encapsulamiento.
- Métodos públicos y protegidos.
- Atributos privados.
- Manejo de excepciones con `try`, `except` y `raise`.
- Uso de `super()`.
- Uso de `isinstance()`.
- Listas para almacenar clientes y cuentas.

## Estructura principal

El sistema está compuesto por las siguientes clases:

### `Cuenta`

Clase base que contiene el comportamiento común de las cuentas bancarias, como consultar saldo, depositar y retirar dinero.

### `CuentaAhorro`

Hereda de `Cuenta` y añade una tasa de interés que puede aplicarse al saldo.

### `CuentaCorriente`

Hereda de `Cuenta` y sobrescribe el método de retiro para añadir una comisión y permitir un límite de sobregiro.

### `Cliente`

Representa a un cliente del banco mediante un identificador y permite asociarle múltiples cuentas.

### `Banco`

Gestiona los clientes y permite buscar cuentas, realizar depósitos, retiros, consultar saldos y aplicar intereses.

## Cómo ejecutar el programa

1. Tener Python instalado.
2. Descargar o clonar este repositorio.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python3 "Cuenta Bancaria/sistema_bancario.py"
```

En algunos sistemas también se puede utilizar:

```bash
python "Cuenta Bancaria/sistema_bancario.py"
```

## Versión

Versión actual:

`v3.0`

Esta versión incluye la gestión de clientes, múltiples cuentas, cuentas de ahorro, cuentas corrientes, operaciones bancarias y validación de errores.

## Próxima versión

Para la versión `v4.0` se planea continuar mejorando la estructura del programa y añadir nuevas funcionalidades.
