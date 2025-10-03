import pygame
from pygame import SurfaceType

from primerParcial.Figuras.Circulo import Circulo
from primerParcial.Figuras.Cuadrado import Cuadrado
from primerParcial.Figuras.LineaDDA import LineaDDA
from primerParcial.Figuras.Ovalo import Ovalo
from primerParcial.Figuras.Triangulo import Triangulo
from primerParcial.animacion.Personajes.Movimiento import Movimiento


class ZombieCono(Movimiento):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__objetos = []
        self.__superficieAux = pygame.Surface((400, 500), pygame.SRCALPHA)
        self.__iniciarObjetos()

    def __iniciarObjetos(self):

        cabeza = Ovalo()
        cabeza.setResolucion(30)
        cabeza.setCoordenadas(100, 100, 28, 30)
        cabeza.setColor((142, 153, 118))
        cabeza.setRelleno(True)
        self.__objetos.append(cabeza)

        boca = Cuadrado()
        boca.setCoordenadas(75, 115, 110, 125)
        boca.setRelleno(True)
        self.__objetos.append(boca)

        ojo1 = Ovalo()
        ojo1.setResolucion(20)
        ojo1.setCoordenadas(75, 95, 8, 11)
        ojo1.setColor((255,255,255))
        ojo1.setRelleno(True)
        self.__objetos.append(ojo1)

        pupila1 = Ovalo()
        pupila1.setResolucion(10)
        pupila1.setCoordenadas(73, 95, 4, 6)
        pupila1.setRelleno(True)
        self.__objetos.append(pupila1)

        ojo2 = Ovalo()
        ojo2.setResolucion(20)
        ojo2.setCoordenadas(100, 95, 10, 15)
        ojo2.setColor((255,255,255))
        ojo2.setRelleno(True)
        self.__objetos.append(ojo2)

        pupila2 = Ovalo()
        pupila2.setResolucion(10)
        pupila2.setCoordenadas(100, 95, 5, 5)
        pupila2.setRelleno(True)
        self.__objetos.append(pupila2)

        cono = Circulo()
        cono.setResolucion(3)
        cono.setCoordenadas(115, 75, 40)
        cono.calcularPuntos()
        cono.rotacion(-60)
        cono.setColor((255,127, 39))
        cono.setRelleno(True)
        self.__objetos.append(cono)

        cuerpo = Cuadrado()
        cuerpo.setCoordenadas(80, 130, 120, 210)
        cuerpo.setColor((78,50,20))
        cuerpo.setRelleno(True)
        self.__objetos.append(cuerpo)

        brazo1 = Cuadrado()
        brazo1.setCoordenadas(68, 150, 81, 200)
        brazo1.setRelleno(True, (78, 50, 20))
        self.__objetos.append(brazo1)


        brazo2 = Cuadrado()
        brazo2.setCoordenadas(118, 140, 131, 200)
        brazo2.setRelleno(True, (78, 50, 20))
        self.__objetos.append(brazo2)

        corbata = Triangulo()
        corbata.setCoordenadas(90, 140, 110, 190)
        corbata.setColor((237,28,36))
        corbata.setRelleno(True)
        self.__objetos.append(corbata)

        pierna1 = Cuadrado()
        pierna1.setCoordenadas(78, 210, 95, 250)
        pierna1.setColor((65,88,113))
        pierna1.setRelleno(True)
        self.__objetos.append(pierna1)

        pie1 = Cuadrado()
        pie1.setCoordenadas(65, 245, 91, 260)
        pie1.setRelleno(True)
        self.__objetos.append(pie1)

        pierna2 = Cuadrado()
        pierna2.setCoordenadas(105, 208, 120, 250)
        pierna2.setColor((65, 88, 113))
        pierna2.setRelleno(True)
        self.__objetos.append(pierna2)

        pie2 = Cuadrado()
        pie2.setCoordenadas(98, 245, 125, 260)
        pie2.setRelleno(True)
        self.__objetos.append(pie2)

        mano1 = Cuadrado()
        mano1.setCoordenadas(65, 200, 85, 215)
        mano1.setRelleno(True, (142, 153, 118))
        self.__objetos.append(mano1)

        mano1 = Cuadrado()
        mano1.setCoordenadas(115, 200, 135, 210)
        mano1.setRelleno(True, (142, 153, 118))
        self.__objetos.append(mano1)

        for i in self.__objetos:
            i.dibujar(self.__superficieAux)

    def dibujar(self, display:SurfaceType):

        self._verificarMovimiento()

        display.blit(self.__superficieAux, (self._x, self._y))
