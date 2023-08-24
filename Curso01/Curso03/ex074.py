# Crie um programa que vai gerar 5 numeros aleatórios e colocar numa tupla.
#Depois, mostre a listagem dos números e também indique o maior e menor valor entre eles.

from random import randint

a = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = menor = a[0]
for n in a:
    print(f'{n}',end=' ')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'\nMaior = {maior}')
print(f'Menor = {menor}')

print(f'Maior = {max(a)}')
print(f'Menor = {min(a)}')
