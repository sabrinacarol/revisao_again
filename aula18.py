'''Fatiamento de strings
 012345678 
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] (pega uma fatia da string)
Obs.: a função len retorna 
a qtd de caracteres da str
len - conta os caracteres, sized
indice - começa do 0 e vai até 8'''

variavel = 'Olá mundo'
print(variavel[4:6])
print(len(variavel))
print(variavel[0:len(variavel):1])

