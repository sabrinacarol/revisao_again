primeiro_valor = int(input('Digite uma valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'do que {segundo_valor=}'
        )
else:
    print(
        f'{segundo_valor=} é maior do que '
            f'{primeiro_valor=}'
    )