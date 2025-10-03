import pygame
from pygame import SurfaceType

from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.animacion.Personajes.Girasol import Girasol
from primerParcial.animacion.Personajes.LanzaGuisantes import LanzaGuisantes
from primerParcial.animacion.Personajes.Sol import Sol


class Hierbas():

    def __init__(self):
        self.__objetos = []
        self.__superficieAux = pygame.Surface((500, 800), pygame.SRCALPHA)
        self.__iniciarObjetos()

    def __iniciarObjetos(self):
        for i in range(7):
            ovaloI = Ovalo()
            ovaloI.setCoordenadas(200, 100 + (i*120), 170, 130)
            ovaloI.setRelleno(True, (73, 127, 30))
            self.__objetos.append(ovaloI)

        
        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def dibujar(self, display: SurfaceType):
        display.blit(self.__superficieAux, (1050, 0))