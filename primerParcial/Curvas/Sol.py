import math
from pygame import SurfaceType

from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
class Sol(__BaseFigurasCirculo):

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
        pasos = 14 * math.pi / self.__resolucion

        for i in range(0,self.__resolucion):
            t = pasos * i
            x = 17 * math.cos(t) + 7 * math.cos((17/7) * t)
            y = -(17 * math.sin(t) - 7 * math.sin((17/7) * t))
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))

        self._unionesScanline.pop(-1)
        self._unionesScanline.append((self.__resolucion-1, 0))

        self.escalar(8)