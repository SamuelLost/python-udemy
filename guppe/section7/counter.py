"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter 
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro
e como valor a quantidade de ocorrências desse elemento.
"""

# Utilizando o Counter
from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4 , 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 4, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2
print(Counter('Geek University'))

# Exemplo 3
texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent euismod
nibh eu dolor cursus, nec ultricies elit tincidunt. Donec euismod, massa non
aliquam tincidunt, diam lorem lacinia risus, nec ultricies elit tincidunt non.
Vivamus auctor, tortor eget aliquam molestie, risus nisl elementum purus, non
aliquam tortor orci et mi. Donec euismod, massa non aliquam tincidunt, diam lorem
lacinia risus, nec ultricies elit tincidunt non. Vivamus auctor, tortor eget"""

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))

