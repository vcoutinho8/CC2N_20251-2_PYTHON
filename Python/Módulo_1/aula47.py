"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'BANANA'
contador = 0

while True:
    print('\n=== JOGO DA ADIVINHA ===')
    print('Tente adivinhar as letras da palavra secreta.')
    print(f'Dica: A palavra tem {len(palavra)} letras.')
    print('Digite 1 para responder.')
    print('Digite 0 para sair.')
    
    letra = input('Digite apenas uma letra: ').upper()

    if letra == '1':
        resposta = (input('Digite a palavra aqui: '))
        if resposta == palavra:
            print('Parábens! Você acertou a palavra.')
        break

    if letra == '0':
        print('Você escolheu sair! A palavra era:', palavra).upper()
        break

    if len(letra) != 1 or not letra.isalpha():
        print('ERRO: Digite apenas uma única letra válida.')
        continue

    contador += 1  # Incrementa a contagem de tentativas

    if letra in palavra:
        print(f'A letra "{letra}" está contida na palavra secreta!')
    else:
        print(f'A letra "{letra}" não está na palavra secreta. Tente novamente!')

    print(f'Tentativas: {contador}')

    