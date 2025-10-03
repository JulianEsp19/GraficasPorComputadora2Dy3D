import threading
import time
from time import sleep
import pygame
from primerParcial.Lienzo.Lienzo import Lienzo
from primerParcial.animacion.Personajes.Cursor import Cursor
from primerParcial.animacion.Personajes.Girasol import Girasol
from primerParcial.animacion.Personajes.Guisante import Guisante
from primerParcial.animacion.Personajes.Hierbas import Hierbas
from primerParcial.animacion.Personajes.Horda import Horda
from primerParcial.animacion.Personajes.LanzaGuisantes import LanzaGuisantes
from primerParcial.animacion.Personajes.PantallaMuerte import PantallaMuerte
from primerParcial.animacion.Personajes.Sol import Sol
from primerParcial.animacion.Personajes.TableroSemillas import TableroSemillas
from primerParcial.animacion.Personajes.Zombie import Zombie

pygame.init()

alto, ancho = 800, 1400

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lineas")

lienzo = Lienzo(ventana)

pantallaMuerte = PantallaMuerte(0, -800)

tablero = TableroSemillas()
lienzo.add(tablero)

horda = Horda(1100, 0)
lienzo.add(horda)

cursor = Cursor(500, 400)

sol1 = Sol(400, 0)
sol2 = Sol(-30,-30)

girasol1 = Girasol(105, -40)
girasol2 = Girasol(105, -40)

lanzaGuisantes1 = LanzaGuisantes(235, -40)

guisante1 = Guisante(200, 360)
guisante2 = Guisante(200, 360)
guisante3 = Guisante(200, 360)

zombie1 = Zombie(1050, 200)

lienzo.add(zombie1)



lienzo.add(cursor)

hierba = Hierbas()
lienzo.add(hierba)

lienzo.add(pantallaMuerte)

tiempo = 0
tiempoAux = time.time()
tiempo2 = 0
inicio = True

contador = 0

def lanzarGuisante1(x):
    guisante1.cambiarUbicacion(200, 360)
    guisante1.mover(x, 0)
    if not lienzo.isExist(guisante1):
        lienzo.add(guisante1)
def lanzarGuisante2(x):
    guisante2.cambiarUbicacion(200, 360)
    guisante2.mover(x, 0)
    if not lienzo.isExist(guisante2):
        lienzo.add(guisante2)
def lanzarGuisante3(x):
    guisante3.cambiarUbicacion(200, 360)
    guisante3.mover(x, 0)
    if not lienzo.isExist(guisante3):
        lienzo.add(guisante3)



