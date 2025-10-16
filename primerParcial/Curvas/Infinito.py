import math
from pygame import SurfaceType

from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
class Infinito(__BaseFigurasCirculo):

    def __init__(self, resolucion, radio):
        super().__init__()
        self.__resolucion = resolucion
        self._radio = radio

    def dibujar(self, display: SurfaceType):

        if len(self._puntosScanline):
            self._pintarPuntos(display)
            return

        self.calcularPuntos()

        self._pintarPuntos(display)

    def calcularPuntos(self):
        pasos = 2.5 * math.pi / self.__resolucion

        for i in range(0,self.__resolucion):
            t = pasos * i
            x = (self._radio * math.sin(t))/ (1 + math.cos(t) * math.cos(t))
            y = -((self._radio * math.sin(t) * math.cos(t))/ (1 + math.cos(t) * math.cos(t)))
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))

        self._unionesScanline.pop(-1)

