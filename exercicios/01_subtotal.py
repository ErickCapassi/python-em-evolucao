def calcular_subtotal(quantidade, preco):
    valor_total = quantidade * preco
    return valor_total


quantidade = int(input('Digite a quantidade: '))
preco = float(input('Digite o preço: '))

valor_total = calcular_subtotal(quantidade, preco)
print(f'O preço final multiplicando {quantidade} e {preco} é {valor_total}')
