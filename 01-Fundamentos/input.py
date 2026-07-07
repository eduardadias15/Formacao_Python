# -----VARIÁVEIS -----
# Uma variável é um "espaço na memória" que guarda um valor.
# Em Python não precisamos declarar o tipo, ele é inferido automaticamente.

nome = "Maria"          # string (texto)
idade = 25               # int (número inteiro)
altura = 1.65            # float (número decimal)
esta_estudando = True    # bool (verdadeiro ou falso)

# Variáveis podem ter seu valor alterado a qualquer momento:
idade = 26
print(idade)  # 26

# ----- CONSTANTES -----
# Python não tem um tipo de dado "constante" de verdade.
# Por convenção usamos LETRAS MAIÚSCULAS para indicar que aquele valor não deveria ser alterado no código.

PI = 3.14159
LIMITE_IDADE_MAIOR = 18

# Isso é só uma convenção visual — o Python não vai impedir você de mudar PI = 5, mas outros programadores (e você mesmo no futuro) vão entender que não deveria.