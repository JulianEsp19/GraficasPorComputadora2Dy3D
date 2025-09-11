from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFiguras
from primerParcial.Figuras.Pixel import Pixel

class LineaDDA(__BaseFiguras):

    def dibujar(self, display: SurfaceType):

        x1 = self._punto1[0]
        y1 = -self._punto1[1]

        x2 = self._punto2[0]
        y2 = -self._punto2[1]

        pixel = Pixel()
        pixel.setColor(self._color)

        deltaX = x2 - x1
        deltaY = y2 - y1

        pasos = abs(deltaX) if abs(deltaX) > abs(deltaY) else abs(deltaY)

        incrementox = deltaX / pasos
        incrementoy = deltaY / pasos

        for i in range(0, pasos):
            pixel.setCoordenadas(round(x1), -round(y1))
            pixel.dibujar(display)
            x1 = x1 + incrementox
            y1 = y1 + incrementoy