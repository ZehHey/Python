# Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

n = (input('Digite um valor de 0 9999: '))
len(n)
if len(n) == 4:
    print('Unidade:', n[3])
    print('Dezena:', n[2])
    print('Centena:', n[1])
    print('Milhar:', n[0])
elif len(n) == 3:
    print('Unidade:', n[2])
    print('Dezena:', n[1])
    print('Centena:', n[0])
elif len(n) == 2:
    print('Unidade:', n[1])
    print('Dezena:', n[0])
else:
    print('Unidade:', n[0])