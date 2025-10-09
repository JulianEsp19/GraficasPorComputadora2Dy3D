import math
from pygame import SurfaceType

from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
class Curva1(__BaseFigurasCirculo):

    def __init__(self, resolucion):
        super().__init__()
        self.__resolucion = resolucion

    def dibujar(self, display: SurfaceType):

        if len(self._puntosScanline):
            self._pintarPuntos(display)
            return

        self.calcularPuntos()

        self._pintarPuntos(display)

    def calcularPuntos(self):
        pasos = math.pi / self.__resolucion

        for i in range(0,self.__resolucion+1):
            x = pasos * i
            y = -math.sin(x)
            print(y, x)
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))

        self._unionesScanline.pop(-1)
