import time
from idlelib.debugobj import dispatch

from pygame import SurfaceType

from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.animacion.Personajes.Movimiento import Movimiento


class LanzaGuisantes(Movimiento):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__petalos = []
        self.__tiempoAux = time.time()
        self.__tiempo = 0.0
        self._xAnimacion = 0
        self._yAnimacion = 0
        self.__Animacion = True

    def setAnimar(self, isAnimado):
        self.__Animacion = isAnimado

    def __animar(self):
        if self.__tiempo < .3:
            self._xAnimacion = 5
            self._yAnimacion = 5
        elif self.__tiempo < .66:
            self._xAnimacion = 10
            self._yAnimacion = 10
        elif self.__tiempo < .9:
            self._xAnimacion = 5
            self._yAnimacion = 5
        elif self.__tiempo < 1.2:
            self._xAnimacion = 0
            self._yAnimacion = 0
        elif self.__tiempo < 1.5:
            self._xAnimacion = -5
            self._yAnimacion = 5
        elif self.__tiempo < 1.8:
            self._xAnimacion = -10
            self._yAnimacion = 10
        elif self.__tiempo < 2.1:
            self._xAnimacion = -5
            self._yAnimacion = 5
        elif self.__tiempo < 2.4:
            self._xAnimacion = 0
            self._yAnimacion = 0
        elif self.__tiempo > 2.5:
            self.__tiempo = 0

    def dibujar(self, display: SurfaceType):

        self._verificarMovimiento()

        if self.__Animacion:
            self.__tiempo += time.time() - self.__tiempoAux
            self.__tiempoAux = time.time()
            self.__animar()

        tallo = Cuadrado()
        tallo.setCoordenadas(100 + self._x, 90 + self._y, 110 + self._x, 160 + self._y)
        tallo.setRelleno(True, (104, 203, 75))
        tallo.dibujar(display)

        tallo1 = Ovalo()
        tallo1.setResolucion(20)
        tallo1.setCoordenadas(120 + self._x, 160 + self._y, 20, 10)
        tallo1.setRelleno(True, (100, 203, 75))
        tallo1.dibujar(display)

        tallo2 = Ovalo()
        tallo2.setResolucion(20)
        tallo2.setCoordenadas(90 + self._x, 160 + self._y, 20, 10)
        tallo2.setRelleno(True, (104, 203, 75))
        tallo2.dibujar(display)

        hojaCabeza = Ovalo()
        hojaCabeza.setResolucion(10)
        hojaCabeza.setCoordenadas(60 + self._x + self._xAnimacion,
                                  90 + self._y + self._yAnimacion,
                                  8, 15)
        hojaCabeza.calcularPuntos()
        hojaCabeza.rotacion(60)
        hojaCabeza.setRelleno(True, (104, 203, 75))
        hojaCabeza.dibujar(display)



        cabeza = Ovalo()
        cabeza.setCoordenadas(100 + self._x + self._xAnimacion
                              , 100 + self._y + self._yAnimacion, 33, 25)
        cabeza.setRelleno(True, (104, 203, 75))
        cabeza.dibujar(display)

        boca2 = Ovalo()
        boca2.setResolucion(30)
        boca2.setCoordenadas(140 + self._x + self._xAnimacion,
                             100 + self._y + self._yAnimacion,
                             12, 25)
        boca2.setRelleno(True, (104, 203, 75))
        boca2.dibujar(display)

        boca3 = Ovalo()
        boca3.setResolucion(30)
        boca3.setCoordenadas(140 + self._x + self._xAnimacion,
                             100 + self._y + self._yAnimacion,
                             7, 17)
        boca3.setColor((0,0,0))
        boca3.setRelleno(True)
        boca3.dibujar(display)

        ojo1 = Ovalo()
        ojo1.setResolucion(20)
        ojo1.setCoordenadas(98 + self._x + self._xAnimacion
                            , 90 + self._y + self._yAnimacion, 5, 10)
        ojo1.calcularPuntos()
        ojo1.rotacion(20)
        ojo1.setRelleno(True)
        ojo1.dibujar(display)

        luzOjo1 = Ovalo()
        luzOjo1.setResolucion(20)
        luzOjo1.setCoordenadas(97 + self._x + self._xAnimacion
                               , 87 + self._y + self._yAnimacion, 2, 3)
        luzOjo1.setColor((255, 255, 255))
        luzOjo1.setRelleno(True)
        luzOjo1.dibujar(display)

        ojo2 = Ovalo()
        ojo2.setResolucion(10)
        ojo2.setCoordenadas(115 + self._x + self._xAnimacion
                            , 90 + self._y + self._yAnimacion, 4, 8)
        ojo2.calcularPuntos()
        ojo2.rotacion(20)
        ojo2.setRelleno(True)
        ojo2.dibujar(display)

        luzOjo2 = Ovalo()
        luzOjo2.setResolucion(20)
        luzOjo2.setCoordenadas(114 + self._x + self._xAnimacion
                               , 88 + self._y + self._yAnimacion, 2, 3)
        luzOjo2.setColor((255, 255, 255))
        luzOjo2.setRelleno(True)
        luzOjo2.dibujar(display)
