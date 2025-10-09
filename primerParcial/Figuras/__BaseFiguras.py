import math

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

    def __multiplicarMatriz(self, matriz1, matriz2):
        matrizResultante = []

        for i in matriz1:
            resultado = 0
            for j in range(len(i)):
                resultado += i[j] * matriz2[j][0]
            matrizResultante.append([resultado])

        return matrizResultante

    def __calcularCentro(self):
        x, y = 0, 0
        for i in self._puntosScanline:
            x += i[0]
            y += i[1]

        return (int(x/ len(self._puntosScanline)), int(y / len(self._puntosScanline)))


    def traslacion(self, movimientoX, movimientoY):
        # |1 0 dx| |x|
        # |0 1 dy| |y|
        # |0 0 1 | |1|

        matriz1 = [
            [1, 0, movimientoX],
            [0, 1, -movimientoY],
            [0, 0, 1]
        ]

        nuevosPuntos = []

        for i in self._puntosScanline:
            matriz2 =[
                [i[0]],
                [-i[1]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], -resultado[1][0]))


        self._puntosScanline = nuevosPuntos

    def rotacion(self, grados):
        matriz1 = [
            [math.cos(math.radians(grados)), -math.sin(math.radians(grados))],
            [math.sin(math.radians(grados)), math.cos(math.radians(grados))],
        ]

        centro = self.__calcularCentro()

        nuevosPuntos = []

        for i in self._puntosScanline:
            matriz2 = [
                [i[0]],
                [-i[1]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((round(resultado[0][0]), -round(resultado[1][0])))

        self._puntosScanline = nuevosPuntos

        nuevoCentro = self.__calcularCentro()

        self.traslacion(-(nuevoCentro[0] - centro[0]), -(nuevoCentro[1] - (centro[1])))

    def escalar(self, valorEscala):
        # |sx 0 0| |x|
        # |0 sy 0| |y|
        # |0 0  1| |1|

        matriz1 = [
            [valorEscala, 0, 0],
            [0, valorEscala, 0],
            [0, 0, 1]
        ]

        centro = self.__calcularCentro()

        nuevosPuntos = []

        for i in self._puntosScanline:
            matriz2 = [
                [i[0]],
                [-i[1]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((round(resultado[0][0]), -round(resultado[1][0])))

        self._puntosScanline = nuevosPuntos

        nuevoCentro = self.__calcularCentro()

        self.traslacion(-(nuevoCentro[0] - centro[0]), -(nuevoCentro[1] - (centro[1])))


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

    def __multiplicarMatriz(self, matriz1, matriz2):
        matrizResultante = []

        for i in matriz1:
            resultado = 0
            for j in range(len(i)):
                resultado += i[j] * matriz2[j][0]
            matrizResultante.append([resultado])

        return matrizResultante

    def __calcularCentro(self):
        x, y = 0, 0
        for i in self._puntosScanline:
            x += i[0]
            y += i[1]

        return (int(x/ len(self._puntosScanline)), int(y / len(self._puntosScanline)))


    def traslacion(self, movimientoX, movimientoY):
        # |1 0 dx| |x|
        # |0 1 dy| |y|
        # |0 0 1 | |1|

        matriz1 = [
            [1, 0, movimientoX],
            [0, 1, -movimientoY],
            [0, 0, 1]
        ]

        nuevosPuntos = []

        for i in self._puntosScanline:
            matriz2 =[
                [i[0]],
                [-i[1]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], -resultado[1][0]))


        self._puntosScanline = nuevosPuntos

    def rotacion(self, grados):
        matriz1 = [
            [math.cos(math.radians(grados)), -math.sin(math.radians(grados))],
            [math.sin(math.radians(grados)), math.cos(math.radians(grados))],
        ]

        centro = self.__calcularCentro()

        nuevosPuntos = []

        for i in self._puntosScanline:
            matriz2 = [
                [i[0]],
                [-i[1]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], -resultado[1][0]))

        self._puntosScanline = nuevosPuntos

        nuevoCentro = self.__calcularCentro()

        self.traslacion(-(nuevoCentro[0] - centro[0]), -(nuevoCentro[1] - (centro[1])))

    def escalar(self, valorEscala):
        # |sx 0 0| |x|
        # |0 sy 0| |y|
        # |0 0  1| |1|

        matriz1 = [
            [valorEscala, 0, 0],
            [0, valorEscala, 0],
            [0, 0, 1]
        ]

        centro = self.__calcularCentro()

        nuevosPuntos = []

        for i in self._puntosScanline:
            matriz2 = [
                [i[0]],
                [-i[1]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], -resultado[1][0]))

        self._puntosScanline = nuevosPuntos

        nuevoCentro = self.__calcularCentro()

        self.traslacion(-(nuevoCentro[0] - centro[0]), -(nuevoCentro[1] - (centro[1])))