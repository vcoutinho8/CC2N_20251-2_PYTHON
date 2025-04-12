"""LISTA 2 - ESTRUTURA DE REPETIÇÃO"""

"""# EXERCÍCIO NÚMERO 1:"""

try:
  print('OS MÚLTIPLOS DE 3 NO INTERVALO: [3 100] SÃO: ')
  quantidade = 0
  for contador in range(3, 101, 3):
      if (contador % 3 == 0):
        quantidade += 1
        print(f'{quantidade}º - {contador}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

"""# EXERCÍCIO NÚMERO 2:"""

print('OS MÚLTIPLOS DE 11 SÃO: ')
quantidade = 0
soma = 0
try:
    for contador in range(200, 99, -1):
        if contador % 11 == 0:
            quantidade += 1
            soma += contador
            print(f'{quantidade}º - {contador} / a soma com o número anterior é: {soma}')
    if quantidade > 0:
        media = soma / quantidade
        print(f'A média dos múltiplos de 11 é: {media:.2f}')
    else:
        print('Nenhum múltiplo de 11 encontrado.')
except ValueError:
    print('Erro: Não há múltiplos de 11 para calcular a média.')

"""# EXERCÍCIO NÚMERO 3:"""

try:
    limite_inf = int(input("Digite o limite inferior: "))
    limite_sup = int(input("Digite o limite superior: "))
    n = int(input("Digite o número para encontrar os múltiplos: "))

    print(f"Os múltiplos de {n} no intervalo [{limite_inf}, {limite_sup}] são: ")

    for i in range(limite_inf, limite_sup + 1):
        if i % n == 0:
            print(i, end=' ')
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")
except Exception as e:
    print(f"Erro inesperado: {e}")

"""# EXERCÍCIO NÚMERO 4:"""

soma_pares = 0
soma_impares = 0

for contador in range(10, 100):
    if contador % 2 == 0:
        soma_pares += contador  # Soma apenas os pares
    else:
        soma_impares += contador  # Soma apenas os ímpares

print(f'A soma dos números PARES é: {soma_pares}')
print(f'A soma dos números ÍMPARES é: {soma_impares}')
print(f'A soma total (pares + ímpares) é: {soma_pares + soma_impares}')

"""# EXERCÍCIO NÚMERO 5:"""

total_habitantes = 5  # NÃO PODE SER 10.000 POIS TERÁ MUITAS RESPOSTAS
empregados = 0

for _ in range(total_habitantes):
    resposta = input('Está empregado? (S/N) ')
    while resposta != 'S' and resposta != 'N':
        print('Digite uma resposta válida! (S/N)')
        resposta = input('Está empregado? (S/N) ')
    if resposta == 'S':
        empregados += 1

percentual_empregados = (empregados / total_habitantes) * 100
percentual_desempregados = 100 - percentual_empregados

print(f'Empregados: {percentual_empregados:.2f}%')
print(f'Desempregados: {percentual_desempregados:.2f}%')

"""# EXERCÍCIO NÚMERO 6:"""

SM = 998.05  # Salário Mínimo
clientes_A = 0
clientes_B = 0
clientes_C = 0

total_clientes = 5 # Não pode ser 1000 pois vai ser muitas entradas0

for _ in range(total_clientes):
    salario = float(input("Digite o salário do cliente (R$): "))

    if salario >= 15 * SM:
        clientes_A += 1
    elif salario >= 5 * SM:
        clientes_B += 1
    else:
        clientes_C += 1

percent_A = (clientes_A / total_clientes) * 100
percent_B = (clientes_B / total_clientes) * 100
percent_C = (clientes_C / total_clientes) * 100

print(f"Percentual de clientes tipo A: {percent_A:.2f}%")
print(f"Percentual de clientes tipo B: {percent_B:.2f}%")
print(f"Percentual de clientes tipo C: {percent_C:.2f}%")

"""# EXERCÍCIO NÚMERO 7:"""

quantidade = 0
soma_impares = 0

for contador in range (9, 100, 3):
  if contador % 2 != 0:
    quantidade += 1
    print(f'{quantidade}º - {contador} é impar e múltiplo de 3.')
    soma_impares += contador
print(f'A soma total dos ímpares é: {soma_impares}')

"""# EXERCÍCIO NÚMERO 8:"""

mix1 = 0
mix2 = 0
mix3 = 0
total_votos = 0

while True:
  print('MENU:')
  print('Opção 1: Mix 1')
  print('Opção 2: Mix 2')
  print('Opção 3: Mix 3')
  print('Digite 0 para sair.')
  opcao = int(input('Informe o tipo do seu mix aqui: '))
  if opcao == 0:
    print('Você escolheu sair!')
    break
  elif opcao == 1:
    mix1 += 1
  elif opcao == 2:
    mix2 += 1
  elif opcao == 3:
    mix3 += 1
  else:
    print('ERRO: Escolha novamente!')
    continue
  total_votos += 1

  if total_votos > 0:
    print(f'Opção 1 - (Mix 1): {(mix1 / total_votos) * 100:.2f}%')
    print(f'Opção 2 - (Mix 2): {(mix2 / total_votos) * 100:.2f}%')
    print(f'Opção 3 - (Mix 3): {(mix3 / total_votos) * 100:.2f}%')

"""# EXERCÍCIO NÚMERO 9:"""

soma = 0

while True:
    N = int(input("Digite um número (0 para sair): "))
    if N == 0:
        break
    if (10 <= N or N <= 90) and N % 5 == 2:
        soma += N

print(f"A soma dos números lidos que atendem à condição é: {soma}")

"""# EXERCÍCIO NÚMERO 10:"""

print('Intervalo de [6, 6x]')
x = int(input('Digite aqui o valor de X no intervalo: '))
if x >= 1:
    soma = 0
    contador = 0
    for num in range(6, (6 * x) + 1, 6):
        print(num)
        soma += num
        contador += 1
    media = soma / contador  # Média dos números gerados
    print(f'A média desses números é: {media:.2f}')
else:
    print('ERRO: X precisa ser maior ou igual a um (x >= 1)!')

"""# EXERCÍCIO NÚMERO 11:"""

try:
  numero = int(input('Digite um número inteiro qualquer: '))
  print("Os 50 números subsequentes são:")
  for i in range(1, 51):
      print(numero + i)
except ValueError

"""# EXERCÍCIO NÚMERO 12:"""

temperaturas = []

while True:
    try:
        temp = float(input("Digite a temperatura do dia (ou um valor abaixo de 28 para encerrar): "))

        if temp < 28:
            break

        temperaturas.append(temp)
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"A temperatura média do verão foi: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi registrada.")

