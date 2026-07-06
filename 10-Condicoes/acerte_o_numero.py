from random import choice
Numero = [0 , 1, 2, 3, 4, 5]
sorteado = choice(Numero)

print('='* 10 + 'Adivinhe o número sorteado!' + '='* 10)
print('Escolha um número entre 0 e 5')
escolhido= int(input('Digite o número que você escolheu: '))
if escolhido == sorteado:
    print(f'Parabéns! Você acertou o número sorteado que foi {sorteado}!')
else:
    print(f'Você não acertou o número sorteado que foi {sorteado}. Tente novamente!')
print('='* 18 + 'Fim do jogo!' + '='* 18)