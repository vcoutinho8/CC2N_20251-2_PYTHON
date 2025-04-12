import math

# b)
# try:
#     while True:
#         print('Calcular a área de um quadrado')
#         l = int(input('Digite um tamanho em para L: '))
#         area_quadrado = l ** 2
#         if l < 0:
#             print('Digite apenas valores positivos para L.')
#             break
#         else:
#             print(f'A área do quadrado = {area_quadrado}')
# except ValueError:
#     print('ERRO: Entrada de dados.')



# c)
# try:
#     while True:
#         print('Calcular a área de um retângulo')
#         l = int(input('Digite a largura do retângulo: '))
#         h = int(input('Digite a altura do retângulo: '))
#         area_retangulo = l * h

#         if l and h <= 0:
#             print('ERRO: Digite valores positivos.')
#             break
#         else:
#             print(f'A área do retângulo = {area_retangulo}')
#             continue
# except ValueError:
#     print('ERRO: Entrada de dados.')

# d)
# pi = round(math.pi, 3)
# try:
#     while True:
#         print('Calcular a área e o comprimento do círculo')
#         r = float(input('Informe o R(raio) do círculo: '))

#         if r <= 0:
#             print('Informe um valor válido para o raio.')
#             break
#         else:
#             area = (pi * r**2)
#             comprimento = 2 * pi * r
#             print(f'A área do círculo é: {area:.2f} e o comprimento é: {comprimento:.2f}.')
#             continue
# except ValueError:
#     print('ERRO: Entrada de dados.')


# 1) 

# import math

# def funcao1(n, k):
#     factorial = math.factorial
#     f = k // factorial(n) + k
#     return f

# def funcao2(n, k, p):
#     f = ((k ** n - k) // p * n)
#     return f

# k = 2
# p = 4

# while True:
#     print('MENU:\n')
#     n = int(input('Informe um valor para n (ou 0 para sair): '))

#     if n <= 0:
#         print('Encerrando o programa.')
#         break

#     termo1 = funcao1(n, k)
#     termo2 = funcao2(n, k, p)

#     print(f'Termo 1 (funcao1): {termo1}')
#     print(f'Termo 2 (funcao2): {termo2}')

#     soma_termos = termo1 + termo2
#     print(f'Soma dos termos: {soma_termos}')

#     if termo2 != 0:
#         media_termos = termo1 // termo2
#         print(f'Média inteira dos termos: {media_termos}')
#     else:
#         print('Não é possível dividir por zero na média.')
