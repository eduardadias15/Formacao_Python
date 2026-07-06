Distância = float(input('Digite a distância em km da sua viagem: '))

if Distância <= 200:
    print(f'O valor da sua passagem é de R${Distância * 0.50:.2f}.')
else:
    print(f'O valor da sua passagem é de R${Distância * 0.45:.2f}.')