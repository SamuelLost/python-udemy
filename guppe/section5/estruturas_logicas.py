"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo
"""
ativo = True
logado = True
if ativo and logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

# Exemplo 2
if logado is True:
    print("Bem-vindo usuário")

# Ativo é verdadeiro?
print(ativo is True)

nome = "Geek University"
print(nome.istitle())
