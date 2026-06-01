MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
Idade = int(input("Digite a sua idade:"))

# Exemplo de uso do if

if Idade >= MAIOR_IDADE:
    print("Você pode tirar sua cnh!")

if Idade < MAIOR_IDADE:
    print("Você ainda não pode tirar sua cnh.")

# Exemplo de uso do if-else


if Idade >= MAIOR_IDADE:
    print("Você pode tirar sua cnh!")
else:
    print("Você ainda não pode tirar sua cnh.")
   

# Exemplo de uso do if-elif-else

if Idade >= MAIOR_IDADE:
    print("Você pode tirar sua cnh!")
elif Idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teóricas, menos as práticas.")
else:
    print("Você ainda não pode tirar sua cnh.")