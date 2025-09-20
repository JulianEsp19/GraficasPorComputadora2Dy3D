import math
from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFiguras
from primerParcial.Figuras.LineaDDA import LineaDDA

class Hexagono(__BaseFiguras):

    def dibujar(self, display: SurfaceType):

        if len(self._puntosScanline):
            self._rellenar(display)
            self._pintarPuntos(display)
            return

        x1 = self._punto1[0]
        y1 = self._punto1[1]

        x2 = self._punto2[0]
        y2 = self._punto2[1]

        puntoCentroY = int((y2 - y1) / 2 + y1 if y2 > y1 else (y1 - y2) / 2 + y2)

        apotema = y2 - puntoCentroY

        lado = 2 * apotema * math.tan(math.radians(30))

        diferenciaX = int(((x2 - x1) - lado) / 2 if x2 > x1 else ((x1 - x2) - lado) / 2)

        avanceX1 = x1 + diferenciaX
        avanceX2 = x2 - diferenciaX

        self._puntosScanline = [
            (avanceX1, y1),
            (avanceX1, y2),
            (avanceX2, y1),
            (avanceX2, y2),
            (x2, puntoCentroY),
            (x1, puntoCentroY)
        ]

        self._unionesScanline = [
            (0, 2),
            (1, 3),
            (2, 4),
            (3, 4),
            (5, 0),
            (5, 1)
        ]

        self._rellenar(display)
        self._pintarPuntos(display)
