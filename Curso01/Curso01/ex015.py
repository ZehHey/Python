# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias que ele ficou alugado. Calcule o preço, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

a1 = int(input('Quantos dias alugado?  '))
a2 = float(input('Quantos Km rodados?  '))
d = a1 * 60
km = a2 * 0.15
print('-'*30)
print('O total a pagar é de R${}'.format(d + km))
print('-'*30)