"""# EXERCÍCIO NÚMERO 13:"""

num_pessoas = 3

maior_altura_homem = 0
maior_altura_mulher = 0

soma_altura_homens = 0
soma_altura_mulheres = 0
cont_homens = 0
cont_mulheres = 0

homens_acima_182 = 0
mulheres_acima_182 = 0

for i in range(num_pessoas):
    altura = float(input(f"Digite a altura da {i+1}ª pessoa (em metros): "))
    sexo = int(input("Digite o sexo (1 para Masculino, 2 para Feminino): "))

    if sexo == 1:  # Masculino
        cont_homens += 1
        soma_altura_homens += altura
        if altura > maior_altura_homem:
            maior_altura_homem = altura
        if altura > 1.82:
            homens_acima_182 += 1
    elif sexo == 2:  # Feminino
        cont_mulheres += 1
        soma_altura_mulheres += altura
        if altura > maior_altura_mulher:
            maior_altura_mulher = altura
        if altura > 1.82:
            mulheres_acima_182 += 1
    else:
        print("Entrada inválida! Considerando pessoa não cadastrada.")
        continue

# Cálculo das médias de altura
media_altura_homens = soma_altura_homens / cont_homens if cont_homens > 0 else 0
media_altura_mulheres = soma_altura_mulheres / cont_mulheres if cont_mulheres > 0 else 0

# Cálculo da porcentagem
porc_homens_acima_182 = (homens_acima_182 / cont_homens * 100) if cont_homens > 0 else 0
porc_mulheres_acima_182 = (mulheres_acima_182 / cont_mulheres * 100) if cont_mulheres > 0 else 0

