# Crie um programa que leia dois números e mostre as quatro operações matemáticas simples entre eles.
numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))
print('A soma entre ', numero_1, 'e', numero_2, 'é igual a ', numero_1 + numero_2)
print('A subtração entre {} e {} é igual a {}'.format(numero_1, numero_2, numero_1 - numero_2))
print('A multiplicação entre ', numero_1, 'e', numero_2, 'é igual a ', numero_1 * numero_2)
print('A divisão entre {} e {} é igual a {}'.format(numero_1, numero_2, numero_1 / numero_2))
