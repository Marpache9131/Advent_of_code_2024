import re

def analizar_linea(linea):
    patron = r"mul\((\d{1,3}),(\d{1,3})\)"
    coincidencias = re.finditer(pattern=patron, string=linea)

    suma = 0

    for coincidencia in coincidencias:
        num1, num2 = coincidencia.group(1), coincidencia.group(2)
        valor = int(num1) * int(num2)
        suma += valor
    
    return suma

def analizar_linea_2(linea):
    patron = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    coincidencias = re.finditer(pattern=patron, string=linea)

    suma = 0
    hacer = True

    for coincidencia in coincidencias:
        print(coincidencia)
        if coincidencia.group(0) == "do()":
            hacer = True
            print("Hacer ahora es Verdadero")
            continue
        elif coincidencia.group(0) == "don't()":
            hacer = False
            print("Hacer ahora es Falso")
            continue
        
        if hacer:
            num1, num2 = coincidencia.group(1), coincidencia.group(2)
            print(f"Valores a multiplicar: {num1} y {num2}")
            valor = int(num1) * int(num2)
            suma += valor
            
    return suma

total_1 = 0
total_2 = 0
with open("./Day3/input.txt") as archivo:
    for linea in archivo:
        valor_1 = analizar_linea(linea=linea)
        total_1 += valor_1

        valor_2 = analizar_linea_2(linea=linea)
        total_2 += valor_2

print(f"Suma total Parte 1: {total_1}")
print(f"Suma total Parte 2: {total_2}")
