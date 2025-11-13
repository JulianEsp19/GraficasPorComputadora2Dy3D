import math
import threading
from random import random, randint
from time import sleep

import pygame

from SegundoParcial.Figuras3D import Ejes
from SegundoParcial.Figuras3D.Octaedro import Octaedro
from SegundoParcial.Figuras3D.RelojArena import RelojArena
from primerParcial.Lienzo.Lienzo import Lienzo

pygame.init()

alto, ancho = 1000, 1000

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)
lienzo.setColor((0,0,0))

def blend(color_a, color_b, t):
    return (
        int(color_a[0] * (1 - t) + color_b[0] * t),
        int(color_a[1] * (1 - t) + color_b[1] * t),
        int(color_a[2] * (1 - t) + color_b[2] * t),
    )

# --- Colores secundarios (figura interna) ---
color_sec_por_tipo = {
    1: (200, 30, 30),    # caja regalo (rojo)
    3: (255, 215, 0),    # estrella (dorado)
    4: (150, 30, 200),   # caja regalo 2 (morado)
    5: (220, 240, 255),  # copo de nieve (azulado)
    6: (230, 60, 140),   # dulce (rosa)
}

# --- Paleta de colores pastel para las figuras externas (octaedros) ---
paleta_cycle = [
    (255, 179, 186),  # rosa pastel
    (255, 223, 186),  # durazno claro
    (255, 255, 186),  # amarillo claro
    (186, 255, 201),  # verde menta
    (186, 225, 255),  # celeste claro
    (218, 186, 255),  # lavanda
]

# --- Crear varios octaedros ---
octaedros = []

rows = 3
cols = 3
width, height = 800, 800
margin = 60
size = 160

usable_w = width - 2 * margin
usable_h = height - 2 * margin
spacing_x = usable_w / (cols - 1) if cols > 1 else 0
spacing_y = usable_h / (rows - 1) if rows > 1 else 0

# Ciclo de tipos (sin el árbol navideño, tipo 2)
tipo_seq = [1, 3, 4, 5, 6]
k = 0

for r in range(rows):
    for c in range(cols):
        px = int(margin + c * spacing_x)
        py = int(margin + r * spacing_y)
        pz = 100

        tipo = tipo_seq[k % len(tipo_seq)]
        k += 1

        # Crear el octaedro
        octa = Octaedro(px, py, pz, size, tipo)

        # Color secundario según tipo (figura interna)
        sec_color = color_sec_por_tipo.get(tipo, (255, 255, 0))
        octa.setColorSecundario(sec_color)

        # Color principal inicial (pastel)
        octa.setColor(paleta_cycle[0])

        # Rotación inicial en X para apreciarse mejor
        octa.rotacion(Ejes.X, 70)

        lienzo.add(octa)

        # Cada uno tiene una fase distinta en la animación
        fase = (r * cols + c) * (2 * math.pi / (rows * cols))
        octaedros.append({"obj": octa, "fase": fase, "tipo": tipo})

# --- Animación: rotación suave y cambio de color principal pastel ---
def moverCubo():
    fps_sleep = 1 / 60.0
    rotation_speed = 0.6
    color_speed = 0.8
    t = 0.0
    n_pal = len(paleta_cycle)

    while True:
        t += color_speed * fps_sleep

        for info in octaedros:
            octa = info["obj"]
            fase = info["fase"]

            # rotación suave en Y
            octa.rotacion(Ejes.Y, rotation_speed)

            # interpolación circular entre colores pastel
            u = (t + fase) % (2 * math.pi)
            pos = (u / (2 * math.pi)) * n_pal
            idx = int(math.floor(pos)) % n_pal
            next_idx = (idx + 1) % n_pal
            frac = pos - math.floor(pos)

            color_a = paleta_cycle[idx]
            color_b = paleta_cycle[next_idx]
            color_main = blend(color_a, color_b, frac)

            # actualizar color principal
            octa.setColor(color_main)

        sleep(fps_sleep)

# Hilo de animación
threading.Thread(target=moverCubo, daemon=True).start()

# --- Bucle principal ---
inicio = True
while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    lienzo.update()
    pygame.display.update()

pygame.quit()