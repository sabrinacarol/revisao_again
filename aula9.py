# Introdução Operadores aritméticos

adicao = 10 + 10
print('Adição:', adicao)

subtracao = 10 - 5
print('Subtração:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

divisao = 10 / 2
print('Divisão:', divisao)
# Sempre retorna float

divisao_inteira = 10 // 2.5
print('Divisão inteira:', divisao_inteira)
# Ela trunca o resultado da divisão

exponenciacao = 2 ** 10
print('Exponenciação:', exponenciacao)

modulo = 25 % 6 
print('Módulo:', modulo)
# Resto da divisão () 

print(10 % 8 == 0)
print(16 % 8 == 0)
# Saber se um número é divisel 
# por outro ele retorna o resto da divasão 0

# Precedência dos operadores
conta_1 = 1 + 1 ** 5 + 5
print(conta_1)