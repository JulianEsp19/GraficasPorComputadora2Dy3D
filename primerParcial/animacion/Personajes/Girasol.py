import time
from idlelib.debugobj import dispatch

from pygame import SurfaceType

from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.Figuras.Ovalo import Ovalo


class Girasol():

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__objetos = []
        self.__petalos = []
        self.__tiempoAux = time.time()
        self.__tiempo = 0.0
        self.__xAnimacion = 0
        self.__yAnimacion = 0
        self.__Animacion = True

    def setAnimar(self, isAnimado):
        self.__Animacion = isAnimado

    def __animar(self):
        if self.__tiempo < .3:
            self.__xAnimacion = 5
            self.__yAnimacion = 5
        elif self.__tiempo < .66:
            self.__xAnimacion = 10
            self.__yAnimacion = 10
        elif self.__tiempo < .9:
            self.__xAnimacion = 5
            self.__yAnimacion = 5
        elif self.__tiempo < 1.2:
            self.__xAnimacion = 0
            self.__yAnimacion = 0
        elif self.__tiempo < 1.5:
            self.__xAnimacion = -5
            self.__yAnimacion = 5
        elif self.__tiempo < 1.8:
            self.__xAnimacion = -10
            self.__yAnimacion = 10
        elif self.__tiempo < 2.1:
            self.__xAnimacion = -5
            self.__yAnimacion = 5
        elif self.__tiempo < 2.4:
            self.__xAnimacion = 0
            self.__yAnimacion = 0
        elif self.__tiempo > 2.5:
            self.__tiempo = 0

    def dibujar(self, display : SurfaceType):


        if self.__Animacion:
            self.__tiempo += time.time() - self.__tiempoAux
            self.__tiempoAux = time.time()
            self.__animar()

        tallo = Cuadrado()
        tallo.setCoordenadas(100 + self.__x, 80 + self.__y, 110 + self.__x, 160 + self.__y)
        tallo.setColor((104, 203, 75))
        tallo.setRelleno(True)
        tallo.dibujar(display)

        tallo1 = Ovalo()
        tallo1.setResolucion(20)
        tallo1.setCoordenadas(120 + self.__x, 160 + self.__y, 20, 10)
        tallo1.setColor((100, 203, 75))
        tallo1.setRelleno(True)
        tallo1.dibujar(display)

        tallo2 = Ovalo()
        tallo2.setResolucion(20)
        tallo2.setCoordenadas(90 + self.__x, 160 + self.__y, 20, 10)
        tallo2.setColor((104, 203, 75))
        tallo2.setRelleno(True)
        tallo2.dibujar(display)

        petalo2 = Ovalo()
        petalo2.setResolucion(30)
        petalo2.setCoordenadas(100 + self.__x + self.__xAnimacion,
                               100 + self.__y + self.__yAnimacion, 8, 55)
        petalo2.setColor((224, 195, 49))
        petalo2.setRelleno(True)
        petalo2.calcularPuntos()
        petalo2.rotacion(90)
        petalo2.dibujar(display)

        petalo3 = Ovalo()
        petalo3.setResolucion(30)
        petalo3.setCoordenadas(100 + self.__x + self.__xAnimacion
                               , 100 + self.__y + self.__yAnimacion, 8, 50)
        petalo3.setColor((224, 195, 49))
        petalo3.setRelleno(True)
        petalo3.calcularPuntos()
        petalo3.rotacion(75)
        petalo3.dibujar(display)

        petalo4 = Ovalo()
        petalo4.setResolucion(30)
        petalo4.setCoordenadas(100 + self.__x + self.__xAnimacion
                               , 100 + self.__y+ self.__yAnimacion, 8, 50)
        petalo4.setColor((224, 195, 49))
        petalo4.setRelleno(True)
        petalo4.calcularPuntos()
        petalo4.rotacion(60)
        petalo4.dibujar(display)
        
        petalo5 = Ovalo()
        petalo5.setResolucion(30)
        petalo5.setCoordenadas(100 + self.__x+ self.__xAnimacion
                               , 100 + self.__y + self.__yAnimacion, 8, 45)
        petalo5.setColor((224, 195, 49))
        petalo5.setRelleno(True)
        petalo5.calcularPuntos()
        petalo5.rotacion(40)
        petalo5.dibujar(display)
        
        
        petalo6 = Ovalo()
        petalo6.setResolucion(30)
        petalo6.setCoordenadas(100 + self.__x + self.__xAnimacion
                               , 100 + self.__y + self.__yAnimacion, 8, 45)
        petalo6.setColor((224, 195, 49))
        petalo6.setRelleno(True)
        petalo6.calcularPuntos()
        petalo6.rotacion(20)
        petalo6.dibujar(display)
        
        petalo7 = Ovalo()
        petalo7.setResolucion(30)
        petalo7.setCoordenadas(100 + self.__x + self.__xAnimacion
                               , 100 + self.__y + self.__yAnimacion, 8, 45)
        petalo7.setColor((224, 195, 49))
        petalo7.setRelleno(True)
        petalo7.dibujar(display)

        petalo8 = Ovalo()
        petalo8.setResolucion(30)
        petalo8.setCoordenadas(100 + self.__x + self.__xAnimacion
                               , 100 + self.__y + self.__yAnimacion, 8, 45)
        petalo8.setColor((224, 195, 49))
        petalo8.setRelleno(True)
        petalo8.calcularPuntos()
        petalo8.rotacion(-20)
        petalo8.dibujar(display)
        
        petalo9 = Ovalo()
        petalo9.setResolucion(30)
        petalo9.setCoordenadas(100 + self.__x + self.__xAnimacion
                               , 100 + self.__y + self.__yAnimacion, 8, 45)
        petalo9.setColor((224, 195, 49))
        petalo9.setRelleno(True)
        petalo9.calcularPuntos()
        petalo9.rotacion(-40)
        petalo9.dibujar(display)

        petalo10 = Ovalo()
        petalo10.setResolucion(30)
        petalo10.setCoordenadas(100 + self.__x + self.__xAnimacion
                                , 100 + self.__y + self.__yAnimacion, 8, 50)
        petalo10.setColor((224, 195, 49))
        petalo10.setRelleno(True)
        petalo10.calcularPuntos()
        petalo10.rotacion(-60)
        petalo10.dibujar(display)

        petalo11 = Ovalo()
        petalo11.setResolucion(30)
        petalo11.setCoordenadas(100 + self.__x + self.__xAnimacion
                                , 100 + self.__y + self.__yAnimacion, 8, 50)
        petalo11.setColor((224, 195, 49))
        petalo11.setRelleno(True)
        petalo11.calcularPuntos()
        petalo11.rotacion(-75)
        petalo11.dibujar(display)
        
        cabeza = Ovalo()
        cabeza.setCoordenadas(100 + self.__x + self.__xAnimacion
                              , 100 + self.__y + self.__yAnimacion, 40, 25)
        cabeza.setColor((224, 152, 49))
        cabeza.setRelleno(True)
        cabeza.dibujar(display)

        boca = Ovalo()
        boca.setResolucion(50)
        boca.setCoordenadas(100 + self.__x + self.__xAnimacion
                            , 100+ self.__y + self.__yAnimacion, 20, 15)
        boca.setRelleno(True)
        boca.dibujar(display)

        boca1 = Ovalo()
        boca1.setResolucion(50)
        boca1.setCoordenadas(100 + self.__x + self.__xAnimacion
                             , 95+ self.__y + self.__yAnimacion, 25, 15)
        boca1.setColor((224, 152, 49))
        boca1.setRelleno(True)
        boca1.dibujar(display)

        ojo1 = Ovalo()
        ojo1.setResolucion(20)
        ojo1.setCoordenadas(85 + self.__x + self.__xAnimacion
                            , 90 + self.__y + self.__yAnimacion, 5, 10)
        ojo1.setRelleno(True)
        ojo1.dibujar(display)

        luzOjo1 = Ovalo()
        luzOjo1.setResolucion(20)
        luzOjo1.setCoordenadas(84 + self.__x + self.__xAnimacion
                               , 87 + self.__y + self.__yAnimacion, 2, 3)
        luzOjo1.setColor((255,255,255))
        luzOjo1.setRelleno(True)
        luzOjo1.dibujar(display)

        ojo2 = Ovalo()
        ojo2.setResolucion(20)
        ojo2.setCoordenadas(110 + self.__x + self.__xAnimacion
                            , 90 + self.__y + self.__yAnimacion, 5, 10)
        ojo2.setRelleno(True)
        ojo2.dibujar(display)

        luzOjo2 = Ovalo()
        luzOjo2.setResolucion(20)
        luzOjo2.setCoordenadas(109 + self.__x + self.__xAnimacion
                               , 87 + self.__y + self.__yAnimacion, 2, 3)
        luzOjo2.setColor((255, 255, 255))
        luzOjo2.setRelleno(True)
        luzOjo2.dibujar(display)
