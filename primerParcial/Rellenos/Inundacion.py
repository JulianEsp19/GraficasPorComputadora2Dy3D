import sys

from pygame import SurfaceType
from threading import Thread

from primerParcial.Figuras.Pixel import Pixel


class Inundacion(Thread):
    def __init__(self, puntoInicio: tuple, display: SurfaceType, color: tuple):
        super().__init__(target=self.rellenar)
        self.__puntoInicio = puntoInicio
        self.__display = display
        self.__colorAux = self.__convertirColorRGBA(color) if len(color) == 3 else color
        self.__colorFondo = self.__obtenerPixel(self.__puntoInicio)
        self.__pixel = Pixel()
        self.__pixel.setColor(color)
        sys.setrecursionlimit(10000)

    def __convertirColorRGBA(self, color):
        nuevoColor = []
        for i in color:
            nuevoColor.append(i)
        nuevoColor.append(255)
        return  tuple(nuevoColor)

    def __obtenerPixel(self, punto: tuple):
        return self.__display.get_at(punto)

    def rellenar(self):
        self.__colorFondo = self.__obtenerPixel(self.__puntoInicio)
        if self.__colorFondo == self.__colorAux:
            return
        self.__inundacionRecursivo(self.__puntoInicio[0], self.__puntoInicio[1])

    def __inundacionRecursivo(self, x, y):
        w, h = self.__display.get_size()
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            if x < 0 or x >= w or y < 0 or y >= h:
                continue
            if self.__obtenerPixel((x, y)) != self.__colorFondo:
                continue

            self.__pixel.setCoordenadas(x, y)
            self.__pixel.dibujar(self.__display)

            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))