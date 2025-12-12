import math
from abc import abstractmethod

from multipledispatch import dispatch
from primerParcial.Figuras.LineaDDA import LineaDDA
from primerParcial.Rellenos.Scanline import Scanline
from pygame import SurfaceType


class __BaseFiguras3D:

    def __init__(self):
        self._color = (0, 0, 0, 255)
        self._punto1 = ()
        self._camara = (400, 0, -500)
        self._puntos3D = []
        self._uniones3D = []
        self._puntosScanline = []
        self._unionesScanline = []
        self._relleno = False
        self._colorRelleno = ()
        self.pintando = False
        self._luz = (0, 0, 1)

    @abstractmethod
    def calcularPuntos(self):
        pass

    @dispatch(int, int)
    def setCoordenadas(self, x1, y1):
        self._punto1 = (x1, y1)
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(tuple)
    def setCoordenadas(self, punto1):
        self._punto1 = punto1
        self._puntosScanline = []
        self._unionesScanline = []

    @dispatch(bool)
    def setRelleno(self, containsRelleno):
        self._relleno = containsRelleno

    @dispatch(bool, tuple)
    def setRelleno(self, containsRelleno, color):
        self._relleno = containsRelleno
        self._colorRelleno = color

    def setPosicionCamara(self, x, y, z):
        if z < 0:
            return
        self._camara = (x, -y, -z)
        self._puntosScanline = []

    def trasladarCamara(self, x, y, z):

        self._camara = (self._camara[0]+x, self._camara[1]-y,self._camara[2]-z,)
        self._puntosScanline = []

    def moverCamara(self, x, y, z):
        pass

    def _proyectar(self):

        for i in self._puntos3D:
            x1 = i[0]
            y1 = i[1]
            z1 = i[2]

            u = (-self._camara[2]/(z1-self._camara[2]))

            x = self._camara[0] + (x1 - self._camara[0]) * u
            y = -(self._camara[1] + (y1 - self._camara[1]) * u)

            self._puntosScanline.append((x,y))
            self._unionesScanline = self._uniones3D

    def dibujar(self, display: SurfaceType):
        self.pintando = True
        if len(self._puntosScanline):
            self._rellenar(display)
            self._pintarPuntos(display)
            return

        self._proyectar()

        self._rellenar(display)
        self._pintarPuntos(display)

    def _pintarPuntos(self, display: SurfaceType):

        linea = LineaDDA()
        linea.setColor(self._color)

        if not len(self._puntosScanline):
            return

        for i in self._unionesScanline:
            linea.setCoordenadas(self._puntosScanline[i[0]], self._puntosScanline[i[1]])
            linea.dibujar(display)

        self.pintando = False

    def __isPintando(self):
        return self.pintando

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

    def _calcularCentro(self):
        x, y, z = 0, 0, 0
        for i in self._puntos3D:
            x += i[0]
            y += i[1]
            z += i[2]

        cantidadPuntos = len(self._puntos3D)

        return (x/ cantidadPuntos, y / cantidadPuntos, z / cantidadPuntos)


    def traslacion(self, movimientoX, movimientoY, movimientoZ):
        # |1 0 dx| |x|
        # |0 1 dy| |y|
        # |0 0 1 | |1|

        matriz1 = [
            [1, 0, 0, movimientoX],
            [0, 1, 0, -movimientoY],
            [0, 0, 1, movimientoZ],
            [0, 0, 0, 1]
        ]

        nuevosPuntos = []


        for i in self._puntos3D:
            matriz2 =[
                [i[0]],
                [i[1]],
                [i[2]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], resultado[1][0], resultado[2][0]))


        self._puntos3D = nuevosPuntos

        while self.pintando:
            continue
        self._puntosScanline = []

    def rotacion(self, eje, grados):
        from math import  cos, sin, radians

        matriz1 = []

        if not eje:
            matriz1 = [
                [1, 0, 0, 0],
                [0, cos(radians(grados)), sin(radians(grados)), 0],
                [0, -sin(radians(grados)), cos(radians(grados)), 0],
                [0, 0, 0, 1]
            ]
        elif eje == 1:
            matriz1 = [
                [cos(radians(grados)), 0, -sin(radians(grados)), 0],
                [0, 1, 0, 0],
                [sin(radians(grados)), 0, cos(radians(grados)), 0],
                [0, 0, 0, 1]
            ]
        else:
            matriz1 = [
                [cos(radians(grados)), sin(radians(grados)), 0, 0],
                [-sin(radians(grados)), cos(radians(grados)), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]


        centro = self._calcularCentro()

        nuevosPuntos = []

        for i in self._puntos3D:
            matriz2 = [
                [i[0]],
                [i[1]],
                [i[2]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], resultado[1][0], resultado[2][0]))

        self._puntos3D = nuevosPuntos

        nuevoCentro = self._calcularCentro()

        self.traslacion(-(nuevoCentro[0] - centro[0]), (nuevoCentro[1]-centro[1]), -(nuevoCentro[2]-centro[2]))

    def escalar(self, valorEscala):
        # |sx 0 0| |x|
        # |0 sy 0| |y|
        # |0 0  1| |1|

        matriz1 = [
            [valorEscala, 0, 0, 0],
            [0, valorEscala, 0, 0],
            [0, 0, valorEscala, 0],
            [0, 0, 0, 1]
        ]

        centro = self._calcularCentro()

        nuevosPuntos = []

        for i in self._puntos3D:
            matriz2 = [
                [i[0]],
                [i[1]],
                [i[2]],
                [1]
            ]

            resultado = self.__multiplicarMatriz(matriz1, matriz2)
            nuevosPuntos.append((resultado[0][0], resultado[1][0], resultado[2][0]))

        self._puntos3D = nuevosPuntos

        nuevoCentro = self._calcularCentro()

        self.traslacion(-(nuevoCentro[0] - centro[0]), (nuevoCentro[1] - centro[1]), -(nuevoCentro[2] - centro[2]))

    def _restar(self, a, b):
        return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

    def _cross(self, a, b):
        return (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]
        )

    def _magnitud(self, v):
        return math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)

    def _normalizar(self, v):
        mag = self._magnitud(v)
        if mag == 0:
            return (0, 0, 1)
        return (v[0]/mag, v[1]/mag, v[2]/mag)

    def _dot(self, a, b):
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    def _calcularNormal(self):
        if len(self._puntos3D) < 3:
            return (0, 0, 1)

        p1 = self._puntos3D[0]
        p2 = self._puntos3D[1]
        p3 = self._puntos3D[2]

        v1 = self._restar(p2, p1)
        v2 = self._restar(p3, p1)

        normal = self._cross(v1, v2)
        return self._normalizar(normal)

    def _calcularColorCara(self, caraIndices):
        """Calcula el color de una cara específica basado en su normal."""
        # Obtenemos los 3 puntos 3D de la cara
        p1 = self._puntos3D[caraIndices[0]]
        p2 = self._puntos3D[caraIndices[1]]
        p3 = self._puntos3D[caraIndices[2]]

        # Calcular vectores
        v1 = self._restar(p2, p1)
        v2 = self._restar(p3, p1)

        # Calcular normal de ESTA cara
        normal = self._cross(v1, v2)
        normal = self._normalizar(normal)

        # Color base (usamos el color de relleno o el principal)
        if len(self._colorRelleno):
            base = (int(self._colorRelleno[0]), int(self._colorRelleno[1]), int(self._colorRelleno[2]))
        else:
            base = (int(self._color[0]), int(self._color[1]), int(self._color[2]))

        # Vector de luz (puedes parametrizarlo)
        luz = (0.5, 1, 0.5)  # Luz viene de arriba-derecha-frente
        luz = self._normalizar(luz)

        # Producto punto para intensidad
        intensidad = self._dot(normal, luz)

        # Clamp: que no sea negativo (luz ambiental mínima 0.2)
        if intensidad < 0: intensidad = 0
        iluminacion = 0.2 + (0.8 * intensidad)

        r = max(0, min(255, int(base[0] * iluminacion)))
        g = max(0, min(255, int(base[1] * iluminacion)))
        b = max(0, min(255, int(base[2] * iluminacion)))

        return (r, g, b)

    def _proyectarPunto(self, punto3D):
        """Proyecta un solo punto 3D a 2D"""
        x1, y1, z1 = punto3D
        if (z1 - self._camara[2]) == 0: return (0, 0)  # Evitar div por cero

        u = (-self._camara[2] / (z1 - self._camara[2]))
        x = self._camara[0] + (x1 - self._camara[0]) * u
        y = -(self._camara[1] + (y1 - self._camara[1]) * u)
        return (x, y)

    def dibujarPorCaras(self, display: SurfaceType, listaCaras: list):
        """
        Renderiza la figura cara por cara usando el algoritmo del pintor.
        listaCaras: Lista de tuplas, ej: [(0,1,4), (1,3,4)...] indices de vertices.
        """
        self.pintando = True

        # 1. Preparar lista de renderizado con profundidad (Z promedio)
        carasOrdenadas = []
        for cara in listaCaras:
            # Obtener vertices 3D
            p1 = self._puntos3D[cara[0]]
            p2 = self._puntos3D[cara[1]]
            p3 = self._puntos3D[cara[2]]

            # Profundidad promedio (Z-sorting / Algoritmo del Pintor)
            zPromedio = (p1[2] + p2[2] + p3[2]) / 3.0

            carasOrdenadas.append({
                'indices': cara,
                'z': zPromedio
            })

        # 2. Ordenar caras: las más lejanas (Z menor) se pintan primero
        # Nota: Depende de tu sistema de coordenadas. Si Z+ es hacia ti, ordena descendente.
        carasOrdenadas.sort(key=lambda k: k['z'], reverse=True)

        # 3. Pintar cada cara
        for item in carasOrdenadas:
            indices = item['indices']

            # Calcular color sombreado para esta cara específica
            colorSombreado = self._calcularColorCara(indices)

            # Proyectar los 3 vertices a 2D
            puntos2D = [
                self._proyectarPunto(self._puntos3D[indices[0]]),
                self._proyectarPunto(self._puntos3D[indices[1]]),
                self._proyectarPunto(self._puntos3D[indices[2]])
            ]

            # Uniones para el Scanline (siempre es un triángulo: 0->1, 1->2, 2->0)
            unionesTriangulo = [(0, 1), (1, 2), (2, 0)]

            # Usar tu clase Scanline para rellenar el triángulo
            scanline = Scanline(puntos2D, unionesTriangulo, colorSombreado)
            scanline.rellenar(display)

