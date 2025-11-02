from pygame import SurfaceType
from primerParcial.Figuras.Pixel import Pixel
from multipledispatch import dispatch

class LineaDDA():
    def __init__(self):
        self._color = (0, 0, 0, 255)
        self._punto1 = ()
        self._punto2 = ()

    @dispatch(int, int, int, int)
    def setCoordenadas(self, x1, y1, x2, y2):
        self._punto1 = (x1, y1)
        self._punto2 = (x2, y2)


    @dispatch(tuple, tuple)
    def setCoordenadas(self, punto1, punto2):
        self._punto1 = punto1
        self._punto2 = punto2

    def setColor(self, color):
        self._color = color

    def dibujar(self, display: SurfaceType):

        x1 = round(self._punto1[0])
        y1 = -round(self._punto1[1])

        x2 = round(self._punto2[0])
        y2 = -round(self._punto2[1])

        if x1 == x2 and y1 == y2:
            return

        pixel = Pixel()
        pixel.setColor(self._color)

        deltaX = x2 - x1
        deltaY = y2 - y1

        pasos = abs(deltaX) if abs(deltaX) > abs(deltaY) else abs(deltaY)

        print(self._punto1, self._punto2)
        incrementox = deltaX / pasos
        incrementoy = deltaY / pasos

        for i in range(0, pasos):
            pixel.setCoordenadas(round(x1), -round(y1))
            pixel.dibujar(display)
            x1 = x1 + incrementox
            y1 = y1 + incrementoy