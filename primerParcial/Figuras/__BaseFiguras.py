from multipledispatch import dispatch

class __BaseFiguras():

    def __init__(self):
        self._color = (0, 0, 0, 255)
        self._punto1 = ()
        self._punto2 = ()
        self._puntosScanline = []
        self._unionesScanline = []

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

    def setColor(self, color):
        self._color = color

class __BaseFigurasCirculo():

    def __init__(self):
        self._color = (0, 0, 0, 255)
        self._punto1 = ()
        self._radio = 0
        self._puntosScanline = []
        self._unionesScanline = []

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

    def setColor(self, color):
        self._color = color