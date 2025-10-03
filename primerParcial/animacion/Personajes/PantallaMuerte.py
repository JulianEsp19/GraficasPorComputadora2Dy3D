import pygame
from pygame import SurfaceType

from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.animacion.Personajes.Girasol import Girasol
from primerParcial.animacion.Personajes.LanzaGuisantes import LanzaGuisantes
from primerParcial.animacion.Personajes.Movimiento import Movimiento
from primerParcial.animacion.Personajes.Sol import Sol
from primerParcial.animacion.Personajes.Zombie import Zombie
from primerParcial.animacion.Personajes.ZombieCasco import ZombieCasco
from primerParcial.animacion.Personajes.ZombieCono import ZombieCono


class PantallaMuerte(Movimiento):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__objetos = []
        self.__superficieAux = pygame.Surface((1400, 800), pygame.SRCALPHA)
        self.__iniciarObjetos()

    def __iniciarObjetos(self):

        cuadrado1 = Cuadrado()
        cuadrado1.setCoordenadas(0, 0, 1400, 400)
        cuadrado1.setColor((187, 0, 0, 200))
        cuadrado1.setRelleno(True)
        self.__objetos.append(cuadrado1)

        ovalo1 = Ovalo()
        ovalo1.setResolucion(50)
        ovalo1.setCoordenadas(100, 500, 50, 200)
        ovalo1.setColor((187, 0, 0, 200))
        ovalo1.setRelleno(True)
        self.__objetos.append(ovalo1)

        ovalo2 = Ovalo()
        ovalo2.setResolucion(50)
        ovalo2.setCoordenadas(300, 400, 50, 100)
        ovalo2.setColor((187, 0, 0, 200))
        ovalo2.setRelleno(True)
        self.__objetos.append(ovalo2)

        ovalo1 = Ovalo()
        ovalo1.setResolucion(50)
        ovalo1.setCoordenadas(1300, 500, 50, 200)
        ovalo1.setColor((187, 0, 0, 200))
        ovalo1.setRelleno(True)
        self.__objetos.append(ovalo1)

        ovalo1 = Ovalo()
        ovalo1.setResolucion(50)
        ovalo1.setCoordenadas(1100, 400, 50, 100)
        ovalo1.setColor((187, 0, 0, 200))
        ovalo1.setRelleno(True)
        self.__objetos.append(ovalo1)

        ovalo1 = Ovalo()
        ovalo1.setResolucion(50)
        ovalo1.setCoordenadas(500, 500, 50, 300)
        ovalo1.setColor((187, 0, 0, 200))
        ovalo1.setRelleno(True)
        self.__objetos.append(ovalo1)

        ovalo1 = Ovalo()
        ovalo1.setResolucion(50)
        ovalo1.setCoordenadas(700, 300, 50, 300)
        ovalo1.setColor((187, 0, 0, 200))
        ovalo1.setRelleno(True)
        self.__objetos.append(ovalo1)

        ovalo1 = Ovalo()
        ovalo1.setResolucion(50)
        ovalo1.setCoordenadas(900, 400, 50, 300)
        ovalo1.setColor((187, 0, 0, 200))
        ovalo1.setRelleno(True)
        self.__objetos.append(ovalo1)

        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def dibujar(self, display: SurfaceType):
        self._verificarMovimiento()
        display.blit(self.__superficieAux, (self._x, self._y))