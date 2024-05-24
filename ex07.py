def calcular_produto(dobro_primeiro, metade_segundo):
    return (2*dobro_primeiro) * (0.5*metade_segundo)

def soma_triplo(primeiro, terceiro):
    return (3* primeiro) + terceiro

def terceiro(terceiro):
    return terceiro**3

primeiro_numero = int(input('Digite o primeiro numero inteiro: '))
segundo_numero = int(input('Digite o segundo numero inteiro: '))
terceiro_numero = float(input('Digite o numero real: '))

resultado1 = calcular_produto(primeiro_numero, segundo_numero)
resultado2 = soma_triplo(primeiro_numero, terceiro_numero)
resultado3 = terceiro(terceiro_numero)

print(f'O produto do dobro do primeiro vezes a metade do segundo é {resultado1}')
print(f'A soma do triplo do primeiro com o terceiro é {resultado2}')
print(f'O cubo do terceiro é {resultado3}')