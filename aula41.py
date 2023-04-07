'''
Argumento nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

# Como se ler a função abaixo.
# definição da função é a soma que recebe x e y


def soma(x, y, z):
    # definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x+y+z)


soma(1, 2, 3)
soma(1, 2, z=5)

print(1, 2, 3, sep='-')

# Se colocar dessa forma ele ficará redundante pois
# exibirá duas vezes o print() o que ele entende é que
# eu pedi para  ele dá um print(soma(1, 2)) pedi dois prints
# se eu já defini a função soma então se eu chamar ela, ela já será exibida
#

# argumentos que passei x e y são argumentos posicionais
# pype é um caractere |
