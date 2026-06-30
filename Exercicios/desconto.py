X=float(input('Qual o valor do produto? R$'))
D=float(input('Qual a porcentagem de desconto?'))
desconto= X - (X * D / 100)
print(' O valor do produto é R${:.2f}\n a quantidade de desconto que você esta recebendo é de {}%\n o valor do produto com o desconto é de R${:.2f}'.format(X, D, desconto))