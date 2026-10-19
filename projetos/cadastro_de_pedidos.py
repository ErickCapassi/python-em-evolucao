produtos = []
quantidades = []
valores = []
Outro_Produto = 1

print('=' * 20)
print('CADASTRO DE PEDIDOS')
print('=' * 20)

nome = input('Digite o seu nome: ')
print(f'\nOlá {nome}, ficamos felizes em ter você em nossa loja.')

while Outro_Produto == 1:
    while True:
        produto = input('Qual produto está na mira de hoje?\n')
        produtos.append(produto)
        break

    while True:
        try:
            quantidade = int(input(
                f'\nÓtima escolha, o(a) {produto} sai muito!'
                f'\nQuantos você pretende levar, {nome}?\n'
            ))
        except ValueError:
            print('\nDigite um número inteiro.')
            continue
        if quantidade <= 0:
            print('\nA quantidade tem que ser maior que zero.')
            continue
        quantidades.append(quantidade)
        break

    while True:
        try:
            preco = float(input(f'Informe o preço do(a) {produto}: '))
        except ValueError:
            print('\nDigite um valor numérico.\n')
            continue
        if preco <= 0:
            print('\nO preço tem que ser maior que zero!\n')
            continue
        valores.append(preco)
        break

    while True:
        try:
            Outro_Produto = int(input(
                'Quer cadastrar outro produto?\n'
                '1 - Sim\n'
                '2 - Não\n'
            ))
        except ValueError:
            print('\nDigite uma opção numérica: 1 ou 2.')
            continue
        if Outro_Produto == 1:
            break
        elif Outro_Produto == 2:
            break
        print('\nEscolha 1 ou 2.')

print('\nRESUMO DO PEDIDO:')
print(f'Nome: {nome}')

total_geral = 0
for i in range(len(produtos)):
    total = quantidades[i] * valores[i]
    total_geral += total
    print(f'PRODUTO: {produtos[i]}')
    print(f'QUANTIDADE: {quantidades[i]}')
    print(f'PREÇO UNITÁRIO: R${valores[i]:.2f}')
    print(f'SUBTOTAL: R${total:.2f}')

print(f'VALOR TOTAL DO PEDIDO: R${total_geral:.2f}')
