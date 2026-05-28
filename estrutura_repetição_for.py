# Exemplo utilizando um iterável

Texto = input("Digite um texto:")
vogais = "AEIOU"

for letra in Texto:
    if letra.upper()in vogais:
        print(letra, end ="")

print() # Quebra de linha para separar a saída


# Exemplo de uso do for com range
for número in range (0, 51, 5):
    print(número, end = "")