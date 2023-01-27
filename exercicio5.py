'''Exercício'''

'''
1) Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
number = input('Digite um número: ')

try:
    (number % 2) == 0:
    print(f'Número par {number}')
elif number:
    print(f'Número ímpar {number}')

except:
    print('Não digitou um número inteiro.')
