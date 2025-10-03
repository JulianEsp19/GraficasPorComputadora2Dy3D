import pygame
from pygame import SurfaceType

from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.animacion.Personajes.Girasol import Girasol
from primerParcial.animacion.Personajes.LanzaGuisantes import LanzaGuisantes
from primerParcial.animacion.Personajes.Sol import Sol


class TableroSemillas():

    def __init__(self):
        self.__objetos = []
        self.__superficieAux = pygame.Surface((1100, 150))
        self.__iniciarObjetos()

    def __iniciarObjetos(self):


        cuadrado1 = Cuadrado()
        cuadrado1.setColor((150, 72, 23))
        cuadrado1.setCoordenadas(0, 0, 1100, 150)
        cuadrado1.setRelleno(True)
        self.__objetos.append(cuadrado1)

        cuadrado2 = Cuadrado()
        cuadrado2.setColor((106, 50, 18))
        cuadrado2.setCoordenadas(10, 10, 130, 140)
        cuadrado2.setRelleno(True)
        self.__objetos.append(cuadrado2)

        cuadrado3 = Cuadrado()
        cuadrado3.setColor((106, 50, 18))
        cuadrado3.setCoordenadas(140, 10, 1090, 140)
        cuadrado3.setRelleno(True)
        self.__objetos.append(cuadrado3)

        for i in range(7):
            cuadradoI = Cuadrado()
            cuadradoI.setCoordenadas(150 + (i*130), 20, 260 + (i*130), 130)
            if i < 2:
                cuadradoI.setColor((241, 239, 230))
            else:
                cuadradoI.setColor((129, 65, 27))
            cuadradoI.setRelleno(True)
            self.__objetos.append(cuadradoI)

        sol = Sol(-30, -30)
        self.__objetos.append(sol)

        girasol2 = Girasol(105, -40)
        girasol2.setAnimar(False)
        self.__objetos.append(girasol2)

        lanzaGuisantes = LanzaGuisantes(235, -40)
        lanzaGuisantes.setAnimar(False)
        self.__objetos.append(lanzaGuisantes)
        for i in self.__objetos:
            i.dibujar(self.__superficieAux)




    def dibujar(self, display: SurfaceType):
        display.blit(self.__superficieAux, (0, 0))


