'''
Exercicio Iterando strings com while
'''
# ......01234567
nome = 'samantha'  # iteráveis

tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# nova_string = ''
# nova_string +=

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
