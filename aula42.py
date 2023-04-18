'''
Valores padrão para parâmetros 
ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: É editar o seu código.

'''
# Mostrar que z é none (Definir como um não valor)

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)