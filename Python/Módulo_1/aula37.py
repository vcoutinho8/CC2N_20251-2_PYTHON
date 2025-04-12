"""
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loo infinito -> quando um condigo nao tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('X')
        continue

    if contador >= 10 and contador <= 27:
        print('X')
        continue

    print(contador)

    if contador == 40:     
        break


print('Acabou')

