# Faça um programa que leia o comprimento do cateto oposto e adjacente de um triangulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
# calculo  a² = b² + c²
from math import hypot
b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(b, c)
print('A hipotenusa vai medir {:.2f}.'.format(h))
