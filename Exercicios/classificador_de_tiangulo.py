L1 =float(input('Me informe o primeiro lado do triângulo: '))
L2 = float(input('Me informe o segundo lado do triângulo: '))
L3 = float(input('Me informe o terceiro lado do triângulo: '))
Perímetro = (L1 + L2 + L3)

if L1 == L2 and L2 == L3:
    print(f'Os lados do seu triângulo são {L1}, {L2} e {L3}, então seu triângulo é equilátero e o perímetro é {Perímetro}')

elif L1 == L2 or L2 == L3 or L1 == L3:
    print(f'Os lados do seu triângulo são {L1}, {L2} e {L3}, então seu triângulo é isósceles e o perímetro é {Perímetro}')
else: 
    print(f'Os lados do seu triângulo são {L1}, {L2} e {L3}, então o seu triângulo é escaleno e o perímetro é {Perímetro}. ')