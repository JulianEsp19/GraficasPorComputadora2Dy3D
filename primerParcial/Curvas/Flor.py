import math
from pygame import SurfaceType

from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
class Flor(__BaseFigurasCirculo):

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
        pasos = 2 * math.pi / self.__resolucion

        for i in range(0,self.__resolucion):
            t = pasos * i
            x = math.cos(t) + 0.5 * math.cos(7 * t) + 0.33 * math.sin(17*t)
            y = -(math.sin(t) + 0.5 * math.sin(7 * t) + 0.33 * math.cos(17 * t))
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))

        self._unionesScanline.pop(-1)
        self._unionesScanline.append((self.__resolucion-1, 0))

        self.escalar(100)