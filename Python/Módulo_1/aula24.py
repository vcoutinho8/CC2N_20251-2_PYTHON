# Operadores in e not in
# String são iteráveis
# 0 1 2 3 4 5 6 7
# V i n i c i u s
# -8-7-6-5-4-3-2-1
nome = 'Vinicius'
#print(nome[0])
#print(nome[1])
#print(nome[2])
#print(nome[3])
#print(nome[4])
#print(nome[5])
#print(nome[6])
#print(nome[7])
#print(10 * 'z')
#print('n' in nome)
#print('z' in nome)
#print('cius' not in nome)
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}!')
else:
    print(f'{encontrar} não está em {nome}!')