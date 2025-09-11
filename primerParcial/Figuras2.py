import math
import sys

from pygame import SurfaceType


class Figuras():
    def __init__(self, display: SurfaceType):
        self.__display = display

        self.__puntosScanline = []
        self.__unionesScanline = []

        self.__colorAux = ()
        self.__colorFondo = ()
        sys.setrecursionlimit(10000)

    def dibujarPixel(self, color, x, y):
        self.__display.set_at((x, y), color)

    def __obtenerPixel(self, punto: tuple):
        return self.__display.get_at(punto)

    def __ecuacionDeRecta(self, punto1, punto2):

        m = (-punto2[1] - (-punto1[1])) / (punto2[0] - punto1[0])

        b = -punto2[1] - m * punto2[0]

        return (m, b)

    def linea(self, color, x1, y1, x2, y2):
        aux = self.__ecuacionDeRecta((x1, y1), (x2, y2))
        m, b = aux[0], aux[1]

        while x1 < x2:
            y1 = int(m*x1 + b)
            self.dibujarPixel(color, x1, -y1)
            x1 += 1

    def lineaDDA(self, color: tuple, x1 = 0, y1 = 0, x2 = 0, y2 = 0, punto1 = (), punto2 = ()):
        if punto1 and punto2:
            x1 = punto1[0]
            y1 = punto1[1]

            x2 = punto2[0]
            y2 = punto2[1]


        y1 = -y1
        y2 = -y2

        deltaX = x2 - x1
        deltaY = y2 - y1

        pasos = abs(deltaX) if abs(deltaX) > abs(deltaY) else abs(deltaY)

        incrementox = deltaX / pasos
        incrementoy = deltaY / pasos

        for i in range(0, pasos):
            self.dibujarPixel(color, round(x1), -round(y1))
            x1 = x1 + incrementox
            y1 = y1 + incrementoy

    def cuadrado(self, color, x1, y1, x2, y2):
        self.__colorAux = color

        self.__puntosScanline = [
            (x1, y1),
            (x2, y1),
            (x1, y2),
            (x2, y2)
        ]

        self.__unionesScanline = [
            (0,1),
            (0,2),
            (1,3),
            (2, 3)
        ]

        for i in self.__unionesScanline:
            self.lineaDDA(self.__colorAux, punto1=self.__puntosScanline[i[0]], punto2=self.__puntosScanline[i[1]])

    def triangulo(self, color, x1, y1, x2, y2):

        puntoCentroX = int((x2 - x1)/2 + x1 if x2 > x1 else (x1 - x2)/2 + x2)

        self.__colorAux = color

        self.__puntosScanline = [
            (x1, y2),
            (puntoCentroX, y1),
            (x2, y2)
        ]

        self.__unionesScanline = [
            (0, 1),
            (0, 2),
            (1, 2)
        ]

        for i in self.__unionesScanline:
            self.lineaDDA(self.__colorAux, punto1=self.__puntosScanline[i[0]], punto2=self.__puntosScanline[i[1]])

    def hexagono(self, color, x1, y1, x2, y2):

        puntoCentroY = int((y2 - y1) / 2 + y1 if y2 > y1 else (y1 - y2) / 2 + y2)

        apotema =  y2 - puntoCentroY

        lado = 2 * apotema * math.tan(math.radians(30))

        diferenciaX = int(((x2 - x1) - lado) / 2 if x2 > x1 else ((x1 - x2) - lado) / 2)

        avanceX1 = x1 + diferenciaX
        avanceX2 = x2 - diferenciaX

        self.__colorAux = color

        self.__puntosScanline = [
            (avanceX1, y1),
            (avanceX1, y2),
            (avanceX2, y1),
            (avanceX2, y2),
            (x2, puntoCentroY),
            (x1, puntoCentroY)
        ]

        self.__unionesScanline = [
            (0, 2),
            (1, 3),
            (2, 4),
            (3, 4),
            (5, 0),
            (5, 1)
        ]

        for i in self.__unionesScanline:
            self.lineaDDA(self.__colorAux, punto1=self.__puntosScanline[i[0]], punto2=self.__puntosScanline[i[1]])

    def pentagonoCirculo(self, color, x1, y2, radio):
        #sen = o    cos = a     tan = o
        #      h          h           a

        #primeros dos puntos del cuadrante superior
        adyacente1 = int(math.cos(math.radians(72)) * radio)
        opuesto1 = int(math.sin(math.radians(72)) * radio)

        # primeros dos puntos del cuadrante inferior
        adyacente2 = int(math.cos(math.radians(54)) * radio)
        opuesto2 = int(math.sin(math.radians(54)) * radio)

        self.__colorAux = color

        self.__puntosScanline = [ 
            (x1, y2 - radio),
            (x1 + opuesto1, y2 - adyacente1),
            (x1 + adyacente2, y2 + opuesto2),
            (x1 - adyacente2, y2 + opuesto2),
            (x1 - opuesto1, y2 - adyacente1)
        ]
        
        self.__unionesScanline = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 0)
        ]

        for i in self.__unionesScanline:
            self.lineaDDA(self.__colorAux, punto1=self.__puntosScanline[i[0]], punto2=self.__puntosScanline[i[1]])

    def estrella(self, color, x1, y1, x2, y2):
        puntoCentroX = int((x2 - x1) / 2 + x1 if x2 > x1 else (x1 - x2) / 2 + x2)
        puntoCentroY = int((y2 - y1) / 2 + y1 if y2 > y1 else (y1 - y2) / 2 + y2)

        apotemaEstrella = (y2 - puntoCentroY) / 2

        self.lineaDDA(color, puntoCentroX, y1, x2, y2)
        self.lineaDDA(color, x1, y2, puntoCentroX, y1)

        self.lineaDDA(color, x1, puntoCentroY-apotemaEstrella, x2, y2)
        self.lineaDDA(color, x1, y2, x2, puntoCentroY - apotemaEstrella)
        self.lineaDDA(color, x1, puntoCentroY-apotemaEstrella, x2, puntoCentroY - apotemaEstrella)

    def estrellaCirculo(self, color, x1, y2, radio):
        # primeros dos puntos del cuadrante superior
        adyacente1 = int(math.cos(math.radians(72)) * radio)
        opuesto1 = int(math.sin(math.radians(72)) * radio)

        # primeros dos puntos del cuadrante inferior
        adyacente2 = int(math.cos(math.radians(54)) * radio)
        opuesto2 = int(math.sin(math.radians(54)) * radio)

        self.__colorAux = color

        self.__puntosScanline = [
            (x1, y2 - radio),
            (x1 + opuesto1, y2 - adyacente1),
            (x1 + adyacente2, y2 + opuesto2),
            (x1 - adyacente2, y2 + opuesto2),
            (x1 - opuesto1, y2 - adyacente1)
        ]

        self.__unionesScanline = [
            (0, 2),
            (3, 0),
            (4, 1),
            (4, 2),
            (3, 1)
        ]

        for i in self.__unionesScanline:
            self.lineaDDA(self.__colorAux, punto1=self.__puntosScanline[i[0]], punto2=self.__puntosScanline[i[1]])

    def octagono(self, color, centroX, centroY, radio):

        radioAux = int(radio / 2)

        self.__colorAux = color

        self.__puntosScanline = [
            (centroX + radio, centroY - radioAux),
            (centroX + radio, centroY + radioAux),

            (centroX + radioAux, centroY + radio),
            (centroX - radioAux, centroY + radio),

            (centroX - radio, centroY + radioAux),
            (centroX - radio, centroY - radioAux),

            (centroX - radioAux, centroY - radio),
            (centroX + radioAux, centroY - radio),
        ]

        self.__unionesScanline = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 0)
        ]

        for i in self.__unionesScanline:
            self.lineaDDA(self.__colorAux, punto1=self.__puntosScanline[i[0]], punto2=self.__puntosScanline[i[1]])

    #rellena la ultima figura hecha con el metodo de scanLine
    def scanLine(self):
        #( (100,100), (200, 100), (200, 200), (100, 200) ) self.__puntosScanline = ()
        #( (0, 1), (1, 2), (2, 3), (3, 0) ) self.__unionesScaline = ()

        self.__eliminarHorizontales()

        #se calculan los valores de m y b (ecuacion de la recta) antes de empezar
        valoresEcuacionDeRecta = []
        scanline = self.__display.get_size()[1]

        for i in self.__unionesScanline:
            if self.__puntosScanline[i[0]][0] == self.__puntosScanline[i[1]][0]:
                valoresEcuacionDeRecta.append(False)
            else:
                #retorna m y b respectivamente ademas de ser dentro de una tupla
                valoresEcuacionDeRecta.append(self.__ecuacionDeRecta(self.__puntosScanline[i[0]], self.__puntosScanline[i[1]]))

        for i in self.__puntosScanline:
            if i[1] < scanline:
                scanline = i[1]
        scanline += 1

        """
         variables a usar:
         scanline = comienzo del algoritmo
         unionesScanLine = lista de pares de puntos que forman una linea
         puntosScanline = lista de puntos a usar
         valoresEcuacionDeRecta = m y b de la ecuacion de la recta donde si es Falso es una linea totalmente vertical
        """
        while True:
            valoresXAux = []
            for i in range(0, len(self.__unionesScanline)):
                aux = self.__unionesScanline[i]
                if self.__puntosScanline[aux[0]][1] < scanline and self.__puntosScanline[aux[1]][1] >= scanline:
                    if valoresEcuacionDeRecta[i]:
                        valoresXAux.append(self.__calcularXEcuacioRecta(scanline, valoresEcuacionDeRecta[i]))
                    else:
                        valoresXAux.append(self.__puntosScanline[aux[0]][0])


            if not len(valoresXAux):
                break

            valoresXAux.sort()

            for i in range(0, len(valoresXAux), 2):
                if valoresXAux[i] == valoresXAux[i+1]:
                    continue
                punto1 = (valoresXAux[i], scanline)
                punto2 = (valoresXAux[i+1], scanline)
                self.lineaDDA(self.__colorAux, punto1=punto1, punto2=punto2)


            scanline += 1

        # print(self.__unionesScanline)
        # print(self.__puntosScanline)
        # print(scanline)

    def __calcularXEcuacioRecta(self, y, valoresRecta):
        return round(-((valoresRecta[1]-(-y))/valoresRecta[0]))

    def __eliminarHorizontales(self):
        valoresEliminar = []
        for i in self.__unionesScanline:
            #eliminar puntos con lineas horizontales
            if self.__puntosScanline[i[0]][1] == self.__puntosScanline[i[1]][1]:
               valoresEliminar.append(i)
            #acomodar las uniones para que el punto con valor mayor en Y quede primero
            elif self.__puntosScanline[i[0]][1] > self.__puntosScanline[i[1]][1]:
                aux = i[:]
                valoresEliminar.append(i)
                self.__unionesScanline.append((aux[1], aux[0]))

        for i in valoresEliminar:
            self.__unionesScanline.remove(i)


    def inundacion(self):
        puntoInicio = self.__puntoMedio()
        self.__colorFondo = self.__obtenerPixel(puntoInicio)
        if self.__colorFondo == self.__colorAux:
            return
        self.__inundacionRecursivo(puntoInicio[0], puntoInicio[1])

    def __convertirColorRGBA(self):
        nuevoColor = []
        for i in self.__colorAux:
            nuevoColor.append(i)
        nuevoColor.append(255)
        self.__colorAux = tuple(nuevoColor)

    def __inundacionRecursivo(self, x, y):
        w = self.__display.get_size()[0]
        h = self.__display.get_size()[1]

        if x < 0 or x >= w or y < 0 or y >= h or self.__obtenerPixel((x, y)) != self.__colorFondo:
            return

        self.dibujarPixel(self.__colorAux, x, y)
        self.__inundacionRecursivo(x+1,y)
        self.__inundacionRecursivo(x-1,y)
        self.__inundacionRecursivo(x,y+1)
        self.__inundacionRecursivo(x,y-1)


    def __puntoMedio(self):
        x = 0
        y = 0
        for i in self.__puntosScanline:
            x += i[0]
            y += i[1]
        x = round(x/ len(self.__puntosScanline))
        y = round(y / len(self.__puntosScanline))

        return (x, y)

    def traslacion(self, ):
        #|1 0 dx| |x|
        #|0 1 dy| |y|
        #|0 0 1 | |1|
        pass

    def escalar(self, ):
        # |sx 0 0| |x|
        # |0 sy 0| |y|
        # |0 0  1| |1|
        pass