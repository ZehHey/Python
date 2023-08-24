# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas;
# * O nome com todas as letras minúsculas;
# * Quantas letras tem ao todo sem considerar os espaços;
# * Quantas letras tem o primeiro nome.

n = str(input('Digite o nome completo:'))
print('Letras Maiúsculas:',n.upper())
print('Letras minúsculas:',n.lower())
n1 = n.split()
n2 = ''.join(n1)
#print('Seu primeiro nome tem {} letras'.format(n,find(' ')))
print('Seu nome tem o total de',len(n2),'letras.')
print('Seu primeiro nome tem o total de',len(n1[0]),'letras.')



