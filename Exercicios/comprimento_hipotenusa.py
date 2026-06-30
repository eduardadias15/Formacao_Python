import math

CO=float(input('Digite o valor do cateto oposto: '))
CA=float(input('Agora digite o valor do cateto adjacente: '))
HI= math.hypot(CO, CA)
print('O valor da hipotenusa é {:.2f}'.format(HI))
