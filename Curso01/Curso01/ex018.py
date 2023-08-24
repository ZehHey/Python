# Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, coseno e tangente desse angulo.

from math import sin, cos, tan, radians
an = float(input('Digite o angulo: '))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('O seno de {} é {:.2f}'.format(an, s))
print('O coseno de {} é {:.2f}'.format(an, c))
print('A tangente de {}é {:.2f}'.format(an, t))
