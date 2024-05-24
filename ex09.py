def calcular_pesoidealhomens(h):
    return (72.7*h) -58

def calcular_pesoidealmulher(h):
    return (62.1*h) - 44.7

genero = input('Digite "h" se voce for homem e "m" se for mulher: ')
altura = float(input('Digite sua altura para calcular seu peso ideal: '))
resultadopesoh = calcular_pesoidealhomens(altura)
resultadopesom = calcular_pesoidealmulher(altura)


if genero == 'h':
    print(f'Seu peso ideal é {resultadopesoh}')
elif genero == 'm':
    print(f'Seu peso ideal é {resultadopesom}')
    