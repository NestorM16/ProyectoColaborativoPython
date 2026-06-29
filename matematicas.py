def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Bloque principal: se ejecuta al correr el archivo
if __name__ == "__main__":
    print("Suma:", suma(5, 3))
    print("Resta:", resta(10, 4))
    print("Multiplicación:", multiplicacion(7, 2))
    print("División:", division(9, 3))
    print("División por cero:", division(9, 0))
