import pygame

from SegundoParcial.Curvas.Curva1 import Curva1
from SegundoParcial.Curvas.CurvaTabla import CurvaTabla
from SegundoParcial.Curvas.Flor import Flor
from SegundoParcial.Curvas.Humito import Humito
from SegundoParcial.Curvas.Infinito import Infinito
from SegundoParcial.Curvas.Sol import Sol
from primerParcial.Lienzo.Lienzo import Lienzo

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

curva1 = Curva1(8)
curva1.calcularPuntos()
curva1.traslacion(200, 100)
lienzo.add(curva1)

curva2 = Curva1(100)
curva2.calcularPuntos()
curva2.traslacion(200, 150)
lienzo.add(curva2)

curva3 = Humito(100)
curva3.calcularPuntos()
curva3.traslacion(400, 100)
lienzo.add(curva3)


curvaTabla = CurvaTabla(10)
curvaTabla.calcularPuntos()
curvaTabla.traslacion(150, 300)
lienzo.add(curvaTabla)

infinito = Infinito(50, 150)
infinito.calcularPuntos()
infinito.traslacion(160, 400)
lienzo.add(infinito)

flor = Flor(200)
flor.calcularPuntos()
flor.traslacion(180, 620)
lienzo.add(flor)

sol = Sol(100)
sol.calcularPuntos()
sol.traslacion(550, 350)
lienzo.add(sol)

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False
    lienzo.update()
    pygame.display.update()
pygame.quit()