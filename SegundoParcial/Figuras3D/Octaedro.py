from pygame import SurfaceType

from SegundoParcial.Figuras3D.__BaseFiguras3D import __BaseFiguras3D
from primerParcial.Figuras.LineaDDA import LineaDDA


class Octaedro(__BaseFiguras3D):

    def __init__(self, x, y, z, lado, figuraInterna):
        super().__init__()
        self._lado = lado
        self._punto1 = (x, -y, z)
        self._figuraInterna = figuraInterna
        self.calcularPuntos()
        self._colorSecundario = 0

    def setColorSecundario(self, color):
        self._colorSecundario = color

    def calcularPuntos(self):
        self.figura3()

        if self._figuraInterna == 1:
            self.figura1()
        elif self._figuraInterna == 2:
            self.figura2()
        elif self._figuraInterna == 3:
            self.figura3()
        elif self._figuraInterna == 4:
            self.figura4()
        elif self._figuraInterna == 5:
            self.figura5()
        elif self._figuraInterna == 6:
            self.figura6()

        self._proyectar()

    def _pintarPuntos(self, display: SurfaceType):

        linea = LineaDDA()
        linea.setColor(self._color)

        if not len(self._puntosScanline):
            return
        contador = 0
        for i in self._unionesScanline:
            linea.setCoordenadas(self._puntosScanline[i[0]], self._puntosScanline[i[1]])
            linea.dibujar(display)
            contador += 1
            if contador > 11:
                linea.setColor(self._colorSecundario)

        self.pintando = False

    def figura6(self):
        import math

        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2.0

        # ---------- TETRAEDRO BASE ----------
        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1), (0, 2), (2, 3), (1, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
            (0, 5), (1, 5), (2, 5), (3, 5),
        ]

        # ---------- FIGURA INTERNA: CAMPANA 3D ORIENTADA Y ESCALADA ----------
        centroX = x + puntoMedio
        centroY = y - puntoMedio
        centroZ = z

        # proporciones dependientes de self._lado
        altura = self._lado * 0.5
        radio_superior = self._lado * 0.10
        radio_inferior = self._lado * 0.25
        profundidad = self._lado * 0.10
        num_segmentos = 8

        indiceBase = len(self._puntos3D)
        puntos_campana = []
        uniones_campana = []

        # ---------- Cuerpo de la campana ----------
        # NOTA: en tu sistema, “abajo” es hacia (y +)
        y_top = centroY - altura * 0.25  # parte superior (más cercana al vértice superior del tetraedro)
        y_bottom = centroY + altura * 0.25  # boca de la campana (mirando hacia el fondo del tetraedro)

        # círculo superior (borde angosto)
        for i in range(num_segmentos):
            ang = (2 * math.pi / num_segmentos) * i
            px = centroX + radio_superior * math.cos(ang)
            pz = centroZ + radio_superior * math.sin(ang)
            puntos_campana.append((px, y_top, pz))

        # círculo inferior (borde ancho)
        for i in range(num_segmentos):
            ang = (2 * math.pi / num_segmentos) * i
            px = centroX + radio_inferior * math.cos(ang)
            pz = centroZ + radio_inferior * math.sin(ang)
            puntos_campana.append((px, y_bottom, pz))

        # punto superior (tope)
        puntos_campana.append((centroX, y_top - profundidad * 0.5, centroZ))

        # círculo interno (clavo)
        num_interno = 6
        radio_interno = radio_inferior * 0.25
        y_interno = y_bottom - profundidad * 0.4
        for i in range(num_interno):
            ang = (2 * math.pi / num_interno) * i
            px = centroX + radio_interno * math.cos(ang)
            pz = centroZ + radio_interno * math.sin(ang)
            puntos_campana.append((px, y_interno, pz))

        # añadir puntos
        self._puntos3D += puntos_campana

        # ---------- UNIONES ----------
        # conectar entre anillos y hacia la punta superior
        for i in range(num_segmentos):
            idx_sup = indiceBase + i
            idx_inf = indiceBase + num_segmentos + i
            next_sup = indiceBase + (i + 1) % num_segmentos
            next_inf = indiceBase + num_segmentos + (i + 1) % num_segmentos

            # círculos
            uniones_campana.append((idx_sup, next_sup))
            uniones_campana.append((idx_inf, next_inf))

            # uniones verticales
            uniones_campana.append((idx_sup, idx_inf))

        # unir punto superior con el anillo superior
        idx_top = indiceBase + num_segmentos * 2
        for i in range(num_segmentos):
            uniones_campana.append((idx_top, indiceBase + i))

        # unir círculo interno (clavo)
        start_inner = idx_top + 1
        for i in range(num_interno):
            idx = start_inner + i
            next_idx = start_inner + (i + 1) % num_interno
            uniones_campana.append((idx, next_idx))
            # colgar del borde inferior
            uniones_campana.append((idx, indiceBase + num_segmentos + (i * 2) % num_segmentos))

        # añadir uniones
        self._uniones3D += uniones_campana

    def figura5(self):

        import math

        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2.0

        # ---------- TETRAEDRO BASE (mantener tal cual) ----------
        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1), (0, 2), (2, 3), (1, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
            (0, 5), (1, 5), (2, 5), (3, 5),
        ]

        # ---------- FIGURA INTERNA: COPO DE NIEVE 3D (ESCALADO CON self._lado) ----------
        centroX = x + puntoMedio
        centroY = y - puntoMedio
        centroZ = z

        # parámetros dependientes de self._lado
        r_outer = self._lado * 0.28  # radio exterior de las puntas
        r_mid = r_outer * 0.55  # radio medio interno
        r_core = r_outer * 0.18  # nucleo pequeño
        depth = self._lado * 0.10  # variación en Y para dar 3D (profundidad)
        spike_len = self._lado * 0.12  # pequeñas puntas secundarias

        indiceBase = len(self._puntos3D)

        puntos_copo = []
        uniones_copo = []

        # núcleo (centro)
        puntos_copo.append((centroX, centroY, centroZ))  # índice indiceBase + 0

        # generar 6 brazos (hexagonal) con 3 nodos por brazo: inner -> outer -> tip (con variación Y para volumen)
        for i in range(6):
            ang = math.radians(i * 60)
            cos_a = math.cos(ang)
            sin_a = math.sin(ang)

            # punto medio cercano al centro
            px_mid = centroX + r_mid * cos_a
            pz_mid = centroZ + r_mid * sin_a
            py_mid = centroY + ((-1) ** i) * (depth * 0.15)  # alterna altura ligera para 3D
            puntos_copo.append((px_mid, py_mid, pz_mid))

            # punto exterior (más profundo/alto para dar volumen)
            px_out = centroX + r_outer * cos_a
            pz_out = centroZ + r_outer * sin_a
            py_out = centroY + ((-1) ** (i + 1)) * (depth * 0.25)
            puntos_copo.append((px_out, py_out, pz_out))

            # punta final (pequeña extensión)
            px_tip = centroX + (r_outer + spike_len) * cos_a
            pz_tip = centroZ + (r_outer + spike_len) * sin_a
            py_tip = centroY + ((-1) ** i) * (depth * 0.35)
            puntos_copo.append((px_tip, py_tip, pz_tip))

        # Añadir algunos nodos de cruce para estructura interior (profundidad en Z/Y)
        # arriba y abajo del núcleo
        puntos_copo.append((centroX, centroY + depth * 0.6, centroZ))  # arriba
        puntos_copo.append((centroX, centroY - depth * 0.6, centroZ))  # abajo

        # añadir puntos al arreglo principal
        self._puntos3D += puntos_copo

        # Construir las uniones:
        # 1) del núcleo a cada punto medio (cada brazo)
        num_puntos_por_brazo = 3
        for i in range(6):
            idx_mid = indiceBase + 1 + i * num_puntos_por_brazo
            idx_out = idx_mid + 1
            idx_tip = idx_mid + 2
            idx_core = indiceBase + 0

            # núcleo -> medio -> exterior -> punta
            uniones_copo.append((idx_core, idx_mid))
            uniones_copo.append((idx_mid, idx_out))
            uniones_copo.append((idx_out, idx_tip))

            # conexiones laterales para formar la estrella (outer ring)
            next_out = indiceBase + 1 + ((i + 1) % 6) * num_puntos_por_brazo + 1
            uniones_copo.append((idx_out, next_out))

            # conexiones cruzadas medios con otros medios (refuerzo)
            next_mid = indiceBase + 1 + ((i + 2) % 6) * num_puntos_por_brazo
            uniones_copo.append((idx_mid, next_mid))

        # 2) unir los nodos arriba/abajo con núcleos de brazos para dar volumen vertical
        idx_arriba = indiceBase + 1 + 6 * num_puntos_por_brazo
        idx_abajo = idx_arriba + 1
        for i in range(6):
            idx_mid = indiceBase + 1 + i * num_puntos_por_brazo
            uniones_copo.append((idx_mid, idx_arriba))
            uniones_copo.append((idx_mid, idx_abajo))

        # 3) unión entre arriba y abajo para eje vertical
        uniones_copo.append((idx_arriba, idx_abajo))

        # finalmente añadir las uniones al arreglo principal
        self._uniones3D += uniones_copo

    def figura4(self):
        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2

        # ---------- TETRAEDRO BASE ----------
        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1), (0, 2), (2, 3), (1, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
            (0, 5), (1, 5), (2, 5), (3, 5),
        ]

        # ---------- FIGURA INTERNA: REGALO 3D ----------
        centroX = x + puntoMedio
        centroY = y - puntoMedio
        centroZ = z
        lado_caja = self._lado / 3

        indiceBase = len(self._puntos3D)

        # Caja cúbica
        p0 = (centroX - lado_caja / 2, centroY + lado_caja / 2, centroZ - lado_caja / 2)
        p1 = (centroX + lado_caja / 2, centroY + lado_caja / 2, centroZ - lado_caja / 2)
        p2 = (centroX + lado_caja / 2, centroY - lado_caja / 2, centroZ - lado_caja / 2)
        p3 = (centroX - lado_caja / 2, centroY - lado_caja / 2, centroZ - lado_caja / 2)
        p4 = (centroX - lado_caja / 2, centroY + lado_caja / 2, centroZ + lado_caja / 2)
        p5 = (centroX + lado_caja / 2, centroY + lado_caja / 2, centroZ + lado_caja / 2)
        p6 = (centroX + lado_caja / 2, centroY - lado_caja / 2, centroZ + lado_caja / 2)
        p7 = (centroX - lado_caja / 2, centroY - lado_caja / 2, centroZ + lado_caja / 2)

        puntos_caja = [p0, p1, p2, p3, p4, p5, p6, p7]

        uniones_caja = [
            (indiceBase + 0, indiceBase + 1),
            (indiceBase + 1, indiceBase + 2),
            (indiceBase + 2, indiceBase + 3),
            (indiceBase + 3, indiceBase + 0),
            (indiceBase + 4, indiceBase + 5),
            (indiceBase + 5, indiceBase + 6),
            (indiceBase + 6, indiceBase + 7),
            (indiceBase + 7, indiceBase + 4),
            (indiceBase + 0, indiceBase + 4),
            (indiceBase + 1, indiceBase + 5),
            (indiceBase + 2, indiceBase + 6),
            (indiceBase + 3, indiceBase + 7),
        ]

        # ---------- MOÑO SUPERIOR (dos lazos curvos simplificados con aristas) ----------
        radio_moño = lado_caja / 3
        altura_moño = lado_caja / 2
        cx = centroX
        cy = centroY + lado_caja / 2
        cz = centroZ

        # Nodos del moño
        p8 = (cx, cy + altura_moño / 2, cz)
        p9 = (cx - radio_moño, cy + altura_moño / 3, cz - radio_moño)
        p10 = (cx + radio_moño, cy + altura_moño / 3, cz - radio_moño)
        p11 = (cx - radio_moño, cy + altura_moño / 3, cz + radio_moño)
        p12 = (cx + radio_moño, cy + altura_moño / 3, cz + radio_moño)

        puntos_moño = [p8, p9, p10, p11, p12]

        indiceMoño = indiceBase + len(puntos_caja)

        uniones_moño = [
            (indiceMoño + 0, indiceMoño + 1),
            (indiceMoño + 0, indiceMoño + 2),
            (indiceMoño + 0, indiceMoño + 3),
            (indiceMoño + 0, indiceMoño + 4),
            (indiceMoño + 1, indiceMoño + 3),
            (indiceMoño + 2, indiceMoño + 4),
        ]

        # Añadir todo
        self._puntos3D += puntos_caja + puntos_moño
        self._uniones3D += uniones_caja + uniones_moño

    def figura3(self):
        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2

        # ---------- TETRAEDRO BASE ----------
        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1), (0, 2), (2, 3), (1, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
            (0, 5), (1, 5), (2, 5), (3, 5),
        ]

        # ---------- FIGURA INTERNA: ESTRELLA 3D ----------
        centroX = x + puntoMedio
        centroY = y - puntoMedio
        centroZ = z
        radio = self._lado / 4

        indiceBase = len(self._puntos3D)

        # Núcleo (centro de la estrella)
        p0 = (centroX, centroY, centroZ)

        # Puntas de la estrella en los ejes principales (6 direcciones)
        p1 = (centroX + radio, centroY, centroZ)  # +X
        p2 = (centroX - radio, centroY, centroZ)  # -X
        p3 = (centroX, centroY + radio, centroZ)  # +Y
        p4 = (centroX, centroY - radio, centroZ)  # -Y
        p5 = (centroX, centroY, centroZ + radio)  # +Z
        p6 = (centroX, centroY, centroZ - radio)  # -Z

        # Puntas diagonales (para dar volumen y aspecto de estrella)
        d = radio / 1.4
        p7 = (centroX + d, centroY + d, centroZ + d)
        p8 = (centroX - d, centroY + d, centroZ + d)
        p9 = (centroX + d, centroY - d, centroZ + d)
        p10 = (centroX - d, centroY - d, centroZ + d)
        p11 = (centroX + d, centroY + d, centroZ - d)
        p12 = (centroX - d, centroY + d, centroZ - d)
        p13 = (centroX + d, centroY - d, centroZ - d)
        p14 = (centroX - d, centroY - d, centroZ - d)

        puntos_estrella = [p0, p1, p2, p3, p4, p5, p6,
                           p7, p8, p9, p10, p11, p12, p13, p14]

        # Uniones (líneas desde el centro hacia las puntas)
        uniones_estrella = [
            (indiceBase + 0, indiceBase + i) for i in range(1, len(puntos_estrella))
        ]

        # También unimos puntas opuestas entre sí para darle estructura
        uniones_estrella += [
            (indiceBase + 1, indiceBase + 2),
            (indiceBase + 3, indiceBase + 4),
            (indiceBase + 5, indiceBase + 6),
            (indiceBase + 7, indiceBase + 14),
            (indiceBase + 8, indiceBase + 13),
            (indiceBase + 9, indiceBase + 12),
            (indiceBase + 10, indiceBase + 11),
        ]

        # Añadir todo
        self._puntos3D += puntos_estrella
        self._uniones3D += uniones_estrella

    def figura2(self):
        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2

        # ---------- TETRAEDRO BASE ----------
        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1), (0, 2), (2, 3), (1, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
            (0, 5), (1, 5), (2, 5), (3, 5),
        ]

        # ---------- FIGURA INTERNA: ÁRBOL DE NAVIDAD 3D ----------
        centroX = x + puntoMedio
        centroY = y - puntoMedio
        centroZ = z
        escala = self._lado / 4.5

        indiceBase = len(self._puntos3D)

        # 3 niveles de pirámides
        niveles = 3
        altura_nivel = escala / 1.5

        puntos_arbol = []
        uniones_arbol = []

        for i in range(niveles):
            s = escala - i * (escala / 3)
            altura = i * altura_nivel
            y_nivel = centroY - altura

            # Base cuadrada del nivel
            p0 = (centroX - s, y_nivel - s, centroZ - s)
            p1 = (centroX + s, y_nivel - s, centroZ - s)
            p2 = (centroX + s, y_nivel - s, centroZ + s)
            p3 = (centroX - s, y_nivel - s, centroZ + s)
            # Punta
            p4 = (centroX, y_nivel + s, centroZ)

            base_i = indiceBase + len(puntos_arbol)
            puntos_arbol += [p0, p1, p2, p3, p4]

            uniones_arbol += [
                (base_i + 0, base_i + 1),
                (base_i + 1, base_i + 2),
                (base_i + 2, base_i + 3),
                (base_i + 3, base_i + 0),
                (base_i + 0, base_i + 4),
                (base_i + 1, base_i + 4),
                (base_i + 2, base_i + 4),
                (base_i + 3, base_i + 4),
            ]

        # ---------- TRONCO CENTRADO ----------
        altura_tronco = escala / 3
        base_tronco = escala / 5

        # Posición ajustada justo debajo del último nivel
        y_base_ultimo_nivel = centroY - (niveles - 1) * altura_nivel - escala
        y_tronco_superior = y_base_ultimo_nivel - base_tronco / 2
        y_tronco_inferior = y_tronco_superior - altura_tronco

        puntos_tronco = [
            (centroX - base_tronco, y_tronco_superior, centroZ - base_tronco),
            (centroX + base_tronco, y_tronco_superior, centroZ - base_tronco),
            (centroX + base_tronco, y_tronco_superior, centroZ + base_tronco),
            (centroX - base_tronco, y_tronco_superior, centroZ + base_tronco),
            (centroX - base_tronco, y_tronco_inferior, centroZ - base_tronco),
            (centroX + base_tronco, y_tronco_inferior, centroZ - base_tronco),
            (centroX + base_tronco, y_tronco_inferior, centroZ + base_tronco),
            (centroX - base_tronco, y_tronco_inferior, centroZ + base_tronco),
        ]

        indice_tronco = indiceBase + len(puntos_arbol)
        puntos_arbol += puntos_tronco

        uniones_tronco = [
            (indice_tronco + 0, indice_tronco + 1),
            (indice_tronco + 1, indice_tronco + 2),
            (indice_tronco + 2, indice_tronco + 3),
            (indice_tronco + 3, indice_tronco + 0),
            (indice_tronco + 4, indice_tronco + 5),
            (indice_tronco + 5, indice_tronco + 6),
            (indice_tronco + 6, indice_tronco + 7),
            (indice_tronco + 7, indice_tronco + 4),
            (indice_tronco + 0, indice_tronco + 4),
            (indice_tronco + 1, indice_tronco + 5),
            (indice_tronco + 2, indice_tronco + 6),
            (indice_tronco + 3, indice_tronco + 7),
        ]

        # Añadir todo
        self._puntos3D += puntos_arbol
        self._uniones3D += uniones_arbol + uniones_tronco

    def figura1(self):
        x = self._punto1[0]
        y = self._punto1[1]
        z = self._punto1[2]

        puntoMedio = self._lado / 2

        # ---------- TETRAEDRO ORIGINAL ----------
        self._puntos3D = [
            (x, y, z),
            (x, y - self._lado, z),
            (x + self._lado, y, z),
            (x + self._lado, y - self._lado, z),
            (x + puntoMedio, y - puntoMedio, z + self._lado),
            (x + puntoMedio, y - puntoMedio, z - self._lado),
        ]

        self._uniones3D = [
            (0, 1), (0, 2), (2, 3), (1, 3),
            (0, 4), (1, 4), (2, 4), (3, 4),
            (0, 5), (1, 5), (2, 5), (3, 5),
        ]

        # ---------- FIGURA INTERNA: CAJA DE REGALO 3D ----------
        centroX = x + puntoMedio
        centroY = y - puntoMedio
        centroZ = z
        escala = self._lado / 4.5  # tamaño dentro del tetraedro

        indiceBase = len(self._puntos3D)

        # 8 vértices del cubo (la caja)
        puntos_caja = [
            (centroX - escala, centroY + escala, centroZ - escala),  # 0 sup izq atrás
            (centroX + escala, centroY + escala, centroZ - escala),  # 1 sup der atrás
            (centroX - escala, centroY - escala, centroZ - escala),  # 2 inf izq atrás
            (centroX + escala, centroY - escala, centroZ - escala),  # 3 inf der atrás
            (centroX - escala, centroY + escala, centroZ + escala),  # 4 sup izq frente
            (centroX + escala, centroY + escala, centroZ + escala),  # 5 sup der frente
            (centroX - escala, centroY - escala, centroZ + escala),  # 6 inf izq frente
            (centroX + escala, centroY - escala, centroZ + escala),  # 7 inf der frente
        ]

        # 4 vértices extra del moño (arriba)
        altura_moño = escala / 2.2
        puntos_moño = [
            (centroX, centroY + escala + altura_moño, centroZ),  # 8 centro moño
            (centroX - escala / 2, centroY + escala + altura_moño / 2, centroZ - escala / 3),  # 9 ala izq
            (centroX + escala / 2, centroY + escala + altura_moño / 2, centroZ - escala / 3),  # 10 ala der
            (centroX, centroY + escala + altura_moño / 2, centroZ + escala / 3),  # 11 ala frente
        ]

        self._puntos3D += puntos_caja + puntos_moño

        # UNIONES DE LA CAJA (12 aristas)
        uniones_caja = [
            # base trasera
            (indiceBase + 0, indiceBase + 1),
            (indiceBase + 1, indiceBase + 3),
            (indiceBase + 3, indiceBase + 2),
            (indiceBase + 2, indiceBase + 0),

            # base delantera
            (indiceBase + 4, indiceBase + 5),
            (indiceBase + 5, indiceBase + 7),
            (indiceBase + 7, indiceBase + 6),
            (indiceBase + 6, indiceBase + 4),

            # columnas
            (indiceBase + 0, indiceBase + 4),
            (indiceBase + 1, indiceBase + 5),
            (indiceBase + 2, indiceBase + 6),
            (indiceBase + 3, indiceBase + 7),
        ]

        # UNIONES DE LA CINTA (cruz arriba y frente)
        uniones_cinta = [
            # cinta vertical al frente
            (indiceBase + 4, indiceBase + 6),
            (indiceBase + 5, indiceBase + 7),
            # cinta horizontal superior
            (indiceBase + 0, indiceBase + 4),
            (indiceBase + 1, indiceBase + 5),
        ]

        # UNIONES DEL MOÑO
        uniones_moño = [
            (indiceBase + 8, indiceBase + 9),
            (indiceBase + 8, indiceBase + 10),
            (indiceBase + 8, indiceBase + 11),
            (indiceBase + 9, indiceBase + 10),
            (indiceBase + 9, indiceBase + 11),
            (indiceBase + 10, indiceBase + 11),
        ]

        # AÑADIR TODO
        self._uniones3D += uniones_caja + uniones_cinta + uniones_moño
