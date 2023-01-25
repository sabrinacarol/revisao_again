''' Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados: (if, elif,else)
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu o nome contém (ou não) espaços 
        Seu nome tem {n} letras (quantas letras tem)
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
    
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    print(f'Sua idade é {idade} anos.')     
else:
    print('Desculpe, você deixou campos vazios.')