import time

from pygame import SurfaceType

from primerParcial.Figuras.Circulo import Circulo
from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.animacion.Personajes.Movimiento import Movimiento


class Cursor(Movimiento):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__acelerar = False

    def acelerar(self):
        self.__acelerar = True

    def dibujar(self, display : SurfaceType):

        self._verificarMovimiento()
        if self.__acelerar:
            self._verificarMovimiento()
            self._verificarMovimiento()

        triangulo1 = Circulo()
        triangulo1.setResolucion(3)
        triangulo1.setCoordenadas(100 + self._x, 100 + self._y, 20)
        triangulo1.setRelleno(True)
        triangulo1.dibujar(display)

        triangulo = Circulo()
        triangulo.setResolucion(3)
        triangulo.setCoordenadas(100 + self._x, 100 + self._y, 16)
        triangulo.setColor((255,255,255))
        triangulo.setRelleno(True)
        triangulo.dibujar(display)

        cuadrado2 = Cuadrado()
        cuadrado2.setCoordenadas(105 + self._x, 105 + self._y, 118 + self._x, 125 + self._y)
        cuadrado2.calcularPuntos()
        cuadrado2.rotacion(30)
        cuadrado2.traslacion(-1, 0)
        cuadrado2.setRelleno(True)
        cuadrado2.dibujar(display)

        cuadrado1 = Cuadrado()
        cuadrado1.setCoordenadas(100 + self._x, 105 + self._y, 108 + self._x, 125 + self._y)
        cuadrado1.calcularPuntos()
        cuadrado1.rotacion(30)
        cuadrado1.traslacion(5, -2)
        cuadrado1.setColor((255,255,255))
        cuadrado1.setRelleno(True)
        cuadrado1.dibujar(display)


