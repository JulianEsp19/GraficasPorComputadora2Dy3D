from multipledispatch import dispatch
from primerParcial.Figuras.LineaDDA import LineaDDA
from primerParcial.Rellenos.Scanline import Scanline
from pygame import SurfaceType


class __BaseFiguras():

    def __init__(self):
        self._color = (0, 0, 0, 255)
        self._punto1 = ()
        self._punto2 = ()
        self._puntosScanline = []
        self._unionesScanline = []
        self._relleno = False
        self._colorRelleno = ()

    @dispatch(int, int, int, int)
    def setCoordenadas(self, x1, y1, x2, y2):
        self._punto1 = (x1, y1)
        self._punto2 = (x2, y2)
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(tuple, tuple)
    def setCoordenadas(self, punto1, punto2):
        self._punto1 = punto1
        self._punto2 = punto2
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(bool)
    def setRelleno(self, containsRelleno):
        self._relleno = containsRelleno

    @dispatch(bool, tuple)
    def setRelleno(self, containsRelleno, color):
        self._relleno = containsRelleno
        self._colorRelleno = color

    def _pintarPuntos(self, display: SurfaceType):

        linea = LineaDDA()
        linea.setColor(self._color)

        for i in self._unionesScanline:
            linea.setCoordenadas(self._puntosScanline[i[0]], self._puntosScanline[i[1]])
            linea.dibujar(display)

    def setColor(self, color):
        self._color = color

    def _rellenar(self, display):
        if not self._relleno:
            return
        if len(self._colorRelleno):
            scanline = Scanline(self._puntosScanline, self._unionesScanline, self._colorRelleno)
        else:
            scanline = Scanline(self._puntosScanline, self._unionesScanline, self._color)
        scanline.rellenar(display)


class __BaseFigurasCirculo():

    def __init__(self):
        self._color = (0, 0, 0, 255)
        self._punto1 = ()
        self._radio = 0
        self._puntosScanline = []
        self._unionesScanline = []
        self._relleno = False
        self._colorRelleno = ()

    @dispatch(int, int, int)
    def setCoordenadas(self, x1, y1, radio):
        self._punto1 = (x1, y1)
        self._radio = radio
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(tuple, int)
    def setCoordenadas(self, punto1, radio):
        self._punto1 = punto1
        self._radio = radio
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(bool)
    def setRelleno(self, containsRelleno):
        self._relleno = containsRelleno

    @dispatch(bool, tuple)
    def setRelleno(self, containsRelleno, color):
        self._relleno = containsRelleno
        self._colorRelleno = color

    def _pintarPuntos(self, display: SurfaceType):
        linea = LineaDDA()
        linea.setColor(self._color)

        for i in self._unionesScanline:
            linea.setCoordenadas(self._puntosScanline[i[0]], self._puntosScanline[i[1]])
            linea.dibujar(display)

    def setColor(self, color):
        self._color = color

    def _rellenar(self, display):
        if not self._relleno:
            return
        if len(self._colorRelleno):
            scanline = Scanline(self._puntosScanline, self._unionesScanline, self._colorRelleno)
        else:
            scanline = Scanline(self._puntosScanline, self._unionesScanline, self._color)
        scanline.rellenar(display)