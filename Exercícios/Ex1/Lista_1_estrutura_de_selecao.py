"""LISTA 1 - ESTRUTURA DE SELEÇÃO"""

"""# EXERCÍCIO NÚMERO 1:"""

try:
  import math
  raio = float(input('Informe o raio em centímetros: '))
  area = 4 * round((math.pi), 2) * raio ** 2
  volume = 4 / 3 * round((math.pi), 2) * raio ** 3
  if (raio < 0):
    print('ERRO: O RAIO PRECISA SER MAIOR QUE ZERO E POSITIVO!')
  else:
    print(f'A área da esfera é: {area: .2f} e o volume é: {volume: .2f}')
except:
  print('ERRO NA ENTRADA DE DADOS')

"""# EXERCÍCIO NÚMERO 2:"""

try:
  import math
  base = float(input('Informe a base em centímetros: '))
  altura = float(input('Informe a altura em centímetros: '))
  if (base < 0) and (altura < 0):
    print('ERRO: A ALTURA E A BASE PRECISAM SER MAIOR QUE ZERO!')
  else:
    perimetro = 2 * base + 2 * altura
    polegada = 2.54
    jardas = 91.44
    print(f'O perímetro em centímetros é: {perimetro}')
    print(f'O perímetro em polegadas é: {perimetro / polegada: .2f}')
    print(f'O perímetro em jardas é: {perimetro / jardas: .2f}')
except:
  print('ERRO NA ENTRADA DE DADOS')

"""# EXERCÍCIO NÚMERO 3:"""

try:
  tempo_segundos = int(input("Digite o tempo de permanência em segundos: "))
  if (tempo_segundos <= 0):
    print('ERRO: O NÚMERO PRECISA SER POSITIVO OU MAIOR QUE ZERO!')
  else:
    horas = int(tempo_segundos / 3600)
    segundos_restantes = tempo_segundos - (horas * 3600)
    minutos = int(segundos_restantes / 60)
    segundos = segundos_restantes - (minutos * 60)

    print(f"Tempo: {tempo_segundos} Segundos = {horas} Hora(s) + {minutos} Minuto(s) + {segundos} Segundo(s)")
except:
  print('ERRO NA ENTRADA DE DADOS!')

"""# EXERCÍCIO NÚMERO 4:"""

try:
  altura = float(input('Informe a sua altura: '))
  sexo = input('Informe o seu sexo (H para homem, M para feminino): ')
  if sexo == 'H':
    peso = (72.7 * altura) - 58
    print(f'Seu peso é de: {peso: .2f} kg.')
  elif sexo == 'M':
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso é de: {peso: .2f} kg.')
  else:
    print("ERRO: Sexo inválido! Digite M para masculino ou F para feminino.")
except:
  print('ERRO NA ENTRADA DE DADOS!')

"""# EXERCÍCIO NÚMERO 5:"""

valor_ingresso = float(input("Valor do ingresso (R$): "))
total_pessoas = int(input("Total de pessoas no estádio: "))
arrecadacao = 0

total_pessoas > 0
idade = int(input("Idade: "))
if idade >= 10:
        if idade <= 17 or input("Doou 1kg de alimento? (s/n): ") == 's':
            arrecadacao += valor_ingresso / 2
            arrecadacao += valor_ingresso
total_pessoas -= 1

print(f"Público total: {total_pessoas} pessoas")
print(f"Arrecadação total: R$ {arrecadacao:.2f}")

"""# EXERCÍCIO NÚMERO 6:"""

try:
  numero = int(input('Digite um número positivo: '))
  if numero > 0:
    quadrado = numero ** 2

    if quadrado % 2 != 0 and quadrado % 11 == 0:
        print(f'O quadrado de {numero} é {quadrado}, que é ímpar e múltiplo de 11.')
    else:
        print(f'O quadrado de {numero} é {quadrado}, que NÃO atende aos critérios.')
  else:
    print('Número inválido! Digite um número positivo.')
except:
  print('ERRO NA ENTRADA DE DADOS!')

"""# EXERCÍCIO NÚMERO 7:"""

try:
    preco = float(input('Digite o preço da mercadoria (R$): '))

    porcentos_usuario = float(input('Quantos porcentos (%) de reajuste você deseja? '))
    print(f'Para o reajuste de {porcentos_usuario:.0f}% escolha:\nAcréscimo (A) ou Desconto (D)?', end=' ')

    usuario_opcao = input().strip().lower()
    porcentos = porcentos_usuario / 100

    if usuario_opcao == 'a':
        preco_reajustado = preco + (porcentos * preco)
        print(f'O seu valor reajustado com acréscimo de {porcentos_usuario:.0f}% é: R$ {preco_reajustado:.2f}')
    elif usuario_opcao == 'd':
        preco_reajustado = preco - (porcentos * preco)
        print(f'O seu valor reajustado com desconto de {porcentos_usuario:.0f}% é: R$ {preco_reajustado:.2f}')
    else:
        print('ERRO: Opção inválida! Digite "A" para acréscimo ou "D" para desconto.')

