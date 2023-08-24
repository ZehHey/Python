# faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
# e que se encontram no intervalo de 1 a 500.

s = 0
cont = 0
for c in range (1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('O total de {} valores somados é {}.'.format(cont, s))
