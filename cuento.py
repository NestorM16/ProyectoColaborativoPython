# Módulo para mostrar un cuento.

# Imprime un cuento.
def imprimir_cuento():
    cuento = [
        "El conejo y la tortuga",
        "",
        "Un conejo se burlaba de una tortuga por caminar muy despacio.",
        "La tortuga lo desafió a una carrera y el conejo aceptó con mucha confianza.",
        "Durante la carrera, el conejo decidió descansar porque pensó que ya había ganado.",
        "Mientras tanto, la tortuga siguió caminando sin detenerse.",
        "Al despertar, el conejo corrió muy rápido, pero la tortuga ya había llegado a la meta.",
        "",
        "Moraleja: La constancia y el esfuerzo pueden vencer al exceso de confianza."
    ]

    # Recorre e imprime cada línea del cuento.
    for linea in cuento:
        print(linea)