except ValueError:
    print('ERRO: Entrada inválida! Certifique-se de digitar números corretamente.')

"""# EXERCÍCIO NÚMERO 8:"""

escala = input('Digite a escala de entrada Celsius ou Fahrenheit (C/F): ')
if escala == 'C' or escala == 'F':
  try:
    temperatura = float(input('Digite o valor da temperatura: '))
  except ValueError:
    print('ERRO: VALOR INVÁLIDO. DIGITE UM NÚMERO.')

  if escala == 'C':
    fahrenheit = (temperatura * 9/5) + 32
    print(f'{temperatura}°C equivalem a {fahrenheit: .2f}°F')
  else:
    celsius = (temperatura - 32) * 5/9
    print(f'{temperatura}°F equivalem a {celsius: .2f}°C')
else:
  print("ERRO: ESCALA INVÁLIDA! USE 'C' PARA CELSIUS OU 'F' PARA FAHRENHEIT.")

"""# EXERCÍCIO NÚMERO 9:"""

try:
  moeda = (input('Informe o tipo de moeda -> Real (R), Dolár (D), Libra (L): '))
  quantidade = float(input('Informe a quantidade em espécie: '))
  cotacao_real = 1.0
  cotacao_dolar = 5.844
  cotacao_libra = 7.55
  if moeda == 'R':
    em_dolar = quantidade / cotacao_dolar
    em_libra = quantidade / cotacao_libra
    print(f'{quantidade:.2f} Reais equivalem a {em_dolar:.2f} Dólares e {em_libra:.2f} Libras.')
  elif moeda == 'D':
    em_real = quantidade * cotacao_dolar
    em_libra = em_real / cotacao_libra
    print(f'{quantidade:.2f} Dólares equivalem a {em_real:.2f} Reais e {em_libra:.2f} Libras.')
  elif moeda == 'L':
    em_real = quantidade * cotacao_libra
    em_dolar = em_real / cotacao_dolar
    print(f'{quantidade:.2f} Libras equivalem a {em_real:.2f} Reais e {em_dolar:.2f} Dólares.')
  else:
    print("Moeda inválida! Use R, D ou L.")
except ValueError:
    print("ERRO: Insira um número válido!")

"""# EXERCÍCIO NÚMERO 10:"""

try:
    medida = input('Informe a unidade da massa (OZ, T, Q): ').strip().upper()
    quantidade = float(input('Informe a quantidade da massa: '))

    quant_onca = 0.0283495
    quant_tonelada = 1000

    if medida == 'OZ':
        em_quilograma = quantidade * quant_onca
        em_tonelada = em_quilograma / quant_tonelada
        print(f'{quantidade:.2f} Onça(s) equivalem a {em_tonelada:.6f} Tonelada(s) e {em_quilograma:.2f} Quilograma(s).')

    elif medida == 'T':
        em_quilograma = quantidade * quant_tonelada
        em_onca = em_quilograma / quant_onca
        print(f'{quantidade:.2f} Tonelada(s) equivalem a {em_onca:.2f} Onça(s) e {em_quilograma:.2f} Quilograma(s).')

    elif medida == 'Q':
        em_onca = quantidade / quant_onca
        em_tonelada = quantidade / quant_tonelada
        print(f'{quantidade:.2f} Quilograma(s) equivalem a {em_onca:.2f} Onça(s) e {em_tonelada:.6f} Tonelada(s).')

    else:
        print("Unidade inválida! Escolha entre OZ (Onça), T (Tonelada) ou Q (Quilograma).")

except ValueError:
    print('ERRO: Entrada de dados inválida! Certifique-se de digitar um número válido para a massa.')

"""# EXERCÍCIO NÚMERO 11:"""

try:
  hora_entrada = input("Hora de Entrada (HH:MM): ").strip()
  hora_saida = input("Hora de Saída (HH:MM): ").strip()
  valor_30min = float(input("Valor pago a cada 30 Minutos (R$): "))

  h1 = int(hora_entrada[:2])
  m1 = int(hora_entrada[3:])

  h2 = int(hora_saida[:2])
  m2 = int(hora_saida[3:])

  minutos_entrada = h1 * 60 + m1
  minutos_saida = h2 * 60 + m2

  if minutos_saida < minutos_entrada:
    minutos_saida += 1440

  tempo_total = minutos_saida - minutos_entrada

  if tempo_total > 1440:
    print("ERRO: Tempo de permanência inválido! O veículo não pode ultrapassar 24 horas.")
  elif tempo_total <= 30:
    print("Total a pagar: R$ 0.00 (Dentro do tempo de carência)")
  else:
    tempo_cobrado = tempo_total - 30
    parcelas = (tempo_cobrado + 29) // 30
    total_a_pagar = parcelas * valor_30min
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")
except:
  print('ERRO: Entrada dos dados inválida!')

"""# EXERCÍCIO NÚMERO 12:"""

