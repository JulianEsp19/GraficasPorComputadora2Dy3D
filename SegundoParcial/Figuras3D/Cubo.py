from SegundoParcial.Figuras3D.__BaseFiguras3D import __BaseFiguras3D


class Cubo(__BaseFiguras3D):

    def __init__(self, x, y, z, lado):
        super().__init__()
        self._lado = lado
        self._punto1 = (x, -y, z)
        self.calcularPuntos()

    def calcularPuntos(self):
        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        self._puntos3D = (
            (x, y, z), #0
            (x + self._lado, y, z), #1
            (x, y - self._lado, z), #2
            (x + self._lado, y - self._lado, z), #3
            (x, y, z + self._lado), #4
            (x + self._lado, y, z + self._lado), #5
            (x, y - self._lado, z + self._lado), #6
            (x + self._lado, y - self._lado, z + self._lado) #7
        )

        self._uniones3D = (
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 6),
            (5, 7),
            (6, 7)
        )

        self._proyectar()