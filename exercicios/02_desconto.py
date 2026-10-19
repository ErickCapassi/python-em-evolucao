def calcular_desconto(a, b):
    desconto = (a * b) / 100
    final = a - desconto
    return final


total = int(input('Digite o preço: '))
percentual = float(input('Digite a porcentagem de desconto: '))

preco_final = calcular_desconto(total, percentual)
print(f'O preço final descontando {percentual}% de {total} é {preco_final}')