# Exibição dos resultados
print(f"Maior altura entre os homens: {maior_altura_homem:.2f} m")
print(f"Maior altura entre as mulheres: {maior_altura_mulher:.2f} m")
print(f"Média de altura dos homens: {media_altura_homens:.2f} m")
print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} m")
print(f"Porcentagem de homens com mais de 1.82m: {porc_homens_acima_182:.2f}%")
print(f"Porcentagem de mulheres com mais de 1.82m: {porc_mulheres_acima_182:.2f}%")

"""# EXERCÍCIO NÚMERO 14:"""

voto_1 = 0
voto_2 = 0
voto_0 = 0
menu = 0

total_votos = 0

while menu < 50:
    print("\nMENU:")
    print("Pressione (1) para votar no Candidato 1.")
    print("Pressione (2) para votar no Candidato 2.")
    print("Pressione (0) para votar nulo.")
    print("Pressione (9) para sair do menu.")

    try:
        opcao = int(input("Digite aqui sua opção: "))

        if opcao == 9:
            print("Você escolheu sair do menu.")
            break
        elif opcao == 1:
            voto_1 += 1
        elif opcao == 2:
            voto_2 += 1
        elif opcao == 0:
            voto_0 += 1
        else:
            print("ERRO: ESCOLHA NOVAMENTE!")
            continue  # Volta para o início do loop sem contar como um voto válido

        menu += 1  # Conta apenas votos válidos
        total_votos += 1

    except ValueError:
        print("ERRO: Digite um número válido!")

# Exibição dos resultados
print("\n=== Resultado da Votação ===")
if total_votos > 0:
    print(f"Candidato 1: {voto_1} votos ({(voto_1 / total_votos) * 100:.2f}%)")
    print(f"Candidato 2: {voto_2} votos ({(voto_2 / total_votos) * 100:.2f}%)")
    print(f"Votos Nulos: {voto_0} votos ({(voto_0 / total_votos) * 100:.2f}%)")
else:
    print("Nenhum voto foi registrado.")

"""# EXERCÍCIO NÚMERO 15:"""

positivos = 0
negativos = 0
total = 0

while True:
    try:
        numero = float(input("Digite um número real (ou 0 para encerrar): "))

        if numero == 0:
            break

        total += 1
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

if total > 0:
    perc_positivos = (positivos / total) * 100
    perc_negativos = (negativos / total) * 100
    print(f"Porcentagem de números positivos: {perc_positivos:.2f}%")
    print(f"Porcentagem de números negativos: {perc_negativos:.2f}%")
else:
    print("Nenhum número válido foi registrado.")

"""# EXERCÍCIO NÚMERO 16:"""

maior_par = float('-inf')
menor_par = float('inf')
maior_impar = float('-inf')
menor_impar = float('inf')

for _ in range(5): #PRECISA SER 300 MAS PRA TESTAR É UM MENOR VALOR!
    num = int(input("Digite um número positivo: "))

    if num % 2 == 0:  # Número par
        if num > maior_par:
            maior_par = num
        if num < menor_par:
            menor_par = num
    else:  # Número ímpar
        if num > maior_impar:
            maior_impar = num
        if num < menor_impar:
            menor_impar = num

print(f"Maior número par: {maior_par}")
print(f"Menor número par: {menor_par}")
print(f"Maior número ímpar: {maior_impar}")
print(f"Menor número ímpar: {menor_impar}")

"""# EXERCÍCIO NÚMERO 17:"""

menor = None
print('MENU:')
while True:

  n = float(input('Digite um número real positivo: '))

  if n == 0:
    print('Você escolheu sair.')
    break
  elif n < 0:
    print('Digite apenas valores positivos.')
    continue

  if menor is None or n < menor:
    menor = n

if menor is not None:
  print(f'O menor número é o: {menor:.2f}')
else:
  print("Nenhum número válido foi informado.")

"""# EXERCÍCIO NÚMERO 18:"""

count = 0
soma = 0
numero = 1  # Começamos do primeiro número ímpar

while count < 100:
    if numero % 7 == 0:  # Verifica se é múltiplo de 7
        soma += numero
        count += 1
    numero += 2  # Incrementa de 2 em 2 para garantir que seja ímpar

media = soma / 100
print(f"A média dos 100 primeiros números ímpares múltiplos de 7 é: {media}")

