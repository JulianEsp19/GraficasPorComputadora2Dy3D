import threading
from random import random, randint
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
lienzo.setColor((0,0,0))

reloj = RelojArena(400, 400, 50, 30, 10, 30)
reloj.setColor((255,0,255))

lienzo.add(reloj)

inicio = True

def moverCubo():
    esperar = 0.01
    while True:
        while True:
            reloj.setColor((200, 0, 255))
            for i in range(100):
                reloj.traslacion(0, 0, -0.8)
                reloj.rotacion(Ejes.Y, 3)
                reloj.rotacion(Ejes.Z, 1)
                sleep(esperar)

            for i in range(100):
                reloj.traslacion(0, 0, 0.8)
                reloj.rotacion(Ejes.Y, -3)
                reloj.rotacion(Ejes.Z, -1)
                sleep(esperar)

            reloj.setColor((0, 255, 255))
            for i in range(120):
                reloj.traslacion(0.6, -0.5, -0.2)
                reloj.rotacion(Ejes.X, 4)
                reloj.rotacion(Ejes.Y, 2)
                sleep(esperar)
            for i in range(120):
                reloj.traslacion(-0.6, 0.5, 0.2)
                reloj.rotacion(Ejes.X, -4)
                reloj.rotacion(Ejes.Y, -2)
                sleep(esperar)


            reloj.setColor((0, 255, 100))
            for i in range(70):
                reloj.traslacion(1, 0, 0)
                reloj.rotacion(Ejes.Z, 5)
                sleep(esperar)
            for i in range(70):
                reloj.traslacion(-1, 0, 0)
                reloj.rotacion(Ejes.Z, -5)
                sleep(esperar)
            for i in range(50):
                reloj.traslacion(0.5, 0, 0)
                reloj.rotacion(Ejes.Z, 8)
                sleep(esperar)
            for i in range(50):
                reloj.traslacion(-0.5, 0, 0)
                reloj.rotacion(Ejes.Z, -8)
                sleep(esperar)

            reloj.setColor((255, 30, 180))
            for i in range(100):
                reloj.rotacion(Ejes.X, 6)
                reloj.rotacion(Ejes.Y, 4)
                reloj.traslacion(0, 0.3, -0.6)
                sleep(esperar)
            for i in range(100):
                reloj.rotacion(Ejes.X, -6)
                reloj.rotacion(Ejes.Y, -4)
                reloj.traslacion(0, -0.3, 0.6)
                sleep(esperar)


            reloj.setColor((255, 255, 100))
            for i in range(60):
                reloj.escalar(1.01)
                sleep(esperar)
            for i in range(60):
                reloj.escalar(0.99)
                sleep(esperar)


            reloj.setColor((180, 0, 255))
            for i in range(120):
                reloj.traslacion(-0.5, 0.5, 0.2)
                reloj.rotacion(Ejes.Y, 3)
                reloj.rotacion(Ejes.Z, 3)
                sleep(esperar)
            for i in range(120):
                reloj.traslacion(0.5, -0.5, -0.2)
                reloj.rotacion(Ejes.Y, -3)
                reloj.rotacion(Ejes.Z, -3)
                sleep(esperar)

            for i in range(360):
                h = i / 60
                x = int((1 - abs(h % 2 - 1)) * 255)

                if 0 <= h < 1:
                    r, g, b = 255, x, 0
                elif 1 <= h < 2:
                    r, g, b = x, 255, 0
                elif 2 <= h < 3:
                    r, g, b = 0, 255, x
                elif 3 <= h < 4:
                    r, g, b = 0, x, 255
                elif 4 <= h < 5:
                    r, g, b = x, 0, 255
                else:
                    r, g, b = 255, 0, x

                reloj.setColor((r, g, b))
                reloj.rotacion(Ejes.Y, 1)
                sleep(0.01)

            reloj.traslacion(0, 0, 0)


threading.Thread(target=moverCubo).start()

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()