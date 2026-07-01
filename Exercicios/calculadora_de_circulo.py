import math
raio= float(input('Digite o valor do raio do círculo: '))
area= math.pi * (raio**2)
perimetro= 2 * math.pi * raio

print('=' * 30)
print(f'A área do círculo é: {area:.2f}cm²')
print(f'O perímetro do círculo é: {perimetro:.2f}cm²')
print('=' * 30)