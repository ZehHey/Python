# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome escolhido.
# nomes = ('João', 'Luiz', 'Ana', 'Bia')

from random import choice
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
nome = [a, b, b, d]
x = choice(nome)
print('-' * 35)
print('O aluno sorteado é: ', x)
print('-' * 35)