"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas: '''Angelinie Jolie'''
- Aspas duplas triplas;
"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # Entrada
nome = input('Qual o seu nome? ')

# Exemplo de print antigo
# print("Seja bem-vindo(a) %s" % nome)
# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}".format(nome))
# Exemplo de print 'mais atual' 3.7>
print(f'Seja bem-vindo(a) {nome}')
# print("Qual a sua idade? ")
# idade = input()
idade = int(input('Qual a sua idade? '))
# Processamento

# Saída de dados
# print("%s tem %s anos" % (nome, idade))
# print('{0} tem {1} anos'.format(nome, idade))
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {2022 - idade}')
