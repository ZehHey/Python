# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.


print('Digite um número inteiro.')
n = int(input('R: '))
r = n % 2
if r == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))