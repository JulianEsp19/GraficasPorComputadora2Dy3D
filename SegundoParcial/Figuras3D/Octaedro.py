import math

from SegundoParcial.Figuras3D import Ejes
from SegundoParcial.Figuras3D.__BaseFiguras3D import __BaseFiguras3D


class Octaedro(__BaseFiguras3D):

    def __init__(self, x, y, z, lado):
        super().__init__()
        self._lado = lado
        self._punto1 = (x, -y, z)
        self.calcularPuntos()

    def calcularPuntos(self):
        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2

        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1),
            (0, 2),
            (2, 3),
            (1, 3),
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4),
            (0, 5),
            (1, 5),
            (2, 5),
            (3, 5),
        ]

        self._proyectar()