nome= input('Informe seu nome: ')
peso= float(input('Informe seu peso em kg: '))
altura= float(input('Informe sua altura em metros: '))
IMC= peso/(altura**2)
IMCarredondado= round(IMC, 1)
if IMC < 18.5:
    classificação= 'Abaixo do peso'
elif IMC >= 18.5 and IMC <= 24.9:
    classificação= 'Peso normal'
elif IMC >= 25 and IMC <= 29.9:
    classificação= 'Sobrepeso'
elif IMC >= 30 and IMC <= 39.9:
    classificação= 'Obesidade'
else:
    classificação= 'Obesidade grave'
print('=' * 35 )
print(f'Relatorio de IMC {nome.upper()}')
print('-' * 35)
print(f'IMC calculado: {IMCarredondado}.')
print(f'Classificação: {classificação}.')
print('=' * 35)