from multipledispatch import dispatch
from pygame import SurfaceType


class Pixel():
    def __init__(self):
        self.__color = (0,0,0,255)
        self.__x = 0
        self.__y = 0

    def setCoordenadas(self, x, y):
        self.__x = x
        self.__y = y

    def setColor(self, color):
        self.__color = color

    def dibujar(self, display: SurfaceType):
        display.set_at((self.__x, self.__y), self.__color)