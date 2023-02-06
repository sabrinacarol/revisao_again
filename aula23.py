'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
'''
condição = True

while condição:
    nome = input('qual é seu nome? ')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break
print('Acabou!')
