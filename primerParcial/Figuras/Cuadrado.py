from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFiguras
from primerParcial.Figuras.LineaDDA import LineaDDA

class Cuadrado(__BaseFiguras):

    def dibujar(self, display: SurfaceType):

        if len(self._puntosScanline):
            self._pintarPuntos(display)
            self._rellenar(display)
            return

        x1 = self._punto1[0]
        y1 = self._punto1[1]

        x2 = self._punto2[0]
        y2 = self._punto2[1]

        self._puntosScanline = [
            (x1, y1),
            (x2, y1),
            (x1, y2),
            (x2, y2)
        ]

        self._unionesScanline = [
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3)
        ]

        self._pintarPuntos(display)
        self._rellenar(display)