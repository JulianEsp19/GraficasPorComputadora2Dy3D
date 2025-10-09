import os

import pygame
from pygame import SurfaceType
from primerParcial.Colores import Colores as cl

class Lienzo():
    def __init__(self, display: SurfaceType):
        self.__display = display
        self.__objetos = []
        self.__color = cl.BLANCO
        #self.__imagen = pygame.image.load('primerParcial/Lienzo/Patio_delantero_de_dia.webp')
        #self.__imagen = pygame.transform.scale(self.__imagen, (1100, 700))
        #self.__imagen.convert_alpha()

    def add(self, objeto):
        self.__objetos.append(objeto)

    def setColor(self, color):
        self.__color = color

    def delete(self, objeto):
        self.__objetos.remove(objeto)

    def isExist(self, objeto):
        return self.__objetos.__contains__(objeto)

    def update(self):
        self.__display.fill(self.__color)

        for objeto in self.__objetos:
            objeto.dibujar(self.__display)