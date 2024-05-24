import math

def calcular_area(raio):
    area = math.pi * raio**2
    return area

raio_circulo = float(input('Digite o raio do círculo: '))
area_do_circulo = calcular_area(raio_circulo)
print("A área do círculo é:", area_do_circulo)
