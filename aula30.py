'''
for(continue, break, else, etc...)
'''

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('For completo com sucesso!')

'''For in com listas'''

lista = ['Ana', 'Maria', 'Kiara']

for nome in lista:
    print(nome, type(nome))