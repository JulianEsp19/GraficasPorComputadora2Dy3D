import pygame
from pygame import SurfaceType

from primerParcial.Figuras.Circulo import Circulo
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.animacion.Personajes.Movimiento import Movimiento


class Guisante(Movimiento):

    def __init__(self, x , y):
        super().__init__(x, y)
        self.__objetos = []
        self.__superficieAux = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.__iniciarObjetos()

    def __iniciarObjetos(self):
        guisante = Circulo()
        guisante.setResolucion(30)
        guisante.setCoordenadas(50,50, 20)
        guisante.setRelleno(True, (104, 203, 75))
        self.__objetos.append(guisante)

        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def dibujar(self, display: SurfaceType):
        self._verificarMovimiento()
        display.blit(self.__superficieAux, (self._x, self._y))

