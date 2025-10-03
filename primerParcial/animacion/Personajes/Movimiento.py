
class Movimiento():

    def __init__(self, x, y):
        self.__moviemntoX = 0
        self.__movimientoY = 0
        self.__Pasos = ()
        self._x = x
        self._y = y
        self.__xAux = x
        self.__yAux = y
        self.__moviendose = False

    def isMoviendo(self):
        return self.__moviendose

    def mover(self, movimientoX, movimientoY):
        if movimientoX == 0:
            self.__Pasos = (0, 2) if movimientoY > 0 else (0, -2)
        elif movimientoY == 0:
            self.__Pasos = (2, 0) if movimientoX > 0 else (-2, 0)
        elif movimientoY == movimientoX:
            self.__Pasos = (2, 2) if movimientoX > 0 else (-2, -2)
        elif movimientoY < 0 and movimientoX < 0:
            self.__Pasos = (-2, -(movimientoY / movimientoX) * 2) if movimientoX > movimientoY else (
            -(movimientoX / movimientoY) * 2, -2)
        else:
            self.__Pasos = (2, (movimientoY/movimientoX) * 2) if movimientoX > movimientoY else ((movimientoX/movimientoY) * 2, 2)
        self.__moviemntoX = movimientoX
        self.__movimientoY = movimientoY
        self.__moviendose = True

    def __mover(self):
        self.__xAux = self.__xAux + self.__Pasos[0]
        self.__yAux = self.__yAux + self.__Pasos[1]
        self._x = round(self.__xAux)
        self._y = round(self.__yAux)

        self.__moviemntoX -= self.__Pasos[0]
        self.__movimientoY -= self.__Pasos[1]

    def cambiarUbicacion(self, x, y):
        self._x = x
        self._y = y
        self.__xAux = x
        self.__yAux = y

    def _verificarMovimiento(self):
        if round(self.__moviemntoX) != 0 or round(self.__movimientoY) != 0:
            self.__mover()
        else:
            self.__moviendose = False