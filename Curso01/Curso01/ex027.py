# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o
# primeiro e o ultimo nome separadamente.

n = str(input('Digite o nome completo:')).strip()
n1 = n.split()
print('Primeiro nome: {}'.format(n1[0]).title())
print('Último nome: {}'.format(n1[len(n1)-1]).title())
