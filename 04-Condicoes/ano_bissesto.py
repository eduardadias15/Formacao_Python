Ano = int(input('Digite o ano que você deseja: '))
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 ==0:
    print(f'O ano {Ano} é bissexto!')
else:
    print(f'O ano {Ano} não é bissexto.')
    