def calcular_subtotal(a, b):
    valor_total = a * b
    return valor_total


def calcular_desconto(a, b):
    desconto = (a * b) / 100
    final = a - desconto
    return final


total = float(input('Digite o preço: '))
quantidade = int(input('Digite a quantidade de itens: '))
percentual = float(input('Digite a porcentagem de desconto: '))

valor_subtotal = calcular_subtotal(total, quantidade)
preco_final = calcular_desconto(valor_subtotal, percentual)

print(f'O preço final descontando {percentual}% de {valor_subtotal} é {preco_final}')