"""# EXERCÍCIO NÚMERO 19:"""

resposta = input('Digite quais múltiplos quer ver: (7) ou (13): ')
if resposta == '7':
    for numero in range(1000, 1501):
        if numero % 7 == 0:
            print(numero)
elif resposta == '13':
    for numero in range(1000, 1501):
        if numero % 13 == 0:
            print(numero)
else:
    print('Digite apenas (7) ou (13)!')

"""# EXERCÍCIO NÚMERO 20:

> Adicionar aspas


"""

# Inicialização de variáveis
cartao_vip = 0
cartao_standard = 0
contador_vip = 0
contador_standard = 0

while True:
    print('MENU:')
    print('Digite "1" para cadastrar cliente.')
    print('Digite "0" para SAIR do Programa.')
    opcao = input('Digite aqui sua escolha: ')

    if opcao == '0':
        print('Você decidiu SAIR do Programa.')
        break
    elif opcao == '1':
        # Solicita o salário do cliente
        salario = float(input('Informe seu salário em (R$): '))

        # Verifica qual tipo de cartão o cliente deve receber
        if salario >= 5000:
            cartao_vip += salario  # Acumula o valor para o Cartão VIP
            contador_vip += 1      # Conta o número de clientes VIP
        else:
            cartao_standard += salario  # Acumula o valor para o Cartão STANDARD
            contador_standard += 1      # Conta o número de clientes STANDARD

        # Exibe as porcentagens de clientes por tipo de cartão
        total_clientes = contador_vip + contador_standard

        if total_clientes > 0:
            perc_vip = (contador_vip / total_clientes) * 100
            perc_standard = (contador_standard / total_clientes) * 100
            print(f'Porcentagem de clientes com Cartão VIP: {perc_vip:.2f}%')
            print(f'Porcentagem de clientes com Cartão STANDARD: {perc_standard:.2f}%')
        else:
            print('Nenhum cliente cadastrado ainda.')

    else:
        print('Digite valores válidos.')

"""# EXERCÍCIO NÚMERO 21:

"""

import math

total = 0
soma = 0
limite_inferior = 10 * math.pi ** 3
limite_superior = 100 * math.pi

while True:
    try:
        numero = float(input(f"Digite um número dentro do intervalo [{limite_inferior:.2f}, {limite_superior:.2f}] (ou fora dele para encerrar): "))

        if numero < limite_inferior or numero > limite_superior:
            break

        total += 1
        soma += numero
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

if total > 0:
    media = soma / total
    print(f"A média dos números dentro do intervalo foi: {media:.2f}")
else:
    print("Nenhum número válido foi registrado dentro do intervalo.")

"""# EXERCÍCIO NÚMERO 22:

"""

total = 0
soma = 0
limite_inferior = -15
limite_superior = 5

while True:
    try:
        temperatura = float(input(f"Digite a temperatura diária da estação de esqui (entre {limite_inferior}°C e {limite_superior}°C, ou fora para encerrar): "))

        if temperatura < limite_inferior or temperatura > limite_superior:
            break

        total += 1
        soma += temperatura
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

if total > 0:
    media = soma / total
    print(f"A temperatura média da estação foi: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi registrada.")

"""# EXERCÍCIO NÚMERO 23:"""

vencedor_inscricao = None
vencedor_tempo = float('inf')

total_maratonistas = 20000

for _ in range(total_maratonistas):
    try:
        inscricao = input("Digite a inscrição do maratonista: ")
        tempo = input("Digite o tempo de prova (em minutos) (ou 0 para parar): ")

        # Verifica se o usuário deseja sair
        if tempo == '0':
            print("Programa interrompido pelo usuário.")
            break

        tempo = float(tempo)

        if tempo < vencedor_tempo:
            vencedor_tempo = tempo
            vencedor_inscricao = inscricao
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

if vencedor_inscricao is not None:
    print(f"O maratonista vencedor foi o de inscrição {vencedor_inscricao} com um tempo de {vencedor_tempo:.2f} minutos.")
else:
    print("Nenhuma inscrição válida foi registrada.")

"""# EXERCÍCIO NÚMERO 24:"""

total_mercadorias = 50
teto_reajuste = 25.50

