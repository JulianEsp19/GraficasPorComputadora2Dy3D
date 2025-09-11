import math
from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
from primerParcial.Figuras.LineaDDA import LineaDDA

class Octagono(__BaseFigurasCirculo):

    def dibujar(self, display: SurfaceType):
        x1 = self._punto1[0]
        y1 = self._punto1[1]

        radioAux = int(self._radio / 2)

        self._puntosScanline = [
            (x1 + self._radio, y1 - radioAux),
            (x1 + self._radio, y1 + radioAux),

            (x1 + radioAux, y1 + self._radio),
            (x1 - radioAux, y1 + self._radio),

            (x1 - self._radio, y1 + radioAux),
            (x1 - self._radio, y1 - radioAux),

            (x1 - radioAux, y1 - self._radio),
            (x1 + radioAux, y1 - self._radio),
        ]

        self._unionesScanline = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 0)
        ]

        linea = LineaDDA()
        linea.setColor(self._color)

        for i in self._unionesScanline:
            linea.setCoordenadas(self._puntosScanline[i[0]], self._puntosScanline[i[1]])
            linea.dibujar(display)