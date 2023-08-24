# Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(x, y):
    a = x * y
    print(f'A área de um terreno de {x:.1f}m x {y:.1f} é de {a:.1f}m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)