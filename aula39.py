# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3]
tupla = 'Python', 'é', 'legal'

for nome in lista:
  print(nome, end=' ')
  
# Tanto o for como o print faz a mesma função

print(*lista)  
