palavra= str(input('Digite uma palavra-código:')).strip()
primeira= palavra[0]
ultima= palavra[-1]
if len(palavra) % 2 ==0:
    print(f'A palavra {palavra} tem {len(palavra)} letras e é par.')
else:
    print(f'A palavra {palavra} tem {len(palavra)} letras e é ímpar.')

if primeira.lower()== ultima.lower():
    print(f'A primeira e a ultima letra são iguais: {primeira} e {ultima}.')
else:
    print('A primeira e a ultima letra da palavra são diferentes.')
vogais = 'aeiou'
contador= 0
for letra in palavra:
    if letra.lower() in vogais:
        contador = contador + 1
print(f'A palavra {palavra} tem {contador} vogais.')
if contador >3:
    print('Palavra com muitas vogais.')
else:
    print('Palavra com poucas vogais.')