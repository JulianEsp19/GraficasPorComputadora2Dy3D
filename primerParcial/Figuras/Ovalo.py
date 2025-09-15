import math
from pygame import SurfaceType
from multipledispatch import dispatch
from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo

class Ovalo(__BaseFigurasCirculo):

    def __init__(self):
        super().__init__()
        self.__resolucion = 100
        self._radio2 = 0

    @dispatch(int, int, int, int)
    def setCoordenadas(self, x1, y1, radio1, radio2):
        self._punto1 = (x1, y1)
        self._radio = radio1
        self._radio2 = radio2
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(tuple, int, int)
    def setCoordenadas(self, punto1, radio1, radio2):
        self._punto1 = punto1
        self._radio = radio1
        self._radio2 = radio2
        self._puntosScanline = []
        self._unionesScanline = []

    def dibujar(self, display: SurfaceType):
        if len(self._puntosScanline):
            self._pintarPuntos(display)
            self._rellenar(display)
            return

        x1 = self._punto1[0]
        y1 = self._punto1[1]

        paso = (2 * math.pi) / self.__resolucion

        for i in range(self.__resolucion):
            angulo = paso * i
            x = round(x1 + self._radio * math.cos(angulo))
            y = round(y1 + self._radio2 * math.sin(angulo))
            self._puntosScanline.append((x, y))
            self._unionesScanline.append((i, i+1))
        self._unionesScanline.pop(-1)
        self._unionesScanline.append((self.__resolucion-1, 0))

        self._pintarPuntos(display)
        self._rellenar(display)

    def setResolucion(self, resolucion):
        self.__resolucion = resolucion