L1 =float(input('Me informe o primeiro lado do triângulo: '))
L2 = float(input('Me informe o segundo lado do triângulo: '))
L3 = float(input('Me informe o terceiro lado do triângulo: '))
Perimetro = (L1 + L2 + L3)

if L1 == L2 and L2 == L3:
    tipo= 'Equilátero'
elif L1 == L2 or L2 == L3 or L1 == L3:
    tipo= 'Isósceles'
else: 
    tipo= 'Escaleno'
    
print(f'O triângulo é do tipo {tipo} e seu perímetro é de {Perimetro:.2f}.')