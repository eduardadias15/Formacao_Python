from random import choice
N1= str(input('Digite o nome do primeiro aluno: '))
N2= str(input('Digite o nome do segundo aluno: '))
N3= str(input('Digite o nome do terceiro aluno: '))
N4= str(input('Digite o nome do quarto aluno: '))

Alunos = [N1, N2, N3, N4]
Sorteado = choice(Alunos)
print('O aluno sorteado para apagar o quadro foi: {}'.format(Sorteado))