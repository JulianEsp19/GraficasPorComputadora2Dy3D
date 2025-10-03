import pygame
from pygame import SurfaceType

from primerParcial.Figuras.Circulo import Circulo
from primerParcial.Figuras.Estrella import Estrella
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.animacion.Personajes.Movimiento import Movimiento


class Sol(Movimiento):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__objetos = []
        self.__superficieAux = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.__iniciarObjetos()

    def __iniciarObjetos(self):
        rayo1 = Estrella()
        rayo1.setCoordenadas(100 , 100 , 55)
        rayo1.setColor((253, 254, 196))
        rayo1.setRelleno(True)
        self.__objetos.append(rayo1)

        rayo2 = Estrella()
        rayo2.setCoordenadas(100 , 100 , 50)
        rayo2.calcularPuntos()
        rayo2.rotacion(40)
        rayo2.setColor((253, 254, 196))
        rayo2.setRelleno(True)
        self.__objetos.append(rayo2)

        centro = Circulo()
        centro.setResolucion(50)
        centro.setCoordenadas(100 , 100 , 20)
        centro.setColor((237, 241, 0))
        centro.setRelleno(True)
        self.__objetos.append(centro)

        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def cambiarColor(self):

        self.__superficieAux.fill((0,0,0,0))

        self.__objetos = []

        rayo1 = Estrella()
        rayo1.setCoordenadas(100, 100, 55)
        rayo1.setColor((232, 68, 68))
        rayo1.setRelleno(True)
        self.__objetos.append(rayo1)

        rayo2 = Estrella()
        rayo2.setCoordenadas(100, 100, 50)
        rayo2.calcularPuntos()
        rayo2.rotacion(40)
        rayo2.setColor((232, 68, 68))
        rayo2.setRelleno(True)
        self.__objetos.append(rayo2)

        centro = Circulo()
        centro.setResolucion(50)
        centro.setCoordenadas(100, 100, 20)
        centro.setColor((236, 11, 11))
        centro.setRelleno(True)
        self.__objetos.append(centro)

        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def regresarColor(self):

        self.__superficieAux.fill((0, 0, 0, 0))

        self.__objetos = []
        self.__iniciarObjetos()



    def dibujar(self, display: SurfaceType):
        self._verificarMovimiento()
        display.blit(self.__superficieAux, (self._x, self._y))