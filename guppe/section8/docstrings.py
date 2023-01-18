"""
Documentando funções com Docstrings
"""
def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

# Exemplo de docstring
def diz_oi():
    """Uma função simples que retorna a string 'Olá!'"""
    return 'Olá!'

print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)

