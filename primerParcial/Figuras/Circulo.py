import math
from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
from primerParcial.Figuras.LineaDDA import LineaDDA

class Circulo(__BaseFigurasCirculo):

    def __init__(self):
        super().__init__()
        self.__resolucion = 100


    def dibujar(self, display: SurfaceType):
        x1 = self._punto1[0]
        y1 = self._punto1[1]

        paso = (2 * math.pi) / self.__resolucion

        for i in range(self.__resolucion):
            angulo = paso * i
            x = round(x1 + self._radio * math.cos(angulo))
            y = round(y1 + self._radio * math.sin(angulo))
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))
        self._unionesScanline.pop(-1)
        self._unionesScanline.append((self.__resolucion-1, 0))

        linea = LineaDDA()
        linea.setColor(self._color)

        for i in self._unionesScanline:
            linea.setCoordenadas(self._puntosScanline[i[0]], self._puntosScanline[i[1]])
            linea.dibujar(display)

    def setResolucion(self, resolucion):
        self.__resolucion = resolucion