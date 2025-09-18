from pygame import SurfaceType
from primerParcial.Colores import Colores as cl

class Lienzo():
    def __init__(self, display: SurfaceType):
        self.__display = display
        self.__objetos = []
        self.__color = cl.BLANCO

    def add(self, objeto):
        self.__objetos.append(objeto)

    def setColor(self, color):
        self.__color = color

    def update(self):
        self.__display.fill(self.__color)

        for objeto in self.__objetos:
            objeto.dibujar(self.__display)