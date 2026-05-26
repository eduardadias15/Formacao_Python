# operadores de comparação

a = 10
b = 5

print(a == b) # False → 10 não é igual a 5
print(a != b) # True → 10 é diferente de 5
print(a > b) # True → 10 é maior que 5
print(a < b) # False → 10 não é menor que 5
print(a >= 10) # True → 10 é maior ou igual a 10
print(b <= 5) # True → 5 é menor ou igual a 5

x = 10 # = atribui valor à variável
x == 10 # == compara e retorna True/False

# uso com if
   
nota = 7.5

if nota >= 7.0:
        print("aprovado")
elif nota >= 5.0:
        print("recuperação")
else:
        print("reprovado")

# comparação encadeada

idade = 20

    # Python permite encadear comparações!
print(18 <= idade <= 65) # True

    # equivale a:
print(idade >= 18 and idade <= 65)