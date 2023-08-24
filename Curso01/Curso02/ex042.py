# Faça um programa que leia o comprimento de 3 retas e alem de dizer se é possivel formar um triangulo,
# qual tipo de triangulo é possivel formar.
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
a = r1 + r2
b = r1 + r3
c = r2 + r3
if a > r3 and b > r2 and c > r1:
    if r1 == r2 == r3:
        print('É possivel formar um triângulo equilátero.')
    elif r1 != r2 != r3 != r1:
        print('É possível formar um triângulo escaleno.')
    else:
        print('É possível formar um triângulo isósceles.')
else:
    print('Com as medidas apresentadas não é possível formar um triângulo.')
