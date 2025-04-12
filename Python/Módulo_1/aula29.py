"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
#try:
#   print(123)
#   print(456)
#   int('a')
# except ValueError as ERRO_EXCECAO:
#   print('Erro!')
try:
    numero = (input('Informe um número aqui: '))
except:
    print('Erro de exceção.')
#print(numero.isdigit())
#if int(numero) > 0:
#    numero = int(numero) * 2
#    print(f'O dobro do seu número é: {numero}')