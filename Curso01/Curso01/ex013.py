# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

# calculo de 15% = x * 0.15

s = float(input('Digite seu salário: R$'))
n = s + (s * 15/100)
print('Seu novo salário é de R${:.2f}'.format(n))