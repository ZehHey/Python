# Escreva um programa para aprovar o empréstimo bancário para uma compra de uma casa.
# O programa vai perguntar o valor da casa, o salário da pessoa e em quantos anos ela vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário, ou então o
# empéstimo será negado.


print('Digite o valor da casa:')
v = float(input('R$: '))
print('Digite seu salário:')
s = float(input('R$: '))
print('Pretende pagar em quantos anos: ')
a = int(input(''))
p = (v / (a * 12))
x = (s * 30 / 100)
if p > x:
    print('O valor da parcela de \033[1;31mR${:.2f}\033[m excede 30% do seu salário.'.format(p))
    print('Infelizmente o crédito \033[1;31mnão\033[m foi aprovado.')
else:
    print('O valor da parcela é de \033[1;32mR${:.2f}\033[m.'.format(p))
    print('Parabéns! Seu crédito \033[1;32mestá aprovado\033[m.')
