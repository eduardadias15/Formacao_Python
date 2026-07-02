velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade - 80)* 7

if velocidade > 80:
    print('Você foi multado por excesso de velocidade.')
    print(f'O valor da multa é de R${multa:.2f}.')
    print('Tome mais cuidado da proxima vez e dirija com segurança!')
else:
    print('Você esta dentro do limite de velocidade. Continue dirigindo com segurança!')
