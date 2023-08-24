# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
from datetime import date       #para reconhecer 0 como o ano atual
print('Digite o ano a ser analisado (0 pode corresponder ao ano atual):')
a = int(input('R: '))
b = (calendar.isleap(a))
print('-' * 40)
if a == 0:
    a = date.today().year
if b == True:
    print('{} é um ano bissexto'.format(a))
else:
    print('{} não é um ano bissexto.'.format(a))
print('-' * 40)