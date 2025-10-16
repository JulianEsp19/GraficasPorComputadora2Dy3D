import math
from pygame import SurfaceType

from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
class CurvaTabla(__BaseFigurasCirculo):

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
        pasos = 10 / self.__resolucion

        for i in range(0, 10):
            t = pasos * i
            x = t - 3 * math.sin(t)
            y = -(4 - 3 * math.sin(t))
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))

        self._unionesScanline.pop(-1)

        self.escalar(20)
