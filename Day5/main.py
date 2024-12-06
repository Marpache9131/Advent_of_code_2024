from collections import defaultdict, deque

def obtener_reglas_validas(reglas, renglon):
    """Filtra las reglas para que solo se usen las que son aplicables al renglón actual."""
    nuevas_reglas = []
    for regla in reglas:
        if regla[0] in renglon and regla[1] in renglon:
            nuevas_reglas.append(regla)
    return nuevas_reglas

def reordenar_renglon(reglas, renglon):
    """Reordena un renglón inválido respetando las reglas aplicables."""
    nuevas_reglas = obtener_reglas_validas(reglas, renglon)

    grafo = defaultdict(list)
    grados = defaultdict(int)
    for regla in nuevas_reglas:
        X, Y = regla
        grafo[X].append(Y)
        grados[Y] += 1
        if X not in grados:
            grados[X] = 0

    cola = deque([nodo for nodo in renglon if grados[nodo] == 0])
    ordenado = []
    while cola:
        actual = cola.popleft()
        ordenado.append(actual)
        for vecino in grafo[actual]:
            grados[vecino] -= 1
            if grados[vecino] == 0:
                cola.append(vecino)

    return ordenado

def analizar_linea(reglas, renglon):
    """Verifica si el renglón cumple las reglas aplicables."""
    nuevas_reglas = obtener_reglas_validas(reglas, renglon)
    for regla in nuevas_reglas:
        indice_num1 = renglon.index(regla[0])
        indice_num2 = renglon.index(regla[1])
        if indice_num1 < indice_num2:
            continue
        else:
            return 0 
    return renglon[len(renglon) // 2] 


reglas = []
renglones = []

with open("./Day5/input.txt") as archivo:
    for linea in archivo:
        if "|" in linea:
            linea = linea.split("|")
            reglas.append([int(linea[0]), int(linea[1])])
        elif len(linea) > 1:
            if "\n" in linea:
                linea = linea[:-1]
            linea = linea.split(",")
            linea = [int(x) for x in linea]
            renglones.append(linea)

suma = 0

for renglon in renglones:
    if analizar_linea(reglas, renglon) == 0:  # Si el renglón es inválido
        renglon_reordenado = reordenar_renglon(reglas, renglon)
        suma += renglon_reordenado[len(renglon_reordenado) // 2]

print(f"Suma páginas reordenadas: {suma}")
