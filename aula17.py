""" Interpolação de string com %
f'{} e .format() e interpolação são a mesma coisa
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

# nome = 'Sabrina'
# preco = 1000.95897643
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %08X' % (1500, 1500))

''' Formatação com f' strings 
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número aparecer antes dos zeros
Sinal -  + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
(chama o metodo reprd=ask e string=str)__repr__ __str__
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4875648123746:+10,.1f}')
print(f'{variavel}!r')