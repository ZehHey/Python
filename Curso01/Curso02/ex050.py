# Escreva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares.

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n
print('Você informou {} números pares e a soma entre eles é {}.'.format(cont, s))
