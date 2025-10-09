import threading
from time import sleep

import pygame

from primerParcial.Curvas.Curva1 import Curva1
from primerParcial.Lienzo.Lienzo import Lienzo

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

curva1 = Curva1(8)
curva1.calcularPuntos()
curva1.escalar(100)
curva1.traslacion(200, 100)
lienzo.add(curva1)

curva2 = Curva1(100)
curva2.calcularPuntos()
curva2.escalar(100)
curva2.traslacion(200, 400)
lienzo.add(curva2)


inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()