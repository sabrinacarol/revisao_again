'''Enumerate
Exiba os índices da lista
0 Maria
1 Sabrina
2 Kiara
'''
lista = ['Maria', 'Sabrina', 'Kiara']
lista.append('Lazaro')

# Pode ser escrito dessa forma comentada ou
# usando somente o for...

# lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    print(item)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
