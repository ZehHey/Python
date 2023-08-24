# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

# calculo de 5% = x * 0.05

preco = float(input('Digite o preço do produto com os centavos: R$'))
d = preco * 0.05
n = preco - d
print('O valor com desconte é de R${:.2f}'.format (n))