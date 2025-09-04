import pygame
import Figuras as fg
import Colores as cl

pygame.init()

alto, ancho = 800, 800

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

dibujador = fg.Figuras(ventana)

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    ventana.fill((255,255,255))

    dibujador.cuadrado(cl.AZUL, 70, 70, 200,200)

    dibujador.triangulo(cl.AZUL, 100, 100, 400, 400)

    dibujador.dibujarPixel(cl.AZUL,20, 100)

    dibujador.hexagono(cl.ROJO, 150, 150, 400, 400)

    dibujador.estrella(cl.ROJO, 200, 200, 600, 600)

    dibujador.octagono(cl.ROJO, 600, 600, 100)

    dibujador.hexagonoCirculo(cl.ROJO, 100, 400, 100)
    
    dibujador.estrellaCirculo(cl.ROJO, 100, 600, 100)

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