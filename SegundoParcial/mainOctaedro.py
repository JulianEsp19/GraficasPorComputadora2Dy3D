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

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)
lienzo.setColor((0,0,0))

octaedro = Octaedro(200, 200, 100, 200)
octaedro.setColor((0,0,0))
lienzo.add(octaedro)

inicio = True

def moverCubo():
    # Ajustes
    esperar = 0.01  # tiempo de sleep por paso (ajusta la suavidad/velocidad)
    steps_half = 90  # número de pasos para la mitad del ciclo (fade-out o fade-in)
    # Duración total de una transición = 2 * steps_half * esperar

    # Colores base (RGB)
    colores = [
        (255, 0, 0),  # rojo
        (0, 255, 0),  # verde
        (255, 220, 100),  # dorado
        (255, 255, 255)  # blanco
    ]

    def mezcla(color_a, color_b, a_factor, b_factor):
        """Devuelve la mezcla ponderada (enteros 0-255)."""
        r = int(color_a[0] * a_factor + color_b[0] * b_factor)
        g = int(color_a[1] * a_factor + color_b[1] * b_factor)
        b = int(color_a[2] * a_factor + color_b[2] * b_factor)
        return (r, g, b)

    while True:
        for i in range(len(colores)):
            actual = colores[i]
            siguiente = colores[(i + 1) % len(colores)]

            # Primera mitad: FADE OUT del color actual (1 -> 0)
            for paso in range(steps_half):
                # factor de 1.0 a 0.0
                f_actual = 1.0 - (paso / (steps_half - 1))
                f_siguiente = 0.0
                color = mezcla(actual, siguiente, f_actual, f_siguiente)

                # respiración: pequeño movimiento vertical y giro ligero usando seno para fluidez
                fase = (paso / steps_half) * math.pi  # 0..pi
                desplaz_x = math.sin(fase) * 0.12  # movimiento leve lateral
                octaedro.setRelleno(True, color)
                octaedro.rotacion(Ejes.Y, 1)
                octaedro.rotacion(Ejes.Z, 0.6)
                octaedro.traslacion(desplaz_x, 5, 5)
                sleep(esperar)

            # Segunda mitad: FADE IN del color siguiente (0 -> 1)
            for paso in range(steps_half):
                # factor de 0.0 a 1.0
                f_actual = 0.0
                f_siguiente = (paso / (steps_half - 1))
                color = mezcla(actual, siguiente, f_actual, f_siguiente)

                # misma "respiración" suave pero invertida en fase para continuidad
                fase = (paso / steps_half) * math.pi  # 0..pi
                desplaz_x = math.sin(fase) * 0.12
                octaedro.setRelleno(True, color)
                octaedro.rotacion(Ejes.Y, 1)
                octaedro.rotacion(Ejes.Z, 0.6)
                octaedro.traslacion(desplaz_x, -5, -5)
                sleep(esperar)

            # pequeño remate entre transiciones (opcional, suave)
            for k in range(8):
                octaedro.rotacion(Ejes.Y, 1)
                sleep(esperar)



threading.Thread(target=moverCubo).start()

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()