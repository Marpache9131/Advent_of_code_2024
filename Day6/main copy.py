
mapa = []
pos_x = -1
pos_y = -1
with open("./Day6/input.txt") as archivo:
    for linea in archivo:
        encontrado = False
        if "\n" in linea:
            linea = linea[:-1]
        if "^" in linea:
            pos_x = linea.index("^")
            encontrado = True
        
        mapa.append(linea)
        if encontrado:
            pos_y = len(mapa)-1

arriba = True
abajo = False
izquierda = False
derecha = False


ubicaciones = []
unicos = []
bucles = 0

moviendo = True
while moviendo:
    if [pos_x, pos_y,arriba,abajo,izquierda,derecha] not in ubicaciones:
        ubicaciones.append([pos_x,pos_y,arriba,abajo,izquierda,derecha])

    if [pos_x,pos_y] not in unicos:
        unicos.append([pos_x,pos_y])
    if arriba:
        # Revisar si ya salió
        if pos_y - 1 == -1:
            moviendo = False
            continue
        # Revisar si hay obstaculo
        elif mapa[pos_y-1][pos_x] == "#":
            arriba = False
            derecha = True
            pos_x = pos_x
            pos_y = pos_y
            continue
        # Revisar si está libre
        elif mapa[pos_y - 1][pos_x] == "." or mapa[pos_y - 1][pos_x] == "^":
            if [pos_x+1, pos_y,False,False,False,True] in ubicaciones:
                bucles += 1
            pos_x = pos_x
            pos_y = pos_y - 1
            continue
    
    elif derecha:
        if pos_x + 1 == len(mapa[0]):
            moviendo = False
            continue
        
        elif mapa[pos_y][pos_x + 1] == "#":
            derecha = False
            abajo = True
            pos_x = pos_x
            pos_y = pos_y
            continue
            
        elif mapa[pos_y][pos_x + 1]== "." or mapa[pos_y][pos_x + 1] == "^":
            if [pos_x, pos_y + 1,False,True,False,False] in ubicaciones:
                bucles += 1
            pos_x = pos_x + 1
            pos_y = pos_y
            continue
        
    elif abajo:
        if pos_y + 1 == len(mapa):
            moviendo = False
            continue
            
        elif mapa[pos_y + 1][pos_x] == "#":
            abajo = False
            izquierda = True
            pos_x = pos_x
            pos_y = pos_y
            continue

        elif mapa[pos_y + 1][pos_x] == "." or mapa[pos_y + 1][pos_x] == "^":
            if [pos_x - 1, pos_y,False,False,True,False] in ubicaciones:
                bucles += 1
            pos_x = pos_x
            pos_y = pos_y + 1
            continue
        
    elif izquierda:
        if pos_x - 1 == -1:
            moviendo = False
            continue
        elif mapa[pos_y][pos_x - 1] == "#":
            izquierda = False
            arriba = True
            pos_x = pos_x
            pos_y = pos_y
            continue
        elif mapa[pos_y][pos_x - 1] == "." or mapa[pos_y][pos_x - 1] == "^":
            if [pos_x, pos_y-1,True,False,False,False] in ubicaciones:
                bucles += 1
            pos_x = pos_x - 1
            pos_y = pos_y
            continue

print(f"Movimientos unicos: {len(unicos)}")
print(f"Posibles bucles: {bucles}")