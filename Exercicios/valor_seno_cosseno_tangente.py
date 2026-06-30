from math import radians, sin, cos, tan
Angulo=float(input('Digite o valor do angulo: '))
Seno=sin(radians(Angulo))
Cosseno=cos(radians(Angulo))
Tangente=tan(radians(Angulo))
print(' O seu angulo é {}\n O valor do Seno é {:.2f}\n O valor do Cosseno é {:.2f}\n O valor da Tangente é {:.2f}'.format(Angulo,Seno, Cosseno, Tangente))