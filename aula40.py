'''
Introdução ás funções (def) em Python Funçõees são
trechos de código usados para replicar determinada
ação ao longo do seu código.
Elas podem receber valores para parâmetros ou seja
(Argumentos) e retornar um valor específico.
Por padrão, funções Python retornam 
None (nada) quase como se fosse um False.
'''
# Obs: não é interessante começar
# o nome da função com letra maiuscula
# padrão em Python em nomes de funções é o msm das variáveis
# então deve-se começar com letra minúscula


# def imprimir(a, b, c):
#     print(a, b, c)

# Toda vez que se referir a variável (a)
# está se referindo ao parâmetro argumento


# imprimir(1, 2, 3)
# imprimir(1, 2, 3)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Sabrina')
saudacao('Kiara')
saudacao()
