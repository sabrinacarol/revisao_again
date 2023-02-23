''' Faça uma lista de compras com listas 
o usuário deve ter a possibilidade de inserir, apagar
e listar valores da sua lista. não permita que o 
programa quebre com erros de índices inexistentes na lista.
'''
import os

lista = []
while True:
    print('Selecione uma das opções')
    opcao = ('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha um índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        