frase = 'O python é uma linguagem de programação' \
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'


# print(frase.lower().count(''))
i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1
