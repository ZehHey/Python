# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um pograma que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
nomes = [a, b, c, d]
shuffle(nomes)
print('A ordem de apresentação será:')
print('1-', nomes[0])
print('2-', nomes[1])
print('3-', nomes[2])
print('4-', nomes[3])
