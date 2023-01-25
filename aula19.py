'''Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

number = input('Vou dobrar o número que você digitar: ')

number_float = float(number)
print(f'O dobro de {number} é {number_float * 2:.0f}')

# Sempre que o usuário mandar um valor 
# você deve tratar esse valor

number_str = input('Digite um valor: ')
print(number_str.isdigit())




