"""
Tipo Float
"""

# Errado
valor = 1, 44
print(valor)  # O python vê como uma tupla
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(f'Tipo {type(valor1)} com valor {valor1}')
print(valor2)

# Podemos trabalhar com números complexos
variavel = 5j
print(f'Tipo {type(variavel)} com valor {variavel}')
variavel **= 2
print(variavel)
