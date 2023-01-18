"""
Entendendo o *args
- O *args é um parâmetro, como outro qualquer. Isso significa que você 
poderá chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:
*xis
Mas por convenção, utilizamos *args para definições de funções

Mas o que é o *args?
O parâmetro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""

# Exemplo

def soma_todos_numeros(*args):
    return sum(args)

# Outro exemplo
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é...'


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(3, 4, 5))
print(soma_todos_numeros(23.4, 12.5))

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

numeros = [1, 2, 3, 4, 5, 6, 7]
# Desempacotador
print(soma_todos_numeros(*numeros))
# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados. 
# Desta forma, ele saberá que precisará antes desempacotar estes dados.
