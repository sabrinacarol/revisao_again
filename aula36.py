'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].rstrip())

print(lista_frases)


# exemplo
# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x)

# txt = "welcome to the jungle"

# x = txt.split()

# print(x)
