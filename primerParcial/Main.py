import threading
from time import sleep

import pygame
import Figuras2 as fg
from primerParcial.Lienzo.Lienzo import Lienzo
from primerParcial.Figuras.Pixel import Pixel
from primerParcial.Figuras.Linea import Linea
from primerParcial.Figuras.LineaDDA import LineaDDA
from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.Figuras.Triangulo import Triangulo
from primerParcial.Figuras.Hexagono import Hexagono
from primerParcial.Figuras.Circulo import Circulo
from primerParcial.Colores import Colores as cl

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

dibujador = fg.Figuras(ventana)

lienzo = Lienzo(ventana)

pixel = Pixel()
pixel.setCoordenadas(100, 100)

linea = Linea()
linea.setCoordenadas(100, 100, 200, 200)

lineaDDA = LineaDDA()
lineaDDA.setCoordenadas(120, 100, 220, 200)

cuadrado = Cuadrado()
cuadrado.setCoordenadas(150, 100, 250, 200)

triangulo = Triangulo()
triangulo.setCoordenadas(200, 300, 400, 500)

hexagono = Hexagono()
hexagono.setCoordenadas(400, 400, 500, 500)

circulo = Circulo()
circulo.setCoordenadas(175, 300, 100)

# circulo2 = Circulo()
# circulo2.setCoordenadas(325, 300, 100)
#
# circulo3 = Circulo()
# circulo3.setCoordenadas(475, 300, 100)
#
# circulo4 = Circulo()
# circulo4.setCoordenadas(625, 300, 100)

def movimiento():
    while True:
        for i in range(100, 700):
            circulo.setCoordenadas(i, 300, 100)
            sleep(.01)

        j = 700
        for i in range(600):
            j -= 1
            circulo.setCoordenadas(j, 300, 100)
            sleep(.01)

lienzo.add(circulo)
# lienzo.add(circulo2)
# lienzo.add(circulo3)
# lienzo.add(circulo4)

threading.Thread(target=movimiento).start()

lienzo.add(pixel)
lienzo.add(linea)
lienzo.add(lineaDDA)
lienzo.add(cuadrado)
lienzo.add(triangulo)
lienzo.add(hexagono)

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    lienzo.update()


    # las coordenadas polares presentan un punto en el plano mediante:
    # 1.- r = distancia del origen(radio)
    # 2.- (simbolo angulo) = medido desde el eje x positivo
    # 3.- en lugar de x, y se usa r, teta para convertir de polares a cartesiano
    #
    # x = r  * cos(angulo)
    # y = r * sen(angulo)
    # x2 = x0* r * cos(angulo)
    # y2 =


    pygame.display.update()
pygame.quit()