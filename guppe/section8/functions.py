"""
Definindo funções
- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, 
é bom fazer uma verificação para que a função seja simplificada.
"""
# Exemplo de utilização de funções
# Core do sistema
def diz_oi():
    print('Oi!')

# Função com parametro padrão, caso não seja passado nenhum valor 
# para o parametro, o valor padrão será utilizado.
# OBS: Os parametros com valores padrão DEVEM sempre estar ao final da declaração
def exponente(numero, potencia=2):
    return numero ** potencia

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor...'
    return f'Olá {nome}'

# Função como parametro de outra função (função de alta ordem)
def soma(a, b):
    return a + b

def mat(a, b, fun=soma):
    return fun(a, b)

def sub(a, b):
    return a - b


# Fibonacci - Função
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado

# Utilizando funções
def sei_la():
    return 1, 2, 3, 4, 5

# Função para jogar uma moeda
from random import random
def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    # if random() > 0.5:
    #     return 'Cara'
    # return 'Coroa'
    return 'Cara' if random() > 0.5 else 'Coroa'

diz_oi()
print(joga_moeda())

var1, var2, var3, var4, var5 = sei_la()
print(var1)
oi = diz_oi
oi()
print(fibonacci(10))

# Exemplo de função com parametro padrão
print(exponente(2, 3))
print(exponente(3, 2))
print(exponente(3))

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Samuel'))

# Exemplo de função como parametro de outra função
print(mat(2, 3))
print(mat(2, 2, sub))


