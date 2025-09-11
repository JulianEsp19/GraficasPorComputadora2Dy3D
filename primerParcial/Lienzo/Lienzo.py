from pygame import SurfaceType
from primerParcial.Colores import Colores as cl

class Lienzo():
    def __init__(self, display: SurfaceType):
        self.__display = display
        self.__objetos = []

    def add(self, objeto):
        self.__objetos.append(objeto)

    def update(self):
        self.__display.fill(cl.BLANCO)

        for objeto in self.__objetos:
            objeto.dibujar(self.__display)