''' 
Lista de listas e seus índices
'''

salas = [
    # 0 nº indice 1
    ['João', 'Sabrina', ],  # 0 nº da lista
    # 0
    ['Maria', ],  # 1 nº da lista
    # 0           1        2
    ['Lazaro', 'Pedro', 'Miguel', (0, 10, 20, 30, 40)],  # 2 nº da lista
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][3])
# print(salas[2][3][2])
# Entra na (lista 2) e depois entra na (tupla de indice 3) e depois mostra o (índice 3)

# Na primeira [lista] na segunda o [índice]

# for sala in salas:
#    print(sala)

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

# para cada sala nas salas me retorne a sala
# para cada aluno na sala me retorne aluno
# entao print aluno
