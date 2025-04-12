"""LISTA 3 - MODULARIZAÇÃO"""

"""# EXERCÍCIO SORTEADO 1:"""

# CRIAR A FUNÇÃO AQUI:
def multiplicacao(n, opcao):
    resultado = 1
    encontrou = False

    for i in range(1, n + 1):
        if opcao == 'P' and i % 2 == 0:
            resultado *= i
            encontrou = True
        elif opcao == 'I' and i % 2 != 0:
            resultado *= i
            encontrou = True

    return resultado if encontrou else 0

# MENU: REUSABILIDADE
contador = 0
for i in range (100): # USA A FUNÇÃO 100 VEZES PARA OPÇÃO E NÚMERO.
  try:
      n = int(input('Informe um valor de n: '))
      opcao = input('Informe (P)ar ou (I)mpar: ').strip().upper()

      if opcao not in ['P', 'I']:
        print('Digite "P" para par e "I" para impar')
        continue

      if n <= 0:
        print('ERRO: Digite apenas n MAIOR que 0.')
        continue

      resultado = multiplicacao(n, opcao)
      print(f'O resultado é {resultado}.')

  except ValueError:
    print('ERRO: Entrada de dados.')

"""# EXERCÍCIO SORTEADO 2:"""

# CRIAR A FUNÇÃO AQUI:
def fatorial(N = 0):
  if(N == 0 or N == 1):
    return 1
  Fat = 1
  for i in range(2, N + 1):
    Fat *= i     # ACUMULAR: 1 * 2 * 3 * ... * n
  return Fat

def arranjo(n, p):
  A = fatorial(n) // fatorial(n - p)
  return A

def combinacao(n, p):
  C = fatorial(n) // (fatorial(p) * fatorial(n - p))
  return C

while True:
  try:
    print('\n--- Combinação e Arranjo ---')
    n = int(input('Digite um valor para N (ou 0 para sair): '))
    if n == 0:
      print('Encerrando o programa.')
      break

    p = int(input('Digite um valor para P (ou 0 para sair): '))
    if p == 0:
      print('Encerrando o programa.')
      break

    if n < 0 or p < 0:
      print('ERRO: N e P precisam ser MAIORES ou IGUAIS a zero.')
      continue

    if n < p:
      print('ERRO: N precisa ser MAIOR ou IGUAL a P.')
      continue

    resultado_1 = combinacao(n, p)
    resultado_2 = arranjo(n, p)

    print(f'Resultado da Combinação: {resultado_1:.2f}')
    print(f'Resultado do Arranjo: {resultado_2:.2f}')

  except ValueError:
    print('ERRO: Entrada inválida. Digite apenas números inteiros.')

"""# EXERCÍCIO SORTEADO 3:"""

# CRIAR A FUNÇÃO AQUI:
def somatorio_fibonacci(n):
    a, b = 0, 1
    soma = 0
    for i in range(n):
        soma += a
        a, b = b, a + b
    return soma

# MENU: REUSABILIDADE
try:
  n = int(input('Digite n para termos em Fibonacci: '))

  soma = somatorio_fibonacci(n)

  print(f'O somatório dos n termos é: {soma}')
except ValueError:
  print('ERRO: Entrada de dados.')

"""# EXERCÍCIO SORTEADO 4:"""

# CRIAR A FUNÇÃO AQUI:
def arran_comb (n, p):
  fatorial = N = 0
  if(N == 0 or N == 1):
    return 1
  Fat = 1
  for i in range(2, N + 1):
    Fat *= i
  return Fat

  arranjo = factorial(n) // factorial(n - p)
  combinacao = factorial(n) // (factorial(p) * factorial(n - p))
  return arranjo, combinacao

# MENU: REUSABILIDADE
while True:
  try:
    print('\n--- Combinação e Arranjo ---')
    n = int(input('Digite um valor para N (ou 0 para sair): '))
    if n == 0:
      print('Encerrando o programa.')
      break

    p = int(input('Digite um valor para P (ou 0 para sair): '))
    if p == 0:
      print('Encerrando o programa.')
      break

    if n < 0 or p < 0:
      print('ERRO: N e P precisam ser MAIORES ou IGUAIS a zero.')
      continue

    if n < p:
      print('ERRO: N precisa ser MAIOR ou IGUAL a P.')
      continue

    resultado_1 = combinacao(n, p)
    resultado_2 = arranjo(n, p)

    print(f'Resultado da Combinação: {resultado_1:.2f}')
    print(f'Resultado do Arranjo: {resultado_2:.2f}')

  except ValueError:
    print('ERRO: Entrada inválida. Digite apenas números inteiros.')

"""# EXERCÍCIO SORTEADO 5:"""

# CRIAR A FUNÇÃO AQUI:
def estacionamento(entrada, saida):
    h1, m1 = map(int, entrada.split(':'))
    h2, m2 = map(int, saida.split(':'))

    entrada_min = h1 * 60 + m1
    saida_min = h2 * 60 + m2

    if saida_min < entrada_min:
        saida_min += 24 * 60

    tempo_total = saida_min - entrada_min
    horas = tempo_total // 60
    minutos = tempo_total % 60

    if minutos > 0:
        horas += 1

    total = horas * 7
    return horas, minutos, total

# MENU: REUSABILIDADE
try:
  print('MENU: \n')
  print('Custo por hora: R$7,00')
  entrada = input('Hora de entrada (HH:MM): ')
  saida = input('Hora de saída (HH:MM): ')

  horas, minutos, total = estacionamento(entrada, saida)

  print(f'Diferença: {horas:02d}:{minutos:02d}')
  print(f'Total a pagar: R${total:.2f}')

except ValueError:
  print('ERRO: Entrada de dados.')