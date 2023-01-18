"""
**kwargs
Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.

Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()  # Isso não gera erro
cores_favoritas(geek='navy')  # Isso não gera erro

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

def myfunction(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

myfunction(8, 'Julia')
myfunction(18, 'Felicity', 4, 5, 3, solteiro=True)
myfunction(34, 'Felipe', eu='Não', voce='Vai')
myfunction(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda porque é importante manter a ordem dos parâmetros na declaração
# Função com a ordem correta de parâmetros
def mostrainfo(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros
# def mostrainfo(a, b, instrutor='Geek', *args, **kwargs):
#     return [a, b, args, instrutor, kwargs]

print(mostrainfo(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função.

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)
