número=str((input('Digite um número entre 0 e 9999:')))
número= número.zfill(4) # Preenche com zeros à esquerda para garantir que tenha 4 dígitos
print(f'A unidade: {número[3]}')
print(f'A dezena: {número[2]}')
print(f'A centena: {número[1]}')
print(f'O milhar: {número[0]}')
