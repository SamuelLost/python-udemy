"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""
# Import
from collections import deque

# Criando deques
deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo
print(deq)

# Remover elementos
print(deq.pop())  # Remove e retorna o último elemento

print(deq.popleft())  # Remove e retorna o primeiro elemento

# Remover todos os elementos
deq.clear()
print(deq)

# Inverter a ordem dos elementos
deq = deque('geek')
deq.reverse()
print(deq)

# Copiando deques
deq = deque('geek')
novo = deq.copy()
print(novo)

# Podemos contar quantos elementos tem um determinado valor
print(deq.count('e')) 

