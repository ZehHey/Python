# Escreva um programa que leia o comprimento de tres retas e diga ao usuário de elas podem ou não
# formar um triângulo.

n1 = float(input('Medida da reta 01: '))
n2 = float(input('Medida da reta 02: '))
n3 = float(input('Medida da reta 03: '))
a = n1 + n2
b = n1 + n3
c = n2 + n3
if a > n3 and b > n2 and c > n1:
    print('Com essas medidas é possivel formar um triângulo.')
else:
    print('Não é possível formar um triângulo com as medidas indicadas.')