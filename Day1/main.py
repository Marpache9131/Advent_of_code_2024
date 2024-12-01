
def analizar_similitud(lista1, lista2):
    similitud = []
    for num in lista1:
        valor = num * lista2.count(num)
        similitud.append(valor)
    return sum(similitud)

with open("./input.txt") as archivo:
    lista1 = []
    lista2 = []
    for fila in archivo:
        fila = fila.split(" ")

        lista1.append(int(fila[0]))
        lista2.append(int(fila[-1]))
    

lista1.sort()
lista2.sort()

distancias = []

for indice in range(len(lista1)):
    num1 = lista1[indice]
    num2 = lista2[indice]

    distancia = abs(num1 - num2)
    distancias.append(distancia)
print("Parte 1")
print(f"La distancia es: {sum(distancias)}")

similitud_lista_1 = analizar_similitud(lista1=lista1, lista2=lista2)

print(f"La similitud entre las listas es: {similitud_lista_1 }")