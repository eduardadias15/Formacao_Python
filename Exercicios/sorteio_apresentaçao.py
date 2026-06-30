from random import shuffle
N1= str(input('Digite o nome do primeiro aluno: '))
N2= str(input('Digite o nome do segundo aluno: '))
N3= str(input('Digite o nome do terceiro aluno: '))
N4= str(input('Digite o nome do quarto aluno: '))
Alunos = [N1, N2, N3, N4]
shuffle(Alunos)
print('A ordem de apresentação será: {}'.format(Alunos))

