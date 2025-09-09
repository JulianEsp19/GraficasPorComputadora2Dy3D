def ecuacionDeRecta(punto1, punto2):

    m = (-punto2[1] - (-punto1[1])) / (punto2[0] - punto1[0])

    b = -punto2[1] - m * punto2[0]

    return (m, b)


#Pruebas para scanline
puntosScanline = [(100,100), (200, 100), (200, 200), (100, 200)]
unionesScanline =  [(0, 1), (1, 2), (2, 3), (3, 0)]
scanline = 0
puntoBajo = 800 #dimensiones del display en Y
for i in unionesScanline:
    if puntosScanline[i[0]][1] == puntosScanline[i[1]][1]:
        unionesScanline.remove(i)

    if puntosScanline[i[0]][1] > scanline:
        scanline = puntosScanline[i[0]][1]
    if puntosScanline[i[1]][1] > scanline:
        scanline = puntosScanline[i[1]][1]

    if puntosScanline[i[0]][1] < puntoBajo:
        puntoBajo = puntosScanline[i[0]][1]
    if puntosScanline[i[1]][1] < puntoBajo:
        puntoBajo = puntosScanline[i[1]][1]

# acomodar los puntos de union para que el punto de union con Y mayor quede primero
for i in unionesScanline:
    if puntosScanline[i[0]][1] < puntosScanline[i[1]][1]:
        aux = i[:]
        unionesScanline.remove(i)
        unionesScanline.append((aux[1], aux[0]))

valoresEcuacionDeRecta = []
for i in unionesScanline:
    if puntosScanline[i[0]][0] == puntosScanline[i[1]][0]:
        valoresEcuacionDeRecta.append(False)
    else:
        valoresEcuacionDeRecta.append(ecuacionDeRecta(puntosScanline[i[0]], puntosScanline[i[1]]))

print(unionesScanline)
print(scanline)
print(puntoBajo)
print(valoresEcuacionDeRecta)

numeros = [4, 5, 7, 1]
print(numeros)
numeros.sort()
print(numeros)

for i in range(0, len(numeros), 2):
    print(i)

#en los puntos 0 = X y 1 = Y

