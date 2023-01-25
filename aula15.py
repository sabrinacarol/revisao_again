# Operador lógico and
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São consideradas falsy(Que não são especificamente valores falsos,
# mas são valores falsos) 0 0.0 '' False
# Tambem existe o tipo None que é usado para representar um não valor

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'

# if é uma condição 
# if só vai ser avaliado quando a expressão inteira for True
# tudo que está entre parenteses ela é avaliada primeiro

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

# Avaliação de curto circuito
#print(True or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)