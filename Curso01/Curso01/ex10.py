# Crie um programa que leia quanto uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar
# Considere U$$1.00 = R$3.27

r = float(input('Quanto dineiro você tem na sua carteira? '))
d = 3.27
n = r / d
print('Você pode comprar US${:.2f}'.format (n))

