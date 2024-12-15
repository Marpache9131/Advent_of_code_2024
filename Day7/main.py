from itertools import product

datos = []

def evaluar_resultado(numeros, operadores):
    res = 0
    for i, operador in enumerate(operadores):
        if res == 0:
            if operador == "+":
                res = int(numeros[i]) + int(numeros[1+i])
            elif operador == "*":
                res = int(numeros[i]) * int(numeros[1+i])
            elif operador == "||":
                res = int(numeros[i]+numeros[i+1])
        elif operador == "+":
            res += int(numeros[i+1])
        
        elif operador == "*":
            res *= int(numeros[i+1])
        
        elif operador == "||":
            res = int(f"{res}{numeros[i+1]}")

    return res 


with open("./Day7/input.txt") as archivo:
    for linea in archivo:
        linea = linea.split()
        resultado = linea.pop(0)
        resultado = int(resultado[:-1])
        datos.append([resultado, linea])

suma = 0
for dato in datos:
    viable = False
    operadores_necesarios = len(dato[1])-1
    for ops in product(["*","+","||"], repeat=operadores_necesarios):
        possible_result = evaluar_resultado(dato[1], ops)

        if possible_result == dato[0]:
            viable = True
    if viable:
        suma += dato[0]

print(f"Valor de calibración: {suma}")