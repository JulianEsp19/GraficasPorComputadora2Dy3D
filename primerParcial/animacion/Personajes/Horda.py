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


class Horda(Movimiento):

    def __init__(self, x, y):
        super().__init__(x , y)
        self.__objetos = []
        self.__superficieAux = pygame.Surface((1100, 800), pygame.SRCALPHA)
        self.__iniciarObjetos()

    def __iniciarObjetos(self):
        for i in range(8):
            zombie = Zombie(100, 100)
            if not i % 4:
                zombie = ZombieCasco(200 + (i * 100), 100)
            elif not i % 3:
                zombie = ZombieCono(200 + (i * 100), 100)
            elif not i % 2:
                zombie = Zombie(200 + (i * 100), 100)
            self.__objetos.append(zombie)

        for i in range(8):
            zombie = Zombie(50, 250)
            if not i % 4:
                zombie = ZombieCono(150 + (i * 100), 250)
            elif not i % 3:
                zombie = Zombie(150 + (i * 100), 250)
            elif not i % 2:
                zombie = ZombieCasco(150 + (i * 100), 250)
            self.__objetos.append(zombie)
            
        for i in range(8):
            zombie = Zombie(150, 400)
            if not i % 4:
                zombie = ZombieCono(250 + (i * 100), 400)
            elif not i % 3:
                zombie = ZombieCasco(250 + (i * 100), 400)
            elif not i % 2:
                zombie = Zombie(250 + (i * 100), 400)
            self.__objetos.append(zombie)


        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def dibujar(self, display: SurfaceType):
        self._verificarMovimiento()
        display.blit(self.__superficieAux, (self._x, self._y))