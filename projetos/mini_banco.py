def exibir_menu():
    print('=' * 20)
    print('MENU - Banco do Erickitto')
    print('Opção 1: Consultar saldo')
    print('Opção 2: Depositar')
    print('Opção 3: Resgatar')
    print('Opção 4: Fechar')
    print('=' * 20)


opcao = 0
saldo = 0
valor = 0

while opcao != 4:
    exibir_menu()
    try:
        opcao = int(input('Escolha uma opção: '))
        if not (1 <= opcao <= 4):
            print('\nDigite uma opção válida (1 a 4).\n')
            continue
    except ValueError:
        print('\nDigite apenas uma das opções numéricas apresentadas.')
        continue

    if opcao == 1:
        print(f'\nO saldo na conta é de R${saldo:.2f}')
    elif opcao == 2:
        try:
            valor = float(input('\nQuanto deseja depositar? '))
        except ValueError:
            print('\nDigite apenas números.')
            continue
        if valor <= 0:
            print('\nDigite um valor maior que zero.')
            continue
        saldo += valor
        print(f'\nDepósito de R${valor:.2f} concluído!')
    elif opcao == 3:
        try:
            valor = float(input('\nQuanto deseja resgatar? '))
        except ValueError:
            print('\nDigite apenas números.')
            continue
        if saldo < valor:
            print('\nVocê não tem saldo suficiente para este resgate.')
            continue
        elif valor <= 0:
            print('\nResgate um valor maior que zero.')
            continue
        saldo -= valor
        print(f'Resgate no valor de R${valor:.2f} concluído.')
    elif opcao == 4:
        print('\nEncerrando...')
