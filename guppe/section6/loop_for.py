"""
Loop for

Loop -> estrutura de repetição
For -> Uma dessas estruturas

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = "Geek University"
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(f'{letra} ', end='')
print()

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(f'{numero} ', end='')
print()

# Exemplo de for 3 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.
1 2 3 4 5 6 7 8 9
10 - Não
"""
for numero in range(1, 10):
    print(f'{numero} ', end='')

"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...
"""
for i, v in enumerate(nome):
    print(f'{i}: {v} ', end='')
