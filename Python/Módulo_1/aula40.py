''' Calculadora com While '''

# while True:
#     print('MENU: ')
#     numero_1 = input('Digite um numero: ')
#     numero_2 = input('Digite outro numero: ')
#     operador = input('Digite o operador (+-/*): ')
    
#     numeros_validos = None

#     try:
#         num1_float = float(numero_1)
#         num2_float = float(numero_2)
#         numeros_validos = True
#     except:
#         numeros_validos = None
  
#     if numeros_validos is None:
#         print('Um ou ambos numeros digitados foram invalidos.')
#         continue
#     operadores_permitidos = '+-/*'
#     if operador not in operadores_permitidos:
#         print('Operador invalido.')
#         continue
#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue

#         ###

#     if operador == '+':
#         soma = num1_float + num2_float
#         print(f'Resultado = {soma}')
#     elif operador == '-':
#         subtracao = num1_float - num2_float
#         print(f'Resultado = {subtracao}')
#     elif operador == '/':
#         divisao = num1_float / num2_float
#         print(f'Resultado = {divisao}')
#     elif operador == '*':
#         multiplicacao = num1_float * num2_float
#         print(f'Resultado = {multiplicacao}')

#     sair = input('Quer sair? [s]im: ').lower().startswith('s')
#     if sair is True:
#         break
