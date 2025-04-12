nome = 'Vinicius Coutinho'
altura = float(1.74)
peso = float(59.09)
imc = peso / (altura * altura) # IMC = peso / (altura x altura).

# f-strings
linha_1 = f'{nome} tem altura de {altura:.2f}.'
linha_2 = f'Pesa {peso:.2f} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
