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
from primerParcial.Figuras.Estrella import Estrella
from primerParcial.Figuras.Pentagono import Pentagono
from primerParcial.Figuras.Octagono import Octagono
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.Colores import Colores as cl

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

pixel = Pixel()
pixel.setCoordenadas(700, 500)

linea = Linea()
linea.setCoordenadas(100, 600, 200, 800)

lineaDDA = LineaDDA()
lineaDDA.setCoordenadas(120, 600, 220, 800)

# 🔹 Círculos
circulo1 = Circulo()
circulo1.setCoordenadas(50, 50, 40)  # sin relleno

circulo2 = Circulo()
circulo2.setRelleno(True)
circulo2.setCoordenadas(150, 50, 40)  # con relleno

# 🔹 Cuadrados
cuadrado1 = Cuadrado()
cuadrado1.setCoordenadas(250, 30, 320, 100)  # sin relleno

cuadrado2 = Cuadrado()
cuadrado2.setRelleno(True)
cuadrado2.setCoordenadas(350, 30, 420, 100)  # con relleno

# 🔹 Estrellas
estrella1 = Estrella()
estrella1.setCoordenadas(500, 50, 50)  # sin relleno

estrella2 = Estrella()
estrella2.setRelleno(True)
estrella2.setCoordenadas(600, 50, 50)  # con relleno

# 🔹 Hexágonos
hexagono1 = Hexagono()
hexagono1.setCoordenadas(50, 150, 120, 220)  # sin relleno

hexagono2 = Hexagono()
hexagono2.setRelleno(True)
hexagono2.setCoordenadas(150, 150, 220, 220)  # con relleno

# 🔹 Octágonos
octagono1 = Octagono()
octagono1.setCoordenadas(250, 550, 50)  # sin relleno

octagono2 = Octagono()
octagono2.setRelleno(True)
octagono2.setCoordenadas(370, 550, 50)  # con relleno

# 🔹 Pentágonos
pentagono1 = Pentagono()
pentagono1.setCoordenadas(500, 150, 50)  # sin relleno

pentagono2 = Pentagono()
pentagono2.setRelleno(True)
pentagono2.setCoordenadas(600, 150,50)  # con relleno

# 🔹 Triángulos
triangulo1 = Triangulo()
triangulo1.setCoordenadas(50, 300, 150, 400)  # sin relleno

triangulo2 = Triangulo()
triangulo2.setRelleno(True)
triangulo2.setCoordenadas(200, 300, 300, 400)  # con relleno

ovalo = Ovalo()
ovalo.setCoordenadas(600, 500, 50, 75)

ovalo2 = Ovalo()
ovalo2.setRelleno(True)
ovalo2.setCoordenadas(720, 500, 50, 75)

lienzo.add(ovalo)
lienzo.add(ovalo2)


# ➡️ Agregarlos al lienzo
lienzo.add(circulo1)
lienzo.add(circulo2)

lienzo.add(cuadrado1)
lienzo.add(cuadrado2)

lienzo.add(estrella1)
lienzo.add(estrella2)

lienzo.add(hexagono1)
lienzo.add(hexagono2)

lienzo.add(octagono1)
lienzo.add(octagono2)

lienzo.add(pentagono1)
lienzo.add(pentagono2)

lienzo.add(triangulo1)
lienzo.add(triangulo2)

lienzo.add(lineaDDA)
lienzo.add(linea)
lienzo.add(pixel)

inicio = True

def cambio():
    while True:
        sleep(.01)
        cuadrado2.escalar(1.000000001)
threading.Thread(target=cambio).start()

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    lienzo.update()

    pygame.display.update()
pygame.quit()