try:
  massa = float(input("Digite sua massa em kg: "))
  altura = float(input("Digite sua altura em metros: "))


  imc = massa / (altura ** 2)

  if imc < 18.5:
      classificacao = "Magreza"
  elif imc < 25:
      classificacao = "Saudável"
  elif imc < 30:
      classificacao = "Sobrepeso"
  elif imc < 35:
      classificacao = "Obesidade Grau I"
  elif imc < 40:
      classificacao = "Obesidade Grau II (Severa)"
  else:
      classificacao = "Obesidade Grau III (Mórbida)"


  print(f"Seu IMC é: {imc:.2f}")
  print(f"Classificação: {classificacao}")
except:
  print('ERRO: Dados de entrada inválidos!')

"""# EXERCÍCIO NÚMERO 13:"""

try:
  PHI = 11.52743

  a = float(input("Digite o primeiro número: "))
  b = float(input("Digite o segundo número: "))
  c = float(input("Digite o terceiro número: "))

  media = (a + b + c) / 3

  limite_inferior = 10 * PHI
  limite_superior = 200 * PHI

  if limite_inferior <= media <= limite_superior:
      print(f"{media:.5f}")
  else:
      print(f"{(media ** 3):.5f}")
except:
  print('ERRO: Dados de entrada inválidos!')

"""# EXERCÍCIO NÚMERO 14:"""

try:
  av1 = float(input("Digite a nota da AV1 (0-10): "))
  av2 = float(input("Digite a nota da AV2 (0-10): "))
  tf = int(input("Digite o total de faltas: "))

  mp = (av1 + av2) / 2

  if tf > 10:
      status = "Reprovado por Falta"
  elif mp >= 7:
      status = "Aprovado"
      final = mp
  else:
      pf = float(input("Digite a nota da Prova Final (0-10): "))
      final = (mp + pf) / 2

      if final >= 5:
          status = "Aprovado na Final"
      else:
          status = "Reprovado"

  print("\nResultados:")
  print(f"AV1: {av1:.2f}")
  print(f"AV2: {av2:.2f}")
  print(f"Média Parcial: {mp:.2f}")
  if status == "Aprovado na Final":
      print(f"Prova Final: {pf:.2f}")
  print(f"Nota Final: {final:.2f}")
  print(f"Status: {status}")
except:
  print('ERRO: Entrada de dados!')

"""# EXERCÍCIO NÚMERO 15:"""

try:
  a = int(input("Digite o 1º valor inteiro positivo: "))
  b = int(input("Digite o 2º valor inteiro positivo: "))
  c = int(input("Digite o 3º valor inteiro positivo: "))
  d = int(input("Digite o 4º valor inteiro positivo: "))
  e = int(input("Digite o 5º valor inteiro positivo: "))

  if a <= 0 or b <= 0 or c <= 0 or d <= 0 or e <= 0:
      print("ERRO: Todos os valores devem ser inteiros positivos!")
  elif len(set([a, b, c, d, e])) < 5:
      print("ERRO: Os valores devem ser distintos!")
  else:
      pares = []
      impares = []

      if a % 2 == 0:
          pares.append(a)
      else:
          impares.append(a)

      if b % 2 == 0:
          pares.append(b)
      else:
          impares.append(b)

      if c % 2 == 0:
          pares.append(c)
      else:
          impares.append(c)

      if d % 2 == 0:
          pares.append(d)
      else:
          impares.append(d)

      if e % 2 == 0:
          pares.append(e)
      else:
          impares.append(e)

      media_pares = sum(pares) / len(pares) if pares else 0
      media_impares = sum(impares) / len(impares) if impares else 0

      print(f"Média dos números PARES: {media_pares:.2f}" if pares else "Nenhum número PAR foi inserido.")
      print(f"Média dos números ÍMPARES: {media_impares:.2f}" if impares else "Nenhum número ÍMPAR foi inserido.")
except:
  print('ERRO: Dados de entrada inválidos!')

"""# EXERCÍCIO NÚMERO 16:"""

try:
  a = float(input("Digite o primeiro valor: "))
  b = float(input("Digite o segundo valor: "))
  c = float(input("Digite o terceiro valor: "))

  if a == b or a == c or b == c:
    print("ERRO: Os valores devem ser distintos!")
  else:
    if a < b and a < c:
        media = (b + c) / 2
    elif b < a and b < c:
        media = (a + c) / 2
    else:
        media = (a + b) / 2

    print(f"A média dos dois maiores valores é: {media:.2f}")
except:
  print('ERRO: Dados de entrada inválidos!')

"""# EXERCÍCIO NÚMERO 17:"""

try:
  a = float(input("Digite o valor do lado A: "))
  b = float(input("Digite o valor do lado B: "))
  c = float(input("Digite o valor do lado C: "))

  if a < b + c and b < a + c and c < a + b:
      if a == b == c:
          print("O triângulo é Equilátero (todos os lados iguais).")
      elif a == b or a == c or b == c:
          print("O triângulo é Isósceles (dois lados iguais).")
      else:
          print("O triângulo é Escaleno (todos os lados diferentes).")
  else:
      print("Os valores informados NÃO formam um triângulo.")
except:
  print('ERRO: Dados de entrada inválidos!')