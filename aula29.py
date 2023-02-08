'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
# iter() e .__iter__() são a msm coisa

texto = ('Sabrina')  # .__iter__()
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
# código de cima faz a msm coisa do de baixo
# o de baixo é mais usado e mais simples

for letra in texto:
    print(letra)
