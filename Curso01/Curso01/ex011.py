# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

# Area do retangulo = A = a x l = xm²
# Litros de tinta = x/2

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
x = a * l
print('A área da sua parede é de {:.2f}m²'.format(x))
t = x / 2
print('{:.2f} litros de tinta são necessários para pintar a parede.'.format(t))
