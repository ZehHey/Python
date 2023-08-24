# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date
a = date.today().year
count = 0
count2 = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    i = a - n
    if i < 21:
        count += 1
    else:
        count2 += 1
print('\033[1;31m{}\033[m dessas pessoas ainda não atingiram a maioridade de 21 anos.'.format(count))
print('\033[1;32m{}\033[m dessas pessoas já atingiram a maioridade de 21 anos.'.format(count2))
