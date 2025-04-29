"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = ['Banana', 'Uva', 'Goiaba']

try:
    while True:
        print('\nLista de compras:')
        for fruta in lista:
            print(f'- {fruta}')
        
        print('\n===============================')
        print('1 = Excluir item')
        print('2 = Adicionar item')
        print('3 = Enumerar itens')
        print('0 = Sair')
        opcao = int(input('Digite sua opção aqui: '))

        if opcao == 1:
            item = input('Digite aqui o item que deseja excluir: ')
            if item in lista:
                lista.remove(item)
                print(f'\nItem "{item}" removido com sucesso!')
            else:
                print('\nItem não encontrado na lista.')

        elif opcao == 2:
            fruta = input('Digite aqui o item que deseja adicionar: ')
            lista.append(fruta)
            print(f'\nItem "{fruta}" adicionado com sucesso!')

        elif opcao == 3:
            print('\nLista enumerada:')
            for indice, item in enumerate(lista):
                print(f'{indice}: {item}')

        elif opcao == 0:
            print('Você saiu.')
            break

        else:
            print('Opção inválida. Tente novamente.')

except ValueError:
    print('ERRO: Você digitou algo errado.')
