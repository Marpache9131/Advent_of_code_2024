
def es_seguro(registro):
    # 2 Condiciones se tienen que cumplir
    # 1. Toda la lista tiene que ser asencente o decendente
    # 2. los 2 numeros adjacentes deben de ser diferentes por minimo 1 o maximo 3

    print(registro)
    print(sorted(registro) == registro)
    print(sorted(registro, reverse=True)==registro)

    # Revisar que esté ordenado acendente o decendente
    if sorted(registro) == registro or sorted(registro,reverse=True) == registro:
        pass
    else:
        return 0
    
    for item in range(1, len(registro)):
        
        
        if registro[item] == registro[item-1]:
            return 0
        diferencia = abs(registro[item] - registro[item-1])
        if  diferencia >= 1 and diferencia <=3:
            continue
        else:
            return 0
    
    return 1

def es_seguro_parte_2(registro):
    # 3 Condiciones se tienen que cumplir
    # 1. Toda la lista tiene que ser asencente o decendente
    # 2. los 2 numeros adjacentes deben de ser diferentes por minimo 1 o maximo 3
    # 3. Tolerancia a 1 error

    if es_seguro(registro):
        return 1

    for i in range(len(registro)):
        registro_modificado = registro[:i] + registro[i+1:]
        if es_seguro(registro_modificado):
            return 1

    return 0


registros = []
with open("./input copy.txt") as archivo:
    for fila in archivo:
        fila = fila.split(" ")
        fila = list(map(int, fila))
        registros.append(fila)

conteo = 0
for registro in registros:
    valor = es_seguro(registro=registro)
    conteo += valor

print(f"Registros seguros: {conteo}")

conteo = 0
for registro in registros:
    valor = es_seguro_parte_2(registro=registro)
    conteo += valor

print(f"Registros seguros parte 2: {conteo}")
