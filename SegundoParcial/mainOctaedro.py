import math
import threading
from random import random
import random
from time import sleep

import pygame

from SegundoParcial.Figuras3D import Ejes
from SegundoParcial.Figuras3D.Cubo import Cubo
from SegundoParcial.Figuras3D.Octaedro import Octaedro
from primerParcial.Lienzo.Lienzo import Lienzo
from primerParcial.Figuras.Ovalo import Ovalo

pygame.init()

alto, ancho = 1000, 1000

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Octaedro")

lienzo = Lienzo(ventana)
lienzo.setColor((0,0,0))

ANCHO = 1000
ALTO = 1000
NUM_LUCES = 30   # cantidad de óvalos
RADIO_H = 5
RADIO_V = 10

PALETA = [
    (255, 0, 0),      # rojo
    (255, 120, 0),    # naranja
    (255, 255, 0),    # amarillo
    (0, 255, 0),      # verde
    (0, 200, 255),    # celeste
    (0, 0, 255),      # azul
    (180, 0, 255),    # morado
]

# --- OBJETO PARA CADA LUZ ---
class LuzNavidena:
    def __init__(self):
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.color_index = random.randint(0, len(PALETA)-1)
        self.t = 0                 # fase del efecto respiración
        self.vel = random.uniform(0.03, 0.06)  # velocidad de respiración
        self.estado = "subiendo"   # subiendo = prende, bajando = apaga

        self.ovalo = Ovalo()
        self.ovalo.setCoordenadas(self.x, self.y, RADIO_H, RADIO_V)

    def actualizar(self):
        # Avanzamos el tiempo
        self.t += self.vel

        # Intensidad con sinus (respiración)
        intensidad = (math.sin(self.t) + 1) / 2   # entre 0 y 1

        # Detectar cambio de color al apagarse COMPLETO
        if intensidad < 0.02 and self.estado == "bajando":
            # Cambiar color ANTES de volver a subir
            anterior = self.color_index
            self.color_index = (self.color_index + 1) % len(PALETA)
            self.estado = "subiendo"
            self.t = 0  # reiniciar fase para que suba suave
            intensidad = 0

        # Detectar cuando empieza a bajar
        if intensidad > 0.98:
            self.estado = "bajando"

        r, g, b = PALETA[self.color_index]
        r = int(r * intensidad)
        g = int(g * intensidad)
        b = int(b * intensidad)

        self.ovalo.setColor((r, g, b))


# --- CREAR TODAS LAS LUCES ---
luces = [LuzNavidena() for _ in range(NUM_LUCES)]
for l in luces:
    l.ovalo.setRelleno(True)
    lienzo.add(l.ovalo)

# --- LOOP PRINCIPAL ---
def actualizarLuces():
    while True:
        for l in luces:
            l.actualizar()
        #sleep(.5)
threading.Thread(target=actualizarLuces, daemon=True).start()


def blend(color_a, color_b, t):
    return (
        int(color_a[0] * (1 - t) + color_b[0] * t),
        int(color_a[1] * (1 - t) + color_b[1] * t),
        int(color_a[2] * (1 - t) + color_b[2] * t),
    )

# --- Colores secundarios (figura interna) ---
color_sec_por_tipo = {
    1: (200, 30, 30),    # caja regalo (rojo)
    3: (255, 215, 0),    # estrella (dorado)
    4: (150, 30, 200),   # caja regalo 2 (morado)
    5: (220, 240, 255),  # copo de nieve (azulado)
    6: (230, 60, 140),   # dulce (rosa)
}

# --- Paleta de colores pastel para las figuras externas (octaedros) ---
paleta_cycle = [
    (30, 200, 200),   # cian brillante (contraste del rojo)
    (0, 50, 130),     # azul profundo (contraste del dorado)
    (255, 255, 80),   # amarillo pálido (contraste del morado)
    (30, 50, 120),    # azul marino (contraste del azul claro)
    (50, 230, 100),   # verde menta (contraste del rosa)
    (255, 120, 0),    # naranja vivo (extra contraste cálido)
]

# --- Crear varios octaedros ---
octaedros = []

