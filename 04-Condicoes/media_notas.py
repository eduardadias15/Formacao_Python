N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
N3 = float(input('Digite a terceira nota: '))
Media = (N1 + N2 + N3) / 3

if Media >= 6:
    print(f'Sua média foi {Media:.1f} e você foi aprovado!')
else:
    print(f'Sua média foi {Media:.1f} e você foi reprovado!')