import math


class Figuras():
    def __init__(self,display):
        self.__display = display

    def dibujarPixel(self, color, x, y):
        self.__display.set_at((x, y), color)


    def linea(self, color, x1, y1, x2, y2):
        y1 = -y1
        y2 = -y2
        m = (y2 - y1) / (x2 - x1)
        b = y1 - (m * x1)

        while x1 < x2:
            y1 = int(m*x1 + b)
            self.dibujarPixel(color, x1, -y1)
            x1 += 1

    def lineaDDA(self, color, x1, y1, x2, y2):
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
        self.lineaDDA(color, x1, y1, x2, y1)
        self.lineaDDA(color, x1, y1, x1, y2)
        self.lineaDDA(color, x2, y1, x2, y2)
        self.lineaDDA(color, x1, y2, x2, y2)

    def triangulo(self, color, x1, y1, x2, y2):

        puntoCentroX = int((x2 - x1)/2 + x1 if x2 > x1 else (x1 - x2)/2 + x2)

        self.lineaDDA(color, x1, y2, puntoCentroX, y1)
        self.lineaDDA(color, x1, y2, x2, y2)
        self.lineaDDA(color, puntoCentroX, y1, x2, y2)

    def hexagono(self, color, x1, y1, x2, y2):

        puntoCentroY = int((y2 - y1) / 2 + y1 if y2 > y1 else (y1 - y2) / 2 + y2)

        apotema =  y2 - puntoCentroY

        lado = 2 * apotema * math.tan(math.radians(30))

        diferenciaX = int(((x2 - x1) - lado) / 2 if x2 > x1 else ((x1 - x2) - lado) / 2)

        avanceX1 = x1 + diferenciaX
        avanceX2 = x2 - diferenciaX

        self.lineaDDA(color, avanceX1, y1, avanceX2, y1)
        self.lineaDDA(color, avanceX1, y2, avanceX2, y2)
        self.lineaDDA(color, avanceX2, y1, x2, puntoCentroY)
        self.lineaDDA(color, avanceX2, y2, x2, puntoCentroY)
        self.lineaDDA(color, x1, puntoCentroY, avanceX1, y1)
        self.lineaDDA(color, x1, puntoCentroY, avanceX1, y2)

    def hexagonoCirculo(self, color, x1, y2, radio):
        #sen = o    cos = a     tan = o
        #      h          h           a

        #primeros dos puntos del cuadrante superior
        adyacente1 = int(math.cos(math.radians(72)) * radio)
        opuesto1 = int(math.sin(math.radians(72)) * radio)

        print("1.-", adyacente1, opuesto1)

        # primeros dos puntos del cuadrante inferior
        adyacente2 = int(math.cos(math.radians(54)) * radio)
        opuesto2 = int(math.sin(math.radians(54)) * radio)

        print("2.-", adyacente2, opuesto2)

        puntos = (
            (x1, y2 - radio),
            (x1 + opuesto1, y2 - adyacente1),
            (x1 + adyacente2, y2 + opuesto2),
            (x1 - adyacente2, y2 + opuesto2),
            (x1 - opuesto1, y2 - adyacente1)
                  )



        for i in range(0, len(puntos)):
            if i+1 < len(puntos):
                self.lineaDDA(color, puntos[i][0], puntos[i][1], puntos[i+1][0], puntos[i+1][1])
            else:
                self.lineaDDA(color, puntos[i][0], puntos[i][1], puntos[0][0], puntos[0][1])

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

        print("1.-", adyacente1, opuesto1)

        # primeros dos puntos del cuadrante inferior
        adyacente2 = int(math.cos(math.radians(54)) * radio)
        opuesto2 = int(math.sin(math.radians(54)) * radio)

        print("2.-", adyacente2, opuesto2)

        puntos = (
            (x1, y2 - radio),
            (x1 + opuesto1, y2 - adyacente1),
            (x1 + adyacente2, y2 + opuesto2),
            (x1 - adyacente2, y2 + opuesto2),
            (x1 - opuesto1, y2 - adyacente1)
        )

        self.lineaDDA(color, puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1])
        self.lineaDDA(color, puntos[3][0], puntos[3][1], puntos[0][0], puntos[0][1])

        self.lineaDDA(color, puntos[4][0], puntos[4][1], puntos[1][0], puntos[1][1])
        self.lineaDDA(color, puntos[4][0], puntos[4][1], puntos[2][0], puntos[2][1])

        self.lineaDDA(color, puntos[3][0], puntos[3][1], puntos[1][0], puntos[1][1])

    def octagono(self, color, centroX, centroY, radio):

        radioAux = int(radio / 2)

        puntos = (
            (centroX + radio, centroY - radioAux),
            (centroX + radio, centroY + radioAux),

            (centroX + radioAux, centroY + radio),
            (centroX - radioAux, centroY + radio),

            (centroX - radio, centroY + radioAux),
            (centroX - radio, centroY - radioAux),

            (centroX - radioAux, centroY - radio),
            (centroX + radioAux, centroY - radio),

        )

        for i in range(0, len(puntos)):
            if i+1 < len(puntos):
                self.lineaDDA(color, puntos[i][0], puntos[i][1], puntos[i+1][0], puntos[i+1][1])
            else:
                self.lineaDDA(color, puntos[i][0], puntos[i][1], puntos[0][0], puntos[0][1])

        # x, y
        # y, x
        # -y, x
        # -x, y
        # -x, -y
        # -y, -x
        # y, -x
        # x, -y