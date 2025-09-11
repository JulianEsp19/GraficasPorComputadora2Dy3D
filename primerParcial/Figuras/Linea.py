from pygame import SurfaceType
from primerParcial.Figuras.__BaseFiguras import __BaseFiguras
from primerParcial.Figuras.Pixel import Pixel

class Linea(__BaseFiguras):

    def dibujar(self, display: SurfaceType):
        pixel = Pixel()

        aux = self.__ecuacionDeRecta(self._punto1, self._punto2)
        m, b = aux[0], aux[1]

        x1 = self._punto1[0]
        x2 = self._punto2[0]

        pixel.setColor(self._color)

        while x1 < x2:
            y1 = int(m * x1 + b)
            pixel.setCoordenadas(x1, -y1)
            pixel.dibujar(display)
            x1 += 1

    def __ecuacionDeRecta(self, punto1, punto2):

        m = (-punto2[1] - (-punto1[1])) / (punto2[0] - punto1[0])

        b = -punto2[1] - m * punto2[0]

        return (m, b)