for _ in range(total_mercadorias):
    try:
        preco = input("Digite o preço da mercadoria em reais (ou 0 para sair): ")

        # Verifica se o usuário deseja sair
        if preco == '0':
            print('Saindo do programa...')
            break

        preco = float(preco)
        preco_reajustado = preco * 1.05

        if (preco_reajustado - preco) > teto_reajuste:
            preco_reajustado *= 0.98  # Reduz 2% do preço reajustado

        print(f"Preço original: R$ {preco:.2f} | Preço reajustado: R$ {preco_reajustado:.2f}")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

"""# EXERCÍCIO NÚMERO 25:"""

import math

total_pacientes = 500

for _ in range(total_pacientes):
    try:
        idade = float(input("Digite a idade do paciente: "))
        massa = float(input("Digite a massa do paciente (kg): "))
        diabetico = input("O paciente é diabético? (s/n): ").strip().lower()

        # Condição para sair
        if idade == 0 or massa == 0 or diabetico == '0':
            print('Você escolheu sair.')
            break

        if diabetico == 's':
            taxa = (math.sqrt(massa ** 2)) / (0.93 * idade)
        elif diabetico == 'n':
            taxa = (math.sqrt(0.98 * (massa ** 2))) / (1.08 * idade)
        else:
            print("Entrada inválida para diabético. Digite 's' ou 'n'.")
            continue

        print(f"Taxa média de glicose do paciente: {taxa:.2f}")

    except ValueError:
        print("Entrada inválida! Digite números válidos para idade e massa.")

"""# EXERCÍCIO NÚMERO 26:"""

soma = 0
contador = 0

print('MENU:')
while True:
    escolaridade = input('Informe sua escolaridade Superior (S), Médio (M), Fundamental (F) ou "X" para sair: ').upper()

    if escolaridade == 'X':  # Opção para sair do loop
        break

    if escolaridade not in ('S', 'M', 'F'):
        print('ERRO: Digite apenas valores válidos (S, M ou F).')
        continue  # Volta para o início do loop

    try:
        salario = float(input('Informe seu salário aqui (R$): '))
        if salario < 0:
            print('Digite um valor positivo para o salário!')
            continue
    except ValueError:
        print('ERRO: Digite um valor numérico válido.')
        continue

    if escolaridade == 'S':
        print(f'A sua escolaridade é Superior e seu salário é: R$ {salario:.2f}')
    elif escolaridade == 'M':
        print(f'A sua escolaridade é Médio e seu salário é: R$ {salario:.2f}')
    elif escolaridade == 'F':
        print(f'A sua escolaridade é Fundamental e seu salário é: R$ {salario:.2f}')

    soma += salario
    contador += 1

if contador > 0:
    media = soma / contador
    print(f'A média entre os salários informados é: R$ {media:.2f}')
else:
    print('Nenhum salário válido foi informado.')

"""# EXERCÍCIO NÚMERO 27:"""

positivos = 0
negativos = 0
soma_positivos = 0
soma_negativos = 0

while True:
    try:
        numero = float(input("Digite um número real (ou 0 para encerrar): "))

        if numero == 0:
            break

        if numero > 0:
            positivos += 1
            soma_positivos += numero
        else:
            negativos += 1
            soma_negativos += numero
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

if positivos > 0:
    media_positivos = soma_positivos / positivos
    print(f"Média dos números positivos: {media_positivos:.2f}")
else:
    print("Nenhum número positivo foi registrado.")

if negativos > 0:
    media_negativos = soma_negativos / negativos
    print(f"Média dos números negativos: {media_negativos:.2f}")
else:
    print("Nenhum número negativo foi registrado.")

"""# EXERCÍCIO NÚMERO 28:"""

import math

pi = math.pi
soma = 0
multiplicacao = 1

try:
    n = int(input('Digite um valor inteiro positivo: '))

    if n < 1:
        print('ERRO: Digite apenas valores inteiros positivos!')
    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                soma += pi / i
            else:
                multiplicacao *= i / pi

        print('\nResultado:')
        print(f'O resultado da soma é: {soma:.2f}')
        print(f'O resultado da multiplicação é: {multiplicacao:.2f}')
except ValueError as ERRO_EXCECAO:
    print(f"Erro: {ERRO_EXCECAO}")