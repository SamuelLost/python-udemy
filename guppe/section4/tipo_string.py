"""
Tipo string
Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples
- Estiver entre aspas duplas
- Estiver entre aspas simples triplas
- Estiver entre aspas duplas triplas
"""

nome = "Geek University"
print(nome)
print(type(nome))
print(nome[0:4])  # Slice de string
print(nome[5:15])
"""
[::-1] -> Comece do primeiro o elemento, vá até o último elemento e inverta (-1)
"""
print(nome[::-1])
nome = """Samuel
Henrique"""
print(nome)

teste = "Teste \" oi"
texto = "socorram me subino onibus em marrocos"  # Palíndromo
print(texto[::-1])
# print(teste.split()[0])
# print(teste.split()[1])
