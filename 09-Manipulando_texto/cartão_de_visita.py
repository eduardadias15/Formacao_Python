nome= input('Digite seu nome completo: ')
idade= int(input('Digite a sua idade: '))
cidade= input('Nos informe a cidade onde você mora: ')
x= 100-idade

print(f'Seu nome é {nome.upper()} você tem {idade} anos e você mora na cidade de {cidade}')
print(f'Faltam {x} anos para você ter 100 anos de idade')
print(f'Seu nome completo tem {len(nome.replace(" ", ""))} letras')