"""
Iterando strings com while
"""
#       012345678910
nome = 'Vinicius'  # Iteráveis
#      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[0])

indice = 0
while indice < len(nome):
    caractere = nome[indice]
    print('*' + caractere, end='')
    indice += 1