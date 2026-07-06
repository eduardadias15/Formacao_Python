print(str('=' * 20 + 'Vamos descobrir se o número é par ou ímpar!'+ '=' * 20))
Número = float(input('Digite um número para saber se ele é par ou ímpar:'))

if Número % 2 == 0:
    print(f'O número {Número} é par!')
else:
    print(f'O número {Número} é ímpar!')
print(str('=' * 20 + f'Parabéns! você descobriu se o número {Número} é par ou ímpar!' + '=' * 20))