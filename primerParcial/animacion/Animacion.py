import threading
from time import sleep
import pygame
from primerParcial.Lienzo.Lienzo import Lienzo
from primerParcial.animacion.Personajes.Girasol import Girasol

pygame.init()

alto, ancho = 800, 1400

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

girasol = Girasol(-20,-50)
girasol1 = Girasol(500,400)
girasol2 = Girasol(100,500)

lienzo.add(girasol)
lienzo.add(girasol1)
lienzo.add(girasol2)

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()