rows = 3
cols = 3
width, height = 800, 800
margin = 60
size = 160

usable_w = width - 2 * margin
usable_h = height - 2 * margin
spacing_x = usable_w / (cols - 1) if cols > 1 else 0
spacing_y = usable_h / (rows - 1) if rows > 1 else 0

# Ciclo de tipos (sin el árbol navideño, tipo 2)
tipo_seq = [1, 3, 4, 5, 6]
k = 0

for r in range(rows):
    for c in range(cols):
        px = int(margin + c * spacing_x)
        py = int(margin + r * spacing_y)
        pz = 100

        tipo = tipo_seq[k % len(tipo_seq)]
        k += 1

        # Crear el octaedro
        octa = Octaedro(px, py, pz, size, tipo)

        # Color secundario según tipo (figura interna)
        sec_color = color_sec_por_tipo.get(tipo, (255, 255, 0))
        octa.setColorSecundario(sec_color)

        # Color principal inicial (pastel)
        octa.setColor((0,0,0))

        # Rotación inicial en X para apreciarse mejor
        octa.rotacion(Ejes.X, 70)

        lienzo.add(octa)

        # Cada uno tiene una fase distinta en la animación
        fase = (r * cols + c) * (2 * math.pi / (rows * cols))
        octaedros.append({"obj": octa, "fase": fase, "tipo": tipo})

# --- Animación: rotación suave y cambio de color principal pastel ---
def moverCubo():
    fps_sleep = 1 / 60.0
    rotation_speed = 0.6
    color_speed = 0.8
    t = 0.0
    n_pal = len(paleta_cycle)

    while True:
        t += color_speed * fps_sleep

        for info in octaedros:
            octa = info["obj"]
            fase = info["fase"]

            # rotación suave en Y
            octa.rotacion(Ejes.Y, rotation_speed)

            # interpolación circular entre colores pastel
            u = (t + fase) % (2 * math.pi)
            pos = (u / (2 * math.pi)) * n_pal
            idx = int(math.floor(pos)) % n_pal
            next_idx = (idx + 1) % n_pal
            frac = pos - math.floor(pos)

            color_a = paleta_cycle[idx]
            color_b = paleta_cycle[next_idx]
            color_main = blend(color_a, color_b, frac)

            # actualizar color principal
            octa.setColor((0,0,0))
            octa.setRelleno(True, color_main)

        sleep(fps_sleep)

# Hilo de animación
threading.Thread(target=moverCubo, daemon=True).start()

num_copos = 40         # cantidad de cubos (copos)
velocidad_min = 0.8    # velocidad mínima de caída
velocidad_max = 2.2    # velocidad máxima de caída
tamano_copo = 5       # tamaño de lado del cubo

copos = []

# Crear copos (cubos) en posiciones aleatorias arriba de la pantalla
for i in range(num_copos):
    x = random.randint(0, 900)
    y = random.randint(-800, 0)
    z = random.randint(-200, 200)  # para variar profundidad
    vel = random.uniform(velocidad_min, velocidad_max)

    cubo = Cubo(x, y, z, tamano_copo)
    cubo.setColor((255, 255, 255))  # blanco nieve
    cubo.rotacion(Ejes.X, 45)
    cubo.rotacion(Ejes.Y, 45)

    lienzo.add(cubo)
    copos.append({"obj": cubo, "vel": vel})

# --- Hilo para animar los copos (caída constante) ---
def moverNieve():
    fps_sleep = 1 / 60.0
    while True:
        for info in copos:
            cubo = info["obj"]
            vel = info["vel"]

            # Mover el copo hacia abajo
            cubo.traslacion(0, vel, 0)

            # Obtener coordenadas actuales del cubo
            x, y, z = cubo._calcularCentro()

            # Si el copo llegó al fondo, reaparece arriba inmediatamente
            if y < -1200:  # borde inferior de la ventana
                # Reiniciar posición base
                cubo.traslacion(0, -1200, 0)

        sleep(fps_sleep)

# arrancar hilo de copos
threading.Thread(target=moverNieve, daemon=True).start()

# --- Bucle principal ---
inicio = True
while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    lienzo.update()
    pygame.display.update()

pygame.quit()