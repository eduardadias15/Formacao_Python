x = 10

# forma longa -> forma curta (mesmo resultado)

x = x + 5 # ou x += 5 # x = 15
x = x - 3 # ou x -= 3 # x = 12
x = x * 2 # ou x *= 2 # x = 24
x = x / 4 # ou x /= 4 # x = 6.0
x = x ** 2 # ou x **= 2 # x = 36.0



# exemplo 

pontos = 0
vidas = 3

# jogador acerta → ganha 10 pontos
pontos += 10
pontos += 10
print("Pontos:", pontos) # 20

# jogador erra → perde 1 vida
vidas -= 1
print("Vidas:", vidas) # 2

# bônus → dobra os pontos
pontos *= 2
print("Pontos:", pontos) # 40



# atribuiçao multipla 

# atribuir o mesmo valor a várias variáveis
a = b = c = 0
print(a, b, c) # 0 0 0

# atribuir valores diferentes de uma vez
x, y, z = 1, 2, 3
print(x, y, z) # 1 2 3

# trocar valores entre variáveis
x, y = y, x
print(x, y) # 2 1
