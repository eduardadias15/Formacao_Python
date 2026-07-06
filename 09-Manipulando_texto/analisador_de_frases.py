frase=str(input('Digite uma frase: ')).strip()
print(frase.upper())
print(frase.lower())
print(frase.upper().count('A'))   # conta ignorando maiúscula/minúscula
print(frase.upper().find('A'))    # encontra ignorando maiúscula/minúscula
print(frase[::-1])
