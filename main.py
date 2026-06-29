import matematicas
import cuento
import utilidades

print("=== MÓDULO MATEMÁTICAS ===")
print("Suma:", matematicas.suma(7, 3))
print("Resta:", matematicas.resta(7, 3))
print("Multiplicación:", matematicas.multiplicacion(7, 3))
print("División:", matematicas.division(7, 3))
print("Potencia:", matematicas.potencia(7, 3))
print("Residuo:", matematicas.modulo(7, 3))

print("\n=== CUENTO ===")
cuento.imprimir_cuento()

print("\n=== UTILIDADES ===")
texto = "Hola Mundo"
print("Original:", texto)
print("Mayúsculas:", utilidades.convertir_mayusculas(texto))
print("Minúsculas:", utilidades.convertir_minusculas(texto))
print("Caracteres:", utilidades.contar_caracteres(texto))
print("Invertido:", utilidades.invertir_texto(texto))