# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: O numero 6.127 tem a parte inteira 6.

from math import trunc
n = float(input('Digite um numero: '))
print('O número {} tem a sua parte inteira {}'.format (n, trunc(n)))