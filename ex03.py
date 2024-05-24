def area_quadrado(lado):
    return lado * lado

calcular_lado = float(input('Digite o comprimento do lado do quadrado: '))
resultado_area = area_quadrado(calcular_lado)
dobro_area = resultado_area * 2

print(f'A area do quadrado é {resultado_area}')
print(f'O dobro da area é {dobro_area}')
