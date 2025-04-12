"""
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loo infinito -> quando um condigo nao tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')