import pygame
from pygame import SurfaceType
from primerParcial.Figuras.LineaDDA import LineaDDA


class Scanline():
    def __init__(self, puntos: list, uniones: list, color: tuple):
        self.__unionesScanline = uniones[:]
        self.__puntosScanline = puntos[:]
        self.__color = color

    def setPuntos(self, puntos: list):
        self.__puntosScanline = puntos

    def setUniones(self, uniones: list):
        self.__unionesScanline = uniones[:]

    def setColor(self, color):
        self.__color = color

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

    def __ecuacionDeRecta(self, punto1, punto2):

        m = (-punto2[1] - (-punto1[1])) / (punto2[0] - punto1[0])

        b = -punto2[1] - m * punto2[0]

        return (m, b)

    def rellenar(self, display: SurfaceType):
        # ( (100,100), (200, 100), (200, 200), (100, 200) ) self.__puntosScanline = ()
        # ( (0, 1), (1, 2), (2, 3), (3, 0) ) self.__unionesScaline = ()

        self.__eliminarHorizontales()

        # se calculan los valores de m y b (ecuacion de la recta) antes de empezar
        valoresEcuacionDeRecta = []
        scanline = display.get_size()[1]

        for i in self.__unionesScanline:
            if self.__puntosScanline[i[0]][0] == self.__puntosScanline[i[1]][0]:
                valoresEcuacionDeRecta.append(False)
            else:
                # retorna m y b respectivamente ademas de ser dentro de una tupla
                valoresEcuacionDeRecta.append(
                    self.__ecuacionDeRecta(self.__puntosScanline[i[0]], self.__puntosScanline[i[1]]))

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

        #linea = LineaDDA()
        #linea.setColor(self.__color)

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

            for i in range(0, len(valoresXAux)-1, 1):
                if valoresXAux[i] == valoresXAux[i + 1]:
                    continue
                punto1 = (valoresXAux[i], scanline)
                punto2 = (valoresXAux[i + 1], scanline)
                #linea.setCoordenadas(punto1, punto2)
                #linea.dibujar(display)
                pygame.draw.line(display, self.__color, punto1, punto2)

            scanline += 1