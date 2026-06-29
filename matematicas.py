# Módulo con operaciones matemáticas básicas.

# Realiza una suma.
def suma(a, b):
    return a + b

# Realiza una resta.
def resta(a, b):
    return a - b

# Realiza una multiplicación.
def multiplicacion(a, b):
    return a * b

# Realiza una división.
def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

# Calcula una potencia.
def potencia(a, b):
    return a ** b

# Calcula el residuo de una división.
def modulo(a, b):
    return a % b
