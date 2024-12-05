
lineas = []
with open("./Day4/input.txt") as archivo:
    for linea in archivo:
        if "\n" in linea:
            linea = linea[:-1]
        lineas.append(linea)

largo = len(lineas)
ancho = len(lineas[0])

print(f"Largo = {largo}")
print(f"Ancho = {ancho}")

contador = 0
for y in range(len(lineas)):
    for x in range(len(lineas[y])):
        #print(f"Coordenadas x:{x}, y:{y}")
        # Buscar derecha
        if x + 3 < ancho:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y][x+1]}, {lineas[y][x+2]}, {lineas[y][x+3]}")
            if (lineas[y][x] == "X") and (lineas[y][x+1] == "M") and (lineas[y][x+2] == "A") and (lineas[y][x+3] == "S"):
                contador += 1

        # Abajo Derecha
        if x + 3 < ancho and y + 3 < largo:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y+1][x+1]}, {lineas[y+2][x+2]}, {lineas[y+3][x+3]}")
            if (lineas[y][x] == "X") and (lineas[y+1][x+1] == "M") and (lineas[y+2][x+2] == "A") and (lineas[y+3][x+3] == "S"):
                contador += 1
        
        # Abajo
        if y + 3 < largo:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y+1][x]}, {lineas[y+2][x]}, {lineas[y+3][x]}")

            if (lineas[y][x] == "X") and (lineas[y+1][x] == "M") and (lineas[y+2][x] == "A") and (lineas[y+3][x] == "S"):
                contador += 1

        # Abajo Izquierda
        if x - 3 >= 0 and y + 3 < largo:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y+1][x-1]}, {lineas[y+2][x-2]}, {lineas[y+3][x-3]}")
            
            if (lineas[y][x] == "X") and (lineas[y+1][x-1] == "M") and (lineas[y+2][x-2] == "A") and (lineas[y+3][x-3] == "S"):
                contador += 1

        # Izquierda
        if x - 3 >= 0:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y][x-1]}, {lineas[y][x-2]}, {lineas[y][x-3]}")
            
            if (lineas[y][x] == "X") and (lineas[y][x-1] == "M") and (lineas[y][x-2] == "A") and (lineas[y][x-3] == "S"):
                contador += 1

        # Arriba Izquierda
        if x - 3 >= 0 and y - 3 >= 0:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y-1][x-1]}, {lineas[y-2][x-2]}, {lineas[y-3][x-3]}")
    
            if (lineas[y][x] == "X") and (lineas[y-1][x-1] == "M") and (lineas[y-2][x-2] == "A") and (lineas[y-3][x-3] == "S"):
                contador += 1

        # Arriba
        if y - 3 >= 0:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y-1][x]}, {lineas[y-2][x]}, {lineas[y-3][x]}")
            
            if (lineas[y][x] == "X") and (lineas[y-1][x] == "M") and (lineas[y-2][x] == "A") and (lineas[y-3][x] == "S"):
                contador += 1

        # Arriba Derecha
        if y - 3 >= 0 and x + 3 < ancho:
            #print(f"Letras encontradas: {lineas[y][x]}, {lineas[y-1][x+1]}, {lineas[y-2][x+2]}, {lineas[y-3][x+3]}")
            
            if (lineas[y][x] == "X") and (lineas[y-1][x+1] == "M") and (lineas[y-2][x+2] == "A") and (lineas[y-3][x+3] == "S"):
                contador += 1

# Parte 2
contador2 = 0
for y in range(len(lineas)):
    for x in range(len(lineas[y])):

        if lineas[y][x] == "A" and x+1 < ancho and x-1 >= 0 and y + 1 < largo and y - 1 >= 0:
            if (((lineas[y-1][x-1] == "M") and (lineas[y+1][x+1] == "S") or (lineas[y-1][x-1] == "S") and (lineas[y+1][x+1] == "M")) and ((lineas[y+1][x-1] == "M") and (lineas[y-1][x+1] == "S") or (lineas[y+1][x-1] == "S") and (lineas[y-1][x+1] == "M"))):
                contador2 +=1
        
print(f"XMAS encontrados parte 1: {contador}")

print(f"XMAS encontrados parte 2: {contador2}")