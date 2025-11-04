import threading
from time import sleep

import pygame

from SegundoParcial.Figuras3D import Ejes
from SegundoParcial.Figuras3D.RelojArena import RelojArena
from primerParcial.Lienzo.Lienzo import Lienzo

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

reloj = RelojArena(300, 500, 50, 30, 10, 25)

lienzo.add(reloj)

inicio = True

def moverCubo():
    esperar = 0.01
    while True:
        for i in range(200):
            reloj.traslacion(1, 0, 0)
            sleep(esperar)
            if i < 180:
                reloj.rotacion(Ejes.Z, 1)
            if not i:
                reloj.escalar(2)
        reloj.setColor((100, 0, 100))
        for i in range(180):
            sleep(esperar)
            reloj.rotacion(Ejes.Y, 1)
        reloj.setColor((0, 0, 150))
        for i in range(400):
            sleep(esperar)
            reloj.traslacion(-1, 0, 0)
            if i < 360:
                reloj.rotacion(Ejes.Z, 1)
            if not i:
                reloj.escalar(.5)
        for i in range(180):
            reloj.rotacion(Ejes.X, 1)
            sleep(esperar)
        reloj.setColor((0, 140, 100))
        for i in range(200):
            sleep(esperar)
            reloj.traslacion(1, 0, 0)
            if i < 180:
                reloj.rotacion(Ejes.Z, 1)

        sleep(esperar)

threading.Thread(target=moverCubo).start()

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()