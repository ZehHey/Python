# Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# O programa deverá ler um numero pelo teclado e mostrá - la por extenso.

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))

    if 0 <= n <= 20:
        break
    print('Valor inválido. ', end='')

print(f'\033[1;34m{n}\033[m por extenso é: \033[1;31m{num[n]}\033[m.')
