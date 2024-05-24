def calcular_pesoideal(altura):
    return (72.7*altura) - 58

altura = float(input('Digite sua altura para saber seu peso ideal: '))
resultado = calcular_pesoideal(altura)
print(f'Seu peso ideal é {resultado:.2f}')