while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    tiempo += time.time() - tiempoAux
    tiempo2 += time.time() - tiempoAux
    tiempoAux = time.time()

    if tiempo > 1 and contador == 0:
        cursor.mover(-350, - 360)
        contador += 1
    elif tiempo > 1.6 and contador == 1:
        lienzo.add(girasol1)
        girasol1.mover(-100, 200)
        cursor.mover(-100, 200)
        contador += 1
    elif tiempo > 1.9 and contador == 2:
        lienzo.add(sol1)
        sol1.mover(0, 400)
        contador += 1
    elif tiempo > 2.7 and contador == 3 and not cursor.isMoviendo(): #3.5
        lienzo.delete(cursor)
        lienzo.add(cursor)
        cursor.mover(350, 200)
        contador += 1
    elif tiempo > 7 and contador == 4:
        sol1.mover(-400, -420)
        contador += 1
    elif tiempo > 10 and contador == 5:
        zombie1.mover(-100, 0)
        contador += 1
    elif not sol1.isMoviendo() and contador == 6:
        lienzo.delete(sol1)
        contador += 1
    elif tiempo > 11 and contador == 7:
        cursor.mover(-100, -450)
        contador += 1
    elif contador == 8 and not cursor.isMoviendo():
        cursor.mover(-120, 350)
        lienzo.add(lanzaGuisantes1)
        lanzaGuisantes1.mover(-120,350)
        contador += 1
    elif tiempo > 13 and contador == 9:
        zombie1.mover(-26, 0)
        contador += 1
    elif tiempo > 16 and contador == 10:
        zombie1.mover(-26, 0)
        lienzo.add(guisante1)
        guisante1.mover(700, 0)
        contador += 1
    elif tiempo > 17 and contador == 11:
        sol1.cambiarUbicacion(0, 200)
        lienzo.add(sol1)
        sol1.mover(0, -120)
        lienzo.delete(cursor)
        lienzo.add(cursor)
        contador += 1
    elif tiempo > 19 and contador == 12:
        zombie1.mover(-26, 0)
        lienzo.add(guisante2)
        guisante2.mover(690, 0)
        sol1.mover(0, 100)
        contador += 1
    elif tiempo > 20 and contador == 13:
        cursor.mover(-150, -150)
        zombie1.mover(-26, 0)
        contador += 1
    elif tiempo > 22 and contador == 14:
        lienzo.add(guisante3)
        zombie1.mover(-26, 0)
        guisante3.mover(680, 0)
        sol1.mover(-50, -200)
        contador += 1
    elif not sol1.isMoviendo() and contador == 15:
        lienzo.delete(sol1)
        zombie1.mover(-26, 0)
        contador += 1
    elif tiempo > 24.5 and contador == 16:
        zombie1.mover(-26, 0)

        lanzarGuisante1(600)

        sol1.cambiarUbicacion(800, 100)
        lienzo.add(sol1)
        sol1.mover(0, 400)
        print(tiempo)
        contador += 1
    elif tiempo > 27 and contador == 17:
        zombie1.mover(-26, 0)
        lanzarGuisante2(600)
        contador += 1
    elif tiempo > 28 and contador == 18:
        horda.mover(-200, 0)
        cursor.mover(750, 300)
        lienzo.delete(cursor)
        lienzo.add(cursor)
        cursor.acelerar()
        contador+= 1
    elif tiempo > 29 and contador == 19:
        zombie1.mover(-26, 0)
        lanzarGuisante3(590)
        contador += 1
    elif not cursor.isMoviendo() and contador == 20:
        sol1.mover(-800, -600)
        lanzarGuisante1(600)
        contador += 1
    elif not sol1.isMoviendo() and contador == 21:#38
        lienzo.delete(sol1)
        horda.mover(-30, 0)
        contador += 1
    elif not guisante3.isMoviendo() and contador == 22:
        lienzo.delete(zombie1)
        horda.mover(-70, 0)
        cursor.mover(-550, -500)
        lanzarGuisante2(600)
        contador += 1
    elif tiempo > 39 and contador == 23:
        horda.mover(-40, 0)
        contador += 1
    elif not cursor.isMoviendo() and contador == 24:
        lienzo.add(sol2)
        sol2.cambiarColor()
        horda.mover(-40, 0)
        contador += 1
    elif tiempo > 41 and contador == 25:
        sol2.regresarColor()
        horda.mover(-50, 0)
        contador += 1
        lanzarGuisante3(550)
        print(tiempo)
    elif tiempo > 42 and contador == 26:
        sol2.cambiarColor()
        contador += 1
    elif tiempo > 43 and contador== 27:
        sol2.regresarColor()
        horda.mover(-50, 0)
        lanzarGuisante1(500)
        contador += 1
    elif tiempo > 45 and contador == 28:
        horda.mover(-50, 0)
        sol1.cambiarColor()
        contador += 1
    elif tiempo > 46 and contador == 29:
        horda.mover(-50, 0)
        sol1.regresarColor()
        lanzarGuisante2(300)
        contador += 1
    elif tiempo > 47 and contador == 30:
        horda.mover(-50, 0)
        sol1.cambiarColor()
        contador += 1
    elif tiempo > 48 and contador == 31:
        horda.mover(-50, 0)
        cursor.mover(200, 200)
        lanzarGuisante3(300)
        contador += 1
    elif tiempo > 49 and contador == 32:
        horda.mover(-50, 0)
        cursor.mover(100, 0)
        contador += 1
    elif tiempo > 50 and contador == 33:
        horda.mover(-50, 0)
        cursor.mover(-500, 100)
        lanzarGuisante1(250)
        contador += 1
    elif tiempo > 51 and contador == 34:
        horda.mover(-50, 0)
        cursor.mover(500, 0)
        contador += 1
    elif tiempo > 52 and contador == 35:
        horda.mover(-50, 0)
        cursor.mover(-500, -100)
        lanzarGuisante2(150)
        contador += 1
    elif tiempo > 53 and contador == 36:
        horda.mover(-50, 0)
        contador += 1
    elif tiempo > 54 and contador == 37:
        horda.mover(-50, 0)
        lanzarGuisante3(100)
        contador += 1
    elif tiempo > 55 and contador == 38:
        horda.mover(-50, 0)
        lienzo.delete(lanzaGuisantes1)
        contador += 1
    elif tiempo > 57 and contador == 39:
        horda.mover(-50, 0)
        contador += 1
    elif tiempo > 58 and contador == 40:
        horda.mover(-50, 0)
        contador += 1
    elif tiempo > 59 and contador == 41:
        horda.mover(-50, 0)
        lienzo.delete(girasol1)
        contador += 1
    elif tiempo > 61 and contador == 42:
        horda.mover(-50, 0)
        contador+= 1
    elif tiempo > 62 and contador == 43:
        horda.mover(-50, 0)
        contador = 42
        tiempo = 60

    if tiempo2 > 80 and tiempo2 < 81:
        if not pantallaMuerte.isMoviendo():
            pantallaMuerte.mover(0, 800)



    if not guisante1.isMoviendo() and lienzo.isExist(guisante1):
        lienzo.delete(guisante1)
    if not guisante2.isMoviendo() and lienzo.isExist(guisante2):
        lienzo.delete(guisante2)
    if not guisante3.isMoviendo() and lienzo.isExist(guisante3):
        lienzo.delete(guisante3)



    lienzo.update()

    pygame.display.update()
pygame.quit()