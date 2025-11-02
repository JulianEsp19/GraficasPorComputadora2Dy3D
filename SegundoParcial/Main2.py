import threading
from time import sleep

import pygame

from SegundoParcial.Figuras3D import Ejes
from SegundoParcial.Figuras3D.Cubo import Cubo
from primerParcial.Lienzo.Lienzo import Lienzo

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

cubo = Cubo(500, 100, 10, 100)
cubo.setPosicionCamara(400, 0, 500)
cubo.traslacion(0, 100, 0)
lienzo.add(cubo)

inicio = True

def moverCubo():
    while True:
        cubo.rotacion(Ejes.Y, 1)
        cubo.rotacion(Ejes.X, 1)
        sleep(.001)

threading.Thread(target=moverCubo).start()
while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()