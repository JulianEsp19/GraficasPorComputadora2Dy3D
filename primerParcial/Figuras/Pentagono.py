import math
from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFigurasCirculo
from primerParcial.Figuras.LineaDDA import LineaDDA

class Pentagono(__BaseFigurasCirculo):

    def dibujar(self, display: SurfaceType):

        if len(self._puntosScanline):
            self._pintarPuntos(display)
            self._rellenar(display)
            return

        x1 = self._punto1[0]
        y1 = self._punto1[1]

        # primeros dos puntos del cuadrante superior
        adyacente1 = int(math.cos(math.radians(72)) * self._radio)
        opuesto1 = int(math.sin(math.radians(72)) * self._radio)

        # primeros dos puntos del cuadrante inferior
        adyacente2 = int(math.cos(math.radians(54)) * self._radio)
        opuesto2 = int(math.sin(math.radians(54)) * self._radio)

        self._puntosScanline = [
            (x1, y1 - self._radio),
            (x1 + opuesto1, y1 - adyacente1),
            (x1 + adyacente2, y1 + opuesto2),
            (x1 - adyacente2, y1 + opuesto2),
            (x1 - opuesto1, y1 - adyacente1)
        ]

        self._unionesScanline = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 0)
        ]

        self._pintarPuntos(display)
        self._rellenar(display)