import os

lista = []

while True:

    print('Selecione uma das opções.')
    opcao = ('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor
                     )
    elif opcao == 'a':
        print('a')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar.')
    else:
        print('Escolha uma das opções estabelecidas')
