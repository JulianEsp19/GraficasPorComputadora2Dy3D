import math

from SegundoParcial.Figuras3D import Ejes
from SegundoParcial.Figuras3D.__BaseFiguras3D import __BaseFiguras3D


class RelojArena(__BaseFiguras3D):

    def __init__(self, x, y, z, resolucionNivel, resolucionZ, escala):
        super().__init__()
        self._resolucion = resolucionNivel
        self._resolucionZ = resolucionZ
        self._punto1 = (x, -y, z)
        self.calcularPuntos()
        self.traslacion(x, y, z)
        self.rotacion(Ejes.X, 80)
        self.rotacion(Ejes.Y, 90)
        self.rotacion(Ejes.Z, 10)

        self.escalar(escala)

    def calcularPuntos(self):
        from math import pi, cos, sin

        resolucion = (2 * pi) / self._resolucion

        resolucionZ = 8 / self._resolucionZ



        for z in range(self._resolucionZ):
            for phi in range(self._resolucion):
                x = (2 + cos(z * resolucionZ)) * cos(phi * resolucion)
                y = (2 + cos(z * resolucionZ)) * sin(phi * resolucion)

                self._puntos3D.append((x, y, z))
                if phi == 0 : continue
                if phi == (self._resolucion -1):
                    self._uniones3D.append((len(self._puntos3D) - 2, len(self._puntos3D) - 1))
                    self._uniones3D.append((self._resolucion * z, len(self._puntos3D)-1))
                else:
                    self._uniones3D.append((len(self._puntos3D)-2, len(self._puntos3D)-1))

        for unionesZ in range((self._resolucionZ * self._resolucion)-self._resolucion):
            self._uniones3D.append((unionesZ, unionesZ+self._resolucion))

        print(len(self._uniones3D))
        print(self._puntos3D)

        self._proyectar()