'''
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update  Delete --- CRUD
Criar  Ler  Alterar Apagar = lista[i] (CRUD)
'''

#         +01234
#         -54321
string = 'ABCDE'  # 5 caracteres (len)
lista = [0, 1, 2, 3, 'a', 'oi']
# lista[2] = 200  # altera o valor
# del lista[2]  # apaga o indice 2 da []
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
ultimo_valor = lista.pop()
print(lista, 'Removido: ', ultimo